from django.contrib import admin

# Register your models here.
from beex.models import User as Beex_user

admin.site.register(Beex_user)