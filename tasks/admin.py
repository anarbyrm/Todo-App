from django.contrib import admin
from django.db.models import fields
from .models import Task


admin.site.register(Task)
