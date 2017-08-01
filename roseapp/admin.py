from django.contrib import admin

# Register your models here.

from .models import Ocountry ,Obrands,Oshop,Ocatergory,Opacking,Osubcatergory,Oproducts,Oshp_price
#from . import models #import Ocountry ,Obrands,Oshop,Ocatergory,Opacking,Osubcatergory,Oproducts





#class Ocounty(admin.modeladmin):
#	class Meta:
#		model = Ocountry
@admin.register(Oproducts)
class Oproductsadmin(admin.ModelAdmin):
	list_display = ['pd_name','pd_catid','pd_subcatid']


admin.site.register(Ocountry)
admin.site.register(Obrands)
admin.site.register(Oshop)
admin.site.register(Ocatergory)
admin.site.register(Opacking)
admin.site.register(Osubcatergory)
admin.site.register(Oshp_price)