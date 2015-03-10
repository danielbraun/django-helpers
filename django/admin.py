from django.contrib import admin
from sets import Set


def model_list_display(model_class):
    return tuple(Set(model_class._meta.get_all_field_names()) - Set(["id"]))


class ReadonlyAdmin(admin.ModelAdmin):

    def __init__(self, model, admin_site):
        super(ReadonlyAdmin, self).__init__(model, admin_site)
        self.readonly_fields = [field.name for field in filter(
            lambda f: not f.auto_created, model._meta.fields)]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False
