from django.contrib import admin

from .models import Profile,Post
from .models import address
# Register your models here.

admin.site.register(Profile)
admin.site.register(address)
admin.site.register(Post)
