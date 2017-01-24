from django.db import models
<<<<<<< HEAD
from django.db.models import TextField , IntegerField , CharField
=======
from django.db.models import TextField, IntegerField,CharField
>>>>>>> fc3e45350bbd6e02ca2d590c10e9ed7582265998
# Create your models here.\

class IdeaUser(models.Model):
    class Meta():
        db_table="idea"
        verbose_name_plural=u"Идеи"

<<<<<<< HEAD
    idea_name=CharField(max_length=200,blank=True)#Заголовок Идеи
=======
    idea_name=CharField(max_length=200)#Заголовок Идеи
>>>>>>> fc3e45350bbd6e02ca2d590c10e9ed7582265998
    idea_text=TextField()#Текст Идеи
    idea_rank= IntegerField()#Оценка Идеи
    def __unicode__(self):
        return self.idea_name
