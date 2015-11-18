# Register models here

from django.contrib import admin

from .models import Forum, Thread, Post

class ForumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


class ThreadAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('topic',)}


#class PostAdmin(admin.ModelAdmin):
#    prepopulated_fields = {'slug':('content',)} things not needed anymore

admin.site.register(Forum, ForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post)