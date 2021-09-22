import json

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings

from recycle.models import *
from bitrix24 import *

class Home(View):
    def get(self, request):
        categorys = Category.objects.all()
        data = []
        for cat in categorys:
            products = cat.product_set.all()
            data.append({'categoryName': cat.cat_name, 'categoryID': cat.id})
        data = json.dumps(list(data))
        return render(request, 'index.html',{'categorys': categorys})

    def post(self, request):

        try:
            products12 = request.POST['ppp']
            phone = request.POST['PHONE']
            name = request.POST['NAME']
            bx24 = Bitrix24('https://rpro.bitrix24.by/rest/92/qlddk8ebw7pcwiz6/')
            bx24.callMethod('crm.lead.add',
                            fields={
                                    "TITLE": name,
                                    "NAME": 'sdfsfd',
                                    "STATUS_ID": "NEW",
                                    "OPENED": "Y",
                                    "ASSIGNED_BY_ID": 76,
                                    "PHONE": [{"VALUE": phone, "VALUE_TYPE": "WORK"}],
                                    "UF_CRM_1614585863220":products12
                                },
            )
        except Exception as e:
            print(e)



        return render(request, 'index.html')

class ArticleView(View):
    def get(self, request, article_slug):
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


class Singleproduct(View):
    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        return render(request, 'product.html', {'product': product})


class Contact(View):
    messageSent = False
    products = Product.objects.all()
    
    def get(self, request):
        return render(request, 'contact.html', {'products': self.products, 'messageSent':  self.messageSent})
        
    def post(self, request):
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        send_mail(
            f"{surname} {name}",
            message,
            email,
            ["dierbekibragimov@gmail.com  "]
        )
        messageSent = True
        return render(request, 'contact.html', {'products': self.products, 'messageSent': messageSent}) 

class Skupka(View):
    def get(self, request):
        categorys = Category.objects.all()
        regions = Region.objects.all()
        return render(request, 'skupka.html', {'categorys': categorys,'regions':regions})


class Punkty(View):
    def get(self, request):
        regions = Region.objects.all()
        return render(request, 'punkty.html', {'regions':regions})

class News(View):
    def get(self, request):
        stock = False
        articles = Article.objects.all()
        paginator = Paginator(articles, 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        for article in articles:
            if article.isStock == True:
                stock = True
        return render(request, 'news.html', {'articles':articles, 'stock':stock, 'page_obj': page_obj})

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

def handle_error404(request, exception):
    return render(request, "404.html", status=404)
# a.bobkov@rpro.by