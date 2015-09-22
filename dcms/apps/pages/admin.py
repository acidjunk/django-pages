from django.contrib import admin
from .models import Page, Row, Column, Content, Photo, Form, FormElement, File


class PageAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_by', 'created_on', 'modified_on']


class RowAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_by', 'created_on', 'modified_on']


class ColumnAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_by', 'created_on', 'modified_on']


class ContentAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_by', 'created_on', 'modified_on']


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_by', 'created_on', 'modified_on']


class FormAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_by', 'created_on', 'modified_on']


class FormElementAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_by', 'created_on', 'modified_on']


class FileAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_by', 'created_on', 'modified_on']


admin.site.register(Page, PageAdmin)
admin.site.register(Row, RowAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Form, FormAdmin)
admin.site.register(FormElement, FormElementAdmin)
admin.site.register(File, FileAdmin)
