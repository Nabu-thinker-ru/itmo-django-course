# -*- encoding: utf-8 -*-
from django.db import models

class Country(models.Model):
    name = models.CharField('Название',
                        max_length=150,
                        )

    show = models.BooleanField('Показывать на сайте',
                        default=True, )

    order = models.IntegerField('Порядок',
                        default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        ordering = ['order', 'name']

class City(models.Model):
    name = models.CharField('Город',
                            max_length=150,
                            unique=True,
                            )
    slug = models.CharField('Ссылка',
                            max_length=150,
                            null = True,
                            blank = True)
    syn = models.ForeignKey('self',
                            blank = True,
                            null = True,
                            verbose_name = 'Синоним',
                            related_name = 'synonyms',
                            )
    country = models.ForeignKey(Country,
                                related_name = 'cities',
                                null=True,
                                blank=True)

    show = models.BooleanField('Показывать на сайте',
                            default = True,)
    order = models.IntegerField('Порядок',
                            default = 0)
    added = models.DateTimeField('Добавлен',
                            auto_now_add = True)
    changed = models.DateTimeField('Изменен',
                            auto_now = True)

    def __str__(self):
        return self.name

    def save(self):
        if not self.slug:
            self.slug = save_for_url(self.name)
        return super(City, self).save()

    def get_absolute_url(self):
        return self.slug

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['order', 'name']

def to_translit(str):
    """
    Переводит русские буквы в транслит
    """
    ar = {u'А':'A',u'Б':'B',u'В':'V',u'Г':'G',u'Д':'D',u'Е':'E',u'Ё':'E',u'Ж':'J',u'З':'Z',u'И':'I',u'Й':'Y',u'К':'K',u'Л':'L',u'М':'M',u'Н':'N',u'О':'O',u'П':'P',u'Р':'R',u'С':'S',u'Т':'T',u'У':'U',u'Ф':'F',u'Х':'H',u'Ц':'C',u'Ч':'CH',u'Ш':'SH',u'Щ':'SHCH',u'Ы':'Y',u'Э':'E',u'Ю':'YU',u'Я':'YA',u'а':'a',u'б':'b',u'в':'v',u'г':'g',u'д':'d',u'е':'e',u'ё':'e',u'ж':'j',u'з':'z',u'и':'i',u'й':'y',u'к':'k',u'л':'l',u'м':'m',u'н':'n',u'о':'o',u'п':'p',u'р':'r',u'с':'s',u'т':'t',u'у':'u',u'ф':'f',u'х':'h',u'ц':'c',u'ч':'ch',u'ш':'sh',u'щ':'shch',u'ы':'y',u'э':'e',u'ю':'yu',u'я':'ya',u'Ъ':'',u'ъ':'',u'Ь':'',u'ь':''}
    translitstr = ''
    for l in u'%s'%str:
        try:
            translitstr = translitstr + ar[l]
        except KeyError:
            translitstr = translitstr + l
    return translitstr

def save_for_url(str):
    """
    В полученой строке срезается HTML и все \W меняются на подчеркивание
    """
    import re
    r = re.compile('\W')
    return re.sub('\W','_',to_translit(re.sub('<[^>]*?>','',str)))