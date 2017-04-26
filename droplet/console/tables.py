import django_tables2 as tables
from packages.models import Package

class PackageTable(tables.Table):
    class Meta:
        model = Package
        attrs = {'class': 'table table-bordered'}
        fields = ('id', 'user_id.name','created_date','status','plan_id.name','plan_id.price')
