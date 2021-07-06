import json

from django.shortcuts import render
from django.views import View

from recycle.models import *


class Home(View):
    def get(self, request):
        cateory = Category.objects.all()
        data = []
        for cat in cateory:
            products = cat.product_set.all()
            data.append({'categoryName': cat.cat_name, 'categoryID': cat.id})
        data = json.dumps(list(data))
        return render(request, 'index.html', {'data': data})

    def post(self, catID):
        return '123'


class CategoryView(View):
    def get(self, request):
        categorys = Category.objects.all()

        return render(request, 'categorys.html', {'categorys': categorys})


class Contact(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'contact.html', {'products': products})


class Skupka(View):
    def get(self, request):
        categorys = Category.objects.all()
        return render(request, 'skupka.html', {'categorys': categorys})


class Punkty(View):
    def get(self, request):
        regions = Region.objects.all()
        return render(request, 'punkty.html', {'regions':regions})

class News(View):
    def get(self, request):
        articles = Article.objects.all()
        return render(request, 'news.html', {'articles':articles})

class Bytov(View):
    def get(self, request):
        return render(request, 'priem.html')

class Vyvoz(View):
    def get(self, request):
        return render(request, 'vyvoz.html')

class Yuriki(View):
    def get(self, request):
        return render(request, 'yuriki.html')