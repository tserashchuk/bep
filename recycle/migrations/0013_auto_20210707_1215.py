# Generated by Django 3.2.4 on 2021-07-07 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0012_alter_category_cat_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='region_slug',
            field=models.CharField(default='region2021-07-07 12:15:08.564407', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default='slug2021-07-07 12:15:08.542692', max_length=200, verbose_name='URL'),
        ),
    ]
