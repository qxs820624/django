from django.contrib.auth import get_user_model
User = get_user_model()

from packages.models import Package,Server
from applications.models import Review
from helpdesk.models import Ticket


def get_order_information(user,group):
    """get client order information"""
    status = ['Active','Inactive','Pending']
    if group:
        if group.name == "Paid":
            return get_client_order_information(user)
        if group.name == "Staff":
            return get_staff_order_information(user)
    return (order_dict,server_dict,ticket_dict,reviews)

order_dict = {}
server_dict = {}
ticket_dict = {}
status = ['Active','Inactive','Pending']

def get_client_order_information(user):
    """get client information"""
    #order
    order_set = Package.objects.filter(user_id = user)
    if order_set:
        for s in status:
            order_dict.setdefault(s,len(order_set.filter(status=s)))
    #server
    server_set = Server.objects.filter(package_id__in = order_set) if order_set else None
    if server_set:
        for s in status:
            server_dict.setdefault(s,len(order_set.filter(status=s)))
    #ticket
    ticket_set = Ticket.objects.filter(submitter_email=user.email)
    ticket_dict.setdefault('opening',len(ticket_set.filter(status=1)))
    ticket_dict.setdefault('closed',len(ticket_set.filter(status=4)))
    #reviews
    reviews = len(Review.objects.filter(created_by=user.name))
    print(order_dict,server_dict,ticket_dict,reviews)
    return (order_dict,server_dict,ticket_dict,reviews)


def get_staff_order_information(user):
    """get client information"""
    status = ['Pending','Active','Suspended','Fraud','Canceled']
    #order
    order_set = Package.objects.all()
    if order_set:
        for s in status:
            order_dict.setdefault(s,len(order_set.filter(status=s)))
    # #server
    # server_set = Server.objects.filter(package_id__in = order_set) if order_set else None
    # if server_set:
    #     for s in status:
    #         server_dict.setdefault(s,len(order_set.filter(status=s)))
    user_set = User.objects.filter(groups__name__in = ('Paid','Registered','vip'))
    user_dict = {}
    for s in status:
        user_dict.setdefault(s,0)
    user_dict['Active'] = len(user_set.filter(is_active=True))
    #ticket
    ticket_role = ['Support','Billing','Sale']
    ticket_set = Ticket.objects.all()
    for role in ticket_role:
        ticket_dict.setdefault(role,len(ticket_set.filter(queue__title=role)))
    #reviews
    review_dict = {}
    review_set = Review.objects.all()
    if review_set:
        review_dict['Pending'] = len(review_set.filter(status = 'Pending'))
        review_dict['Active'] = len(review_set.filter(status = 'Active'))
    print(order_dict,user_dict,ticket_dict,review_dict)
    return (order_dict,user_dict,ticket_dict,review_dict)
