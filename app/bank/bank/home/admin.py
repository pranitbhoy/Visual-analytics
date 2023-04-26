from django.contrib import admin

# Register your models here.
from.models import USER_details
class productAdmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','email_id']


admin.site.register(USER_details,productAdmin)