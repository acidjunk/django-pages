from django.contrib import admin
from .models import Page, Row, Column, PageArticle, PagePhoto, PageForm, PageFormElement, PageFile


class PageAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_by', 'created_on', 'modified_on']


class RowAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_by', 'created_on', 'modified_on']


class ColumnAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_by', 'created_on', 'modified_on']


class PageArticleAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_by', 'created_on', 'modified_on']


class PagePhotoAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_by', 'created_on', 'modified_on']


class PageFormAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_by', 'created_on', 'modified_on']


class PageFormElementAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_by', 'created_on', 'modified_on']


class PageFileAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_by', 'created_on', 'modified_on']


admin.site.register(Page, PageAdmin)
admin.site.register(Row, RowAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(PageArticle, PageArticleAdmin)
admin.site.register(PagePhoto, PagePhotoAdmin)
admin.site.register(PageForm, PageFormAdmin)
admin.site.register(PageFormElement, PageFormElementAdmin)
admin.site.register(PageFile, PageFileAdmin)
