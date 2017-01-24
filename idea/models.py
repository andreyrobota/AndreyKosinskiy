from django.db import models

from django.db.models import TextField , IntegerField , CharField

from django.db.models import TextField, IntegerField,CharField

# Create your models here.\

class IdeaUser(models.Model):
    class Meta():
        db_table="idea"
        verbose_name_plural=u"Идеи"


    idea_name=CharField(max_length=200,blank=True)#Заголовок Идеи
    idea_name=CharField(max_length=200)#Заголовок Идеи
    idea_text=TextField()#Текст Идеи
    idea_rank= IntegerField()#Оценка Идеи
    def __unicode__(self):
        return self.idea_name
