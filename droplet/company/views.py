from django.shortcuts import render
# from itcast_subject.models import Customer
from company import models
from company.permission import check_permission
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(redirect_field_name='next', login_url='/admin/login/')

@check_permission
def roles(request):
    roles_obj = models.Role.objects.all()
    return render(request, 'role_list.html', locals())

@check_permission
def employees(request):
    employees_obj = models.Employee.objects.all()
    return render(request, 'employee_list.html', locals())
    
#def	index(request):				
	#student_list = Customer.objects.all()				
	#content	= {'customer': customer_list}				
	#return render(request, 'index.html', content)