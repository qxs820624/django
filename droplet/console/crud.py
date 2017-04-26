from crudbuilder.abstract import BaseCrudBuilder
from packages.models import Package

class PersonCrud(BaseCrudBuilder):
    model = Package
    search_fields = ['name']
    tables2_fields = ('name', 'status')
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 5  # default is 10
    modelform_excludes = ['created_by', 'updated_by']
    login_required=True
    permission_required=True
