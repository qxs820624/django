from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group,Permission
User = get_user_model()

from crudbuilder.abstract import BaseCrudBuilder
from crudbuilder.formset import BaseInlineFormset
from clusterdbm.views import get_user_group


class UserCrud(BaseCrudBuilder):
    """user crud"""
    model = User
    search_fields = ['name',]
    tables2_fields = ('name','email','is_active','date_joined',)
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 5
    modelform_excludes = ['created_by', 'updated_by']
    login_required=True
    permission_required=True

    permissions = {
        'list':'wigets.list_client',
        'create': 'wigets.creat_client',
        'detail': 'wigets.detail_client',
        'update': 'wigets.update_client',
        'delete': 'wigets.delete_client',
    }