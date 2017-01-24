from django.db.models import TextField
from django.forms import ModelForm, CharField, IntegerField
from idea.models import IdeaUser


class  IdeaForm (ModelForm):
    class Meta:
        model=IdeaUser
        fields=['idea_name']
