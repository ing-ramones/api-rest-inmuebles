from django.contrib import admin

from real_estate_api import models

admin.site.site_header = "Welcome to the administration site"
admin.site.site_title = "Real Estate Admin"
admin.site.index_title = "Inventory"

admin.site.register(models.Estate)
