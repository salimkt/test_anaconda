from django.contrib import admin
from register.models import Member, Area, HouseName, Dependent


admin.site.register(HouseName)
admin.site.register(Area)
admin.site.register(Member)
admin.site.register(Dependent)
