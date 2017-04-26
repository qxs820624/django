import logging
logger = logging.getLogger('project')

from django.shortcuts import render
from django.contrib.auth.models import AnonymousUser

from django.views import generic
from .models import Product, Review
from django.http import JsonResponse
from django.db.models import Count, Min, Max, Sum,Avg
import json

from clusterdbm.views import get_user_group

def product_list(request):
    """product catagroy and search"""
    #url = request.path
    # method = request.method
    group = get_user_group(request)
    if request.method =='POST':
        query_str = request.POST.get('query_product',None)
        if query_str:
            products_list = Product.objects.filter(name__icontains = query_str)
            if not products_list:
                result = {'result':-1}
            else:
                products_list = products_list[0].name
                result={'result':products_list}
            #return render(request,'products/product_list.html',{ 'result':result})
            return JsonResponse(result,safe=False)
        #the query string in blank
        else:
            return render(request,'products/product_list.html',{'error':'you must enter something to forward',})
        return render(request,'products/product_list.html',
                      {'products_list':products_list,
                       'group':group,
                       })
    else:
        query_product = Product.objects.all()
        logger.info('find products {} '.format(list(query_product)))
        return render(request,'products/product_list.html',{
            'product_list':query_product,
            'group':group,
        })

def product_detail(request, product="redis"):
    if str.lower(product) == 'redis':
        return redis_detail(request)
    elif str.lower(product) == 'postgresql':
        return postgresql_detail(request)
    else:
        return redis_detail(request)

def redis_detail(request):
    """redis detail"""
    #redis = Product.objects.get(name='Redis')
    #if redis:
        #redis_des = redis.description
    #return render(request,'products/redis_detail.html',{'redis_detail':redis_des})
    reviews = Review.objects.filter(product_id=Product.objects.get(name='Redis'))
    id_counts = Review.objects.filter(product_id=Product.objects.get(name='Redis')).aggregate(Count("id"))
    rating_avg = Review.objects.filter(product_id=Product.objects.get(name='Redis')).aggregate(Avg("rating"))
    
    productsName = Product.objects.values("name").distinct()
    productsNames = []
    id_counts = {}
    rating_avgs = {}
    reviews = {}
    for name in productsName:
        productsNames.append(name['name'])
        review = Review.objects.filter(product_id=Product.objects.get(name=name['name']))
        id_count = review.aggregate(Count("id"))
        rating_avg = review.aggregate(Avg("rating"))
        id_counts[name['name']] = id_count['id__count']
        rating_avgs[name['name']] = rating_avg['rating__avg']
        reviews[name['name']] = review
    
    return render(request,'products/redis_detail.html',{'reviews': reviews,
                        'count_of_redis': id_count, 'avg_rating': rating_avgs,
                        'productsNames': productsNames,})

def postgresql_detail(request):
    """postgresql detail"""
    try:
        postgresql = Product.objects.filter(name = 'PostgreSQL')
        a = 1
    except:
        pass
    return render(request, 'products/product_detail.html',{})

class ProductDetail(generic.TemplateView):
    template_name = 'products/product_detail.html'

    def get(self,request,*args,**kwargs):
        product_arg = args[0]
        try:
            product = Product.objects.filter(name=product_arg)[0]
            kwargs['product'] = product
        except:
            return render(request,'404.html',{})
        group = get_user_group(request)
        kwargs['group'] = group
        return super(ProductDetail,self).get(request,*args,**kwargs)
