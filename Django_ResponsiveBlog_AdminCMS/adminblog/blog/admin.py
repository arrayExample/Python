from django.contrib import admin
from .models import Post, homepageMessage
from django.contrib.auth.models import User, Group


class PostAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(Post, PostAdmin)
admin.site.register(homepageMessage)
admin.site.unregister(User)
admin.site.unregister(Group)
