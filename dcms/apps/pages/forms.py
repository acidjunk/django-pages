from django.forms import ModelForm
from models import Page, PageFile, PagePhoto


class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ['name', 'slogan', 'url', 'parent', 'sidebar_right']


class FileForm(ModelForm):
    class Meta:
        model = PageFile
        fields = '__all__'


class PhotoForm(ModelForm):
    class Meta:
        model = PagePhoto
        fields = '__all__'
