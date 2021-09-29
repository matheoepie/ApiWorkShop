#from Workshop.apiWorkShop.models import Situation, UserMessage
from django.contrib import admin
from .models import UserMessage, Situation
# Register your models here.
admin.site.register(Situation)
admin.site.register(UserMessage)
