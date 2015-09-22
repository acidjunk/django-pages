from django.contrib import admin

from .models import Tag, TaggedItem

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'created_on', 'modified_on', 'created_by')
    exclude = ('created_by',)

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(TagAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.created_by.id:
            return False
        return True

    def queryset(self, request):
        if request.user.is_superuser:
            return Tag.objects.all()
        return Tag.objects.filter(created_by=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()


class TaggedItemAdmin(admin.ModelAdmin):
    list_display = ('tag', 'created_on', 'modified_on', 'created_by')
    exclude = ('created_by',)

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(TaggedItemAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.created_by.id:
            return False
        return True

    def queryset(self, request):
        if request.user.is_superuser:
            return TaggedItem.objects.all()
        return TaggedItem.objects.filter(created_by=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()


admin.site.register(Tag, TagAdmin)
admin.site.register(TaggedItem, TaggedItemAdmin)