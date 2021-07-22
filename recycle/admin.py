from recycle.models import *
from recycle.forms import CsvImportForm
import codecs
from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
import csv

admin.site.register(Category, admin.ModelAdmin)
admin.site.register(Article, admin.ModelAdmin)
admin.site.register(Region, admin.ModelAdmin)
admin.site.register(Punkt, admin.ModelAdmin)
admin.site.register(Agent, admin.ModelAdmin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    change_list_template = "admin/products_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            reader = csv.DictReader(codecs.iterdecode(csv_file, 'utf-8'))
            for row in reader:
                category, catcreate = Category.objects.get_or_create(cat_name = row['категория'])
                product, prcreate = Product.objects.update_or_create( id=row['код'], product_price = row['Цена, р/ед'], defaults={'id':row['код'], 'product_name':row['Название'], 'color':row['ед. изм.'], 'product_price' :row['Цена, р/ед'], 'category':category, 'product_image':'IMG_4280_копия.jpg'})
                print(product, prcreate)

                # try:
                #     print(row['код'])
                #     product = Product.objects.create(id=row['код'], product_name=row['Название'], color=row['ед. изм.'], product_price = row['Цена, р/ед'], category=category, product_image='IMG_4280_копия.jpg')
                # except:
                #     print(row['код'])
                #     product1 = Product.objects.get(id=row['код'])
                #     print(product1)


            self.message_user(request, "Продукты импортированы")
            return redirect("..")
        if request.method == "GET":
            form = CsvImportForm()
            payload = {"form": form}
            return render(request, "admin/csv_form.html", payload)