"""RPRO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from recycle import views, rest

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('p/', views.CategoryView.as_view(), name='category'),
    path('p/<str:cat_slug>', views.Products.as_view(), name='products'),
    path('c/', views.Contact.as_view(), name='contact'),
    path('s/', views.Products.as_view(), name='skupka'),
    path('pp/', views.Punkty.as_view(), name='punkty'),
    path('news/', views.News.as_view(), name='news'),
    path('b/', views.Bytov.as_view(), name='priem'),
    path('v/', views.Vyvoz.as_view(), name='vyvoz'),
    path('y/', views.Yuriki.as_view(), name='yuriki'),
    path('editorjs/', include('django_editorjs_fields.urls')),
    path('api-auth/', include(rest.router.urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
