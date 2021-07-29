from django.contrib.sitemaps import Sitemap
from recycle.models import Category, Article, Region
from django.shortcuts import reverse
class CategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8


    def items(self):
        return Category.objects.all().order_by('cat_slug')

class ServicesSitemap(Sitemap):

    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return ['contact','skupka','punkty','news','priem','yuriki','bezvozm','spisanie','vyvoz']

    def location(self, item):
        return reverse(item)

class HomeSitemap(Sitemap):

    changefreq = "monthly"
    priority = 1

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)

class ArticlesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.2

    def items(self):
        return Article.objects.all().order_by('article_slug')

class RegionSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.2

    def items(self):
        return Region.objects.all().order_by('region_slug')


