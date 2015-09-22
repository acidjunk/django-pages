from django.forms import ModelForm
from models import Page, File, Photo


class PageForm(ModelForm):
    class Meta:
        model = Page
        fields = ['name', 'slogan', 'url', 'parent', 'sidebar_right']


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = '__all__'


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
