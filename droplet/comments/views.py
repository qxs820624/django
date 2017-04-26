from django.shortcuts import render

from http import *
from django.http import HttpResponseRedirect 
from django.template import *
from django.conf import *
from django.forms import * 
from django.shortcuts import * 
from applications.models import Product, Review
from datetime import datetime
from django.utils.timezone import utc
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='next', login_url='/login/')
def SaveComments(request, name):
        if request.POST:
                nowstr = now()
                print(request.POST)
                rating=request.POST["rating"]
                reviews=request.POST["comment"]
                if len(rating) ==  0 :
                        rating = 5
                #productName = Product.objects.values("name").distinct()
                #for name in productName:
                Review(product_id= Product.objects.get(name=name),
                        rating=int(rating), reviews=reviews, status= "active",
                        created_date=nowstr, created_by=request.user.name,
                        updated_date = nowstr,
                        updated_by = request.user.name).save()
                return HttpResponseRedirect(request.POST['next'])
        else:
                return HttpResponseRedirect("/")

def now():
        """
        Returns an aware or naive datetime.datetime, depending on settings.USE_TZ.
        """
        if settings.USE_TZ:
                # timeit shows that datetime.now(tz=utc) is 24% slower
                return datetime.utcnow().replace(tzinfo=utc)
        else:
                return datetime.now()
