import datetime
import logging

from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from .models import Package, Plan
from applications.models import Product
from .forms import OrderForm
logger = logging.getLogger('sql_compute')
from clusterdbm.views import get_user_group

class Service(LoginRequiredMixin,generic.TemplateView):
    """user service"""
    template_name = 'packages/service.html'

    def get(self,request,*args,**kwargs):
        user = request.user
        try:
            query_service = Package.objects.filter(user_id=user)
            kwargs['service'] = query_service
        except:
            kwargs['service'] = None
        return super(Service,self).get(request,*args,**kwargs)


class MakeOrder(LoginRequiredMixin,generic.TemplateView):
    """the view of order """
    template_name = 'packages/orderform.html'
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        kwargs['group'] = get_user_group(request)
        product = self.request.GET.get('p',None)
        if not product:
            messages.error(request, "The product required. "
                           "Please choice a product to order.",extra_tags='danger')
            kwargs["order_form"] = OrderForm()
            return super(MakeOrder,self).get(request,*args,**kwargs)
        if "order_form" not in kwargs:
            kwargs["order_form"] = OrderForm()
            kwargs['p'] = product
        return super(MakeOrder,self).get(request,*args,**kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        kwargs['group'] = get_user_group(request)
        product = self.request.GET.get('p',None)
        print(product)
        # product not exists return
        if not product:
            messages.error(request, "The product required. "
                           "Please choice a product to order.",extra_tags='danger')
            kwargs["order_form"] = OrderForm()
            return super(MakeOrder,self).get(request,*args,**kwargs)
        #valid form data
        order_form = OrderForm(request.POST)
        if not order_form.is_valid():
            order_form = OrderForm(request.POST)
            return super(MakeOrder, self).get(request,
                                                order_form=order_form,p=Product)
        #save form data to database
        memory = request.POST.get('memory', None)
        #print(request.POST)
        plan_id = request.POST.get('plan_id', None)
        plan = Plan.objects.get(id=plan_id)
        product_obj = Product.objects.get(name=product)
        name = user.name + '_' + product + '_' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            Package(user_id=user, product_id=product_obj,plan_id=plan,name=name,memory=memory).save()
            messages.success(request, "The order is setup succussfully!")
        except:
            logger.info('{} order the {} failed!'.format(user.name,product))
            messages.error(request, "The order failed please contact the support team!",extra_tags='danger')
        return redirect("order:service")