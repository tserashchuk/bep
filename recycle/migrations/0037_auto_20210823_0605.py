# Generated by Django 3.2.4 on 2021-08-23 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0036_auto_20210820_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='agent_metadesc',
            field=models.CharField(max_length=300, verbose_name='Описание для Open Graph (og:description)'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_metadesc',
            field=models.CharField(max_length=300, verbose_name='Описание для Open Graph (og:description)'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.CharField(default='article2021-08-23 06:05:39.899089', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_metadesc',
            field=models.CharField(blank=True, max_length=300, verbose_name='Описание для Open Graph (og:description)'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default='slug2021-08-23 06:05:39.696916', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_metadesc',
            field=models.CharField(max_length=300, verbose_name='Описание для Open Graph (og:description)'),
        ),
        migrations.AlterField(
            model_name='punkt',
            name='punkt_metadesc',
            field=models.CharField(max_length=300, verbose_name='Описание для Open Graph (og:description)'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_metadesc',
            field=models.CharField(max_length=300, verbose_name='Описание для Open Graph (og:description)'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_slug',
            field=models.CharField(default='region2021-08-23 06:05:39.899931', max_length=200, verbose_name='URL'),
        ),
    ]
