import datetime

from django.template import Library
from ..models import Product
from packages.models import Package

register = Library()

@register.filter('ranking')
def ranking(value):
    """lookup ranks"""
    product = Product.objects.get(name=value)
    review_list = product.review.filter(status='active')
    #compute the average of rank
    total_rank = 0
    rank = 0
    if review_list:
        for review in review_list:
            total_rank += review.rating
        rank = total_rank/len(review_list)
    return round(rank,1) if rank else 5.0


@register.filter('client')
def client(value):
    """the amount of client from the how many product package use"""
    query_package = Package.objects.filter(product_id__name=value)
    return len(query_package)


@register.filter('l_year')
def last_year(value):
    """the usage of year from first release date to now """
    timedelta = -1
    if value:
        timedelta  = datetime.date.today().year - value.year
    return timedelta

@register.filter('tanking')
def tanking(value):
    """lookup comments"""
    product = Product.objects.get(name=value)
    review_list = product.review.filter(status='Active')
    return review_list
