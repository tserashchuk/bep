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
        return render(request, 'index.html')

    def post(self, catID):
        return '123'

class ArticleView(View):
    def get(self, request,article_slug):
        article = Article.objects.get(article_slug=article_slug)
        return render(request, 'article.html', {'article':article})

class CategoryView(View):
    def get(self, request):
        categorys = Category.objects.all()
        return render(request, 'categorys.html', {'categorys': categorys})

class Products(View):
    def get(self, request, cat_slug):
        category = Category.objects.get(cat_slug=cat_slug)
        return render(request, 'products.html', {'category': category})


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
        stock = False
        articles = Article.objects.all()
        for article in articles:
            if article.isStock == True:
                stock = True
        return render(request, 'news.html', {'articles':articles, 'stock':stock})

class Bytov(View):
    def get(self, request):
        return render(request, 'priem.html')

class Vyvoz(View):
    def get(self, request):
        return render(request, 'vyvoz.html')

class Yuriki(View):
    def get(self, request):
        return render(request, 'yuriki.html')

class Bezvozmezdno(View):
    def get(self, request):
        return render(request, 'bezvozmezdno.html')

class RegionView(View):
    def get(self, request, region_slug):
        region = Region.objects.get(region_slug=region_slug)
        return render(request, 'regionpage.html', {'region':region})

class Spisanie(View):
    def get(self, request):
        return render(request, 'spisanie.html')