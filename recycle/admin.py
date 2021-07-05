from django.contrib import admin
from recycle.models import *


admin.site.register(Product, admin.ModelAdmin)
admin.site.register(Category, admin.ModelAdmin)
admin.site.register(Article, admin.ModelAdmin)
admin.site.register(Region, admin.ModelAdmin)
admin.site.register(Punkt, admin.ModelAdmin)
admin.site.register(Agent, admin.ModelAdmin)

