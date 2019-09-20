from django.contrib import admin

from .models import UserInfo, BloodRecord

admin.site.register(UserInfo)
admin.site.register(BloodRecord)
