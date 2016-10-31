from django.shortcuts import render

# Create your views here.
from school import models
from school.permission import  check_permission
from django.contrib.auth.decorators import login_required
# Create your views here.
#from django.conf import settings
#from django.shortcuts import redirect

@login_required(redirect_field_name='next', login_url='/admin/login/')
@check_permission
def students(request):
    students_obj = models.Student.objects.all()
    return render(request, 'students_list.html', locals())
