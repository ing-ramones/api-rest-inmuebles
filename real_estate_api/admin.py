from django.contrib import admin

from real_estate_api import models

admin.site.site_header = "Welcome to the administration site"
admin.site.site_title = "Real Estate Admin"
admin.site.index_title = "Inventory"


class EstateAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'area',
                    'rooms', 'garage', 'geom', 'other', 'company_id',)

    readonly_fields = ['created_by_id', 'last_modified_by_id']


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'nif',)

    readonly_fields = ['created_by_id', 'last_modified_by_id']


admin.site.register(models.Estate, EstateAdmin)
admin.site.register(models.Company, CompanyAdmin)
