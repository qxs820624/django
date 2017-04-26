from django.http import HttpResponse
from django.shortcuts import  render_to_response,render
from django.contrib.auth.decorators import login_required

#self define module
from clusterdbm.views import get_user_group
from packages.models import Package
from ..tables import PackageTable

@login_required
def StaffConsole(request):
    """staff console"""
    group = get_user_group(request)
    user = request.user
    return render(request,'panel/console.html',{'group':group})


@login_required
def staff_order(request):
    """manage orders"""
    STATUS  = {
        'All':'',
        'Pending':'',
        'Active':'',
        'Canceled':'',
        'Suspended':'',
        'Fraud':'',
    }
    group = get_user_group(request)
    if request.method == "GET":
        print(request.GET)
        p = Package.objects.all()
        q = request.GET.get('q','')
        q_s = request.GET.get("s_value",'')
        STATUS[q_s] = 'selected'
        q_s_tuple = ("Pending",'Active','Canceled','Suspended','Fraud',) if q_s == "All" else (q_s,)
        p = p.filter(user_id__name__icontains = q).filter(status__in=q_s_tuple)
        table = PackageTable(p)
        return render(request,'panel/stafforders.html',{
            'table':table,
            'group':group,
            'status':STATUS,
        })
    elif request.method == "POST":
        p = Package.objects.all()
        return render(request,'panel/stafforders.html',{
            'orders':p,
            'group':group,
            'status':STATUS,
        })

