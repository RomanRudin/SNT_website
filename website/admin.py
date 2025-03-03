from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Contacts, Gallery, Docs, News, UsefuleInfo, SubmissionsElectricity, User, LandPlot, WaterMeter, WaterSubmission
from .forms import GroupAdminForm


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

class UserAdmin(admin.ModelAdmin):
    fields = ["email", "password", 'username', 'first_name', 'last_name']


class LandPlotAdmin(admin.ModelAdmin):
    fields = ['user', 'street', 'house_number',  'district']


class WaterMeterAdmin(admin.ModelAdmin):
    fields = ['reg_number', 'land_plot', 'created_at']

class WaterSubmissionAdmin(admin.ModelAdmin):
    fields = ['value', 'created_at']



admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Docs, DocsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(UsefuleInfo, UsefuleInfoAdmin)
admin.site.register(SubmissionsElectricity, SubmissionsElectricityAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(LandPlot, LandPlotAdmin)
admin.site.register(WaterMeter, WaterMeterAdmin)
admin.site.register(WaterSubmission, WaterSubmissionAdmin)


# Unregister the original Group admin.
admin.site.unregister(Group)

# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']

# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)
