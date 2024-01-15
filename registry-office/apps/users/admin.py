from django.contrib import admin
from .models import Person, PersonDetail, Address
# Register your models here.


@admin.register(Address)
class AddresAdmin(admin.ModelAdmin):
    # list_display = ['street', 'city']
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ['rowCount']


@admin.register(PersonDetail)
class PersonDetailAdmin(admin.ModelAdmin):
    pass
