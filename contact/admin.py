from django.contrib import admin
from .models import ContactMessage, Call


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
admin.site.register(ContactMessage, ContactMessageAdmin)



class CallAdmin(admin.ModelAdmin):
    list_display = ['number']
admin.site.register(Call, CallAdmin)