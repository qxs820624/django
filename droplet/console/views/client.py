from django.shortcuts import  render_to_response,render
from django.contrib.auth.decorators import login_required

#self define module
from ..utils import get_order_information
from clusterdbm.views import get_user_group


@login_required
def ClientConsole(request):
    """client console"""
    group = get_user_group(request)
    user = request.user
    orders,servers,tickets,reviews = get_order_information(user,group)
    return render(request,'panel/console.html',
                  {'group':group,
                   'orders':orders,
                   'servers':servers,
                   'tickets':tickets,
                   'reviews':reviews,
                   })