from django.contrib import admin

# Register your models here.

from .models import MainRoom, Topic, Message, User

admin.site.register(User)
admin.site.register(MainRoom)
admin.site.register(Topic)
admin.site.register(Message)
