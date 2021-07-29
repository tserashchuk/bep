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
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from recycle import views, rest
from recycle.sitemap import CategorySitemap, ArticlesSitemap, ServicesSitemap, RegionSitemap, HomeSitemap

sitemaps = {
    'home': HomeSitemap,
    'category': CategorySitemap,
    'article': ArticlesSitemap,
    'service': ServicesSitemap,
    'punkt': RegionSitemap

}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('category/', views.CategoryView.as_view(), name='category'),
    path('category/<str:cat_slug>', views.Products.as_view(), name='products'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('skupka-radiodetaley/', views.Skupka.as_view(), name='skupka'),
    path('punkty-priema/', views.Punkty.as_view(), name='punkty'),
    path('news/', views.News.as_view(), name='news'),
    path('news/<str:article_slug>', views.ArticleView.as_view(), name='article'),
    path('priem-bytovoy-tehniki/', views.Bytov.as_view(), name='priem'),
    path('vyvos-bytovoy-tehniki/', views.Vyvoz.as_view(), name='vyvoz'),
    path('utilizaciya-tehniki/', views.Yuriki.as_view(), name='yuriki'),
    path('bezvozmezdnaya/', views.Bezvozmezdno.as_view(), name='bezvozm'),
    path('spisanie-teh-sostoyanie/', views.Spisanie.as_view(), name='spisanie'),
    path('region/<str:region_slug>', views.RegionView.as_view(), name='region'),
    path('editorjs/', include('django_editorjs_fields.urls')),
    path('api-auth/', include(rest.router.urls)),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
