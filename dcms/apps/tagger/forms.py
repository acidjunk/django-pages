from django.forms import ModelForm
from .models import TaggedItem


class TagItForm(ModelForm):

    class Meta:
        model = TaggedItem
        fields = ['tag']
