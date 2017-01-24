from django.contrib import admin
from idea.models import IdeaUser
# Register your models here.



class IdeaAdmin(admin.ModelAdmin):
    fields=['idea_name','idea_text','idea_rank',]#
    list_display = ("idea_name","idea_text","idea_rank")
admin.site.register(IdeaUser,IdeaAdmin)
