from django.contrib import admin
from .models import Contacts, Gallery, Docs, News, UsefuleInfo, SubmissionsElectricity, SubmissionsWater, Access, Users



class ContactsAdmin(admin.ModelAdmin):
    fields = ["name", "email", "phone", "description", "job"]

class GalleryAdmin(admin.ModelAdmin):
    fields = []

class DocsAdmin(admin.ModelAdmin):
    fields = ["text", "date"]

class NewsAdmin(admin.ModelAdmin):
    fields = ["date", "title", "text"]

class UsefuleInfoAdmin(admin.ModelAdmin):
    fields = ["title", "text", "date"]

class SubmissionsElectricityAdmin(admin.ModelAdmin):
    fields = ["adress", "date", "data"]

class SubmissionsWaterAdmin(admin.ModelAdmin):
    fields = ["adress", "date", "data"]

class AccessAdmin(admin.ModelAdmin):
    fields = ["login"]

class UsersAdmin(admin.ModelAdmin):
    fields = ["login", "password"]



admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Docs, DocsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(UsefuleInfo, UsefuleInfoAdmin)
admin.site.register(SubmissionsElectricity, SubmissionsElectricityAdmin)
admin.site.register(SubmissionsWater, SubmissionsWaterAdmin)
admin.site.register(Access, AccessAdmin)
admin.site.register(Users, UsersAdmin)