from crudbuilder.abstract import BaseCrudBuilder
from .models import Package
from django import forms
from clusterdbm.views import get_user_group

class PackageUpdateForm(forms.ModelForm):
        class Meta:
                model = Package
                exclude =  ['created_by', 'updated_by']

        def __init__(self, *args, **kwargs):
                self.request = kwargs.pop('request', None)
                super(PersonEmployementUpdateForm, self).__init__(*args, **kwargs)

class PersonEmployementCreateForm(forms.ModelForm):
        class Meta:
                model = Package
                exclude = ['created_by', 'updated_by']

        def __init__(self, *args, **kwargs):
                self.request = kwargs.pop('request', None)
                super(PersonEmployementCreateForm, self).__init__(*args, **kwargs)

class PackageCrud(BaseCrudBuilder):
    model = Package
    search_fields = ['name','status']
    tables2_fields = ('name', 'status')
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 5  # default is 10
    modelform_excludes = ['created_by', 'updated_by']
    login_required=True
    permission_required=True
    # createupdate_forms = {
    #             'create': PersonEmployementCreateForm,
    #             'update': PersonEmployementUpdateForm
    #     }
    permissions={
        "list":"wigets.list_client",
    }

    @classmethod
    def custom_queryset(cls, request, **kwargs):
        """Define your own custom queryset for list view"""
        user = request.user
        # p = user.get_all_permissions()
        # for pi in p:
        #     print(pi)
        group = get_user_group(request)
        if group.name=="Staff" or request.user.is_superuser:
            qset = cls.model.objects.all()
            return qset
        else:
            qset = cls.model.objects.filter(user_id = request.user)
            return qset
