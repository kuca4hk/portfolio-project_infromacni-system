from django.contrib import admin
from .models import Organization, VirtualOperation
# Register your models here.


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(VirtualOperation)
class VirtualOperationAdmin(admin.ModelAdmin):
    list_display = ['codeTypeId']
