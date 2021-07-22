import datetime
from django.db import models
from django_editorjs_fields import EditorJsJSONField, EditorJsTextField

PURCACHE_CHOICES = (
    ('Килограмм','кг'),
    ('Штук', 'шт')
)


class Category(models.Model):
    cat_name = models.CharField('Название категории продукта', max_length=200)
    cat_slug = models.CharField('URL', max_length=200, default='slug' + str(datetime.datetime.now()))
    cat_title = models.CharField('Заголовок title', max_length=200, blank=True)
    cat_metadesc = models.CharField('Описание description', max_length=300, blank=True)
    cat_short_desc = models.TextField('Короткое описание', blank=True)
    cat_desc = models.TextField('Полное описание', blank=True)
    cat_image = models.ImageField('Изображение категории', default='IMG_4280_копия.jpg')

    def __str__(self):
        return self.cat_name

class Product(models.Model):
    product_name = models.CharField('Название продукта', max_length=200)
    product_title = models.CharField('Заголовок title', max_length=200)
    color = models.CharField('Оплата', max_length=10, choices=PURCACHE_CHOICES, default='kg')
    product_price = models.CharField('Цена', max_length=200, blank=True, null=True)
    product_metadesc = models.CharField('Описание description', max_length=300)
    product_short_desc = models.TextField('Короткое описание', blank=True)
    product_desc = models.TextField('Полное описание', blank=True)
    product_image = models.ImageField('Изображение продукта', default='IMG_4280_копия.jpg')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.product_name

class Article(models.Model):
    article_name = models.CharField('Заголовок H1', max_length=200)
    article_title = models.CharField('Заголовок title', max_length=200)
    article_slug = models.CharField('URL', max_length=200, default='article' + str(datetime.datetime.now()))
    article_metadesc = models.CharField('Описание description', max_length=300)
    article_short_desc = models.TextField('Короткое описание', blank=True)
    article_image = models.ImageField('Изображение статьи')
    isStock = models.BooleanField(default=False)
    body_editorjs = EditorJsJSONField()

    def __str__(self):
        return self.article_name


class Region(models.Model):
    region_name = models.CharField('Название региона', max_length=200)
    region_slug = models.CharField('URL', max_length=200, default='region' + str(datetime.datetime.now()))
    region_title = models.CharField('Заголовок title', max_length=200)
    region_metadesc = models.CharField('Описание description', max_length=300)
    region_short_desc = models.TextField('Короткое описание', blank=True)
    body_editorjs = EditorJsJSONField()

    def __str__(self):
        return self.region_name


class Punkt(models.Model):
    punkt_name = models.CharField('Название пункта приема', max_length=200)
    punkt_title = models.CharField('Заголовок title', max_length=200)
    punkt_metadesc = models.CharField('Описание description', max_length=300)
    punkt_short_desc = models.TextField('Короткое описание', blank=True)
    punkt_geo = models.CharField('Описание description', max_length=300, default="55.659173,37.762848")
    punkt_image = models.ImageField('Изображение пункта')
    body_editorjs = EditorJsJSONField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.punkt_name

class Agent(models.Model):
    agent_name = models.CharField('Имя агента', max_length=200)
    agent_title = models.CharField('Заголовок title', max_length=200)
    agent_metadesc = models.CharField('Описание description', max_length=300)
    agent_short_desc = models.TextField('Короткое описание', blank=True)
    agent_image = models.ImageField('Фото агента')
    body_editorjs = EditorJsJSONField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.agent_name