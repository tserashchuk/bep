# Generated by Django 3.2.4 on 2021-07-29 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0024_auto_20210722_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.CharField(default='article2021-07-29 11:52:15.858769', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(default='placeholder.jpg', upload_to='', verbose_name='Изображение категории'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default='slug2021-07-29 11:52:15.837842', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='placeholder.jpg', upload_to='', verbose_name='Изображение продукта'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_slug',
            field=models.CharField(default='region2021-07-29 11:52:15.859199', max_length=200, verbose_name='URL'),
        ),
    ]
