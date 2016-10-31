from django.shortcuts import render

# Create your views here.
from school import models
from school.permission import  check_permission
# Create your views here.

@check_permission
def students(request):
    students_obj = models.Student.objects.all()
    return render(request, 'students_list.html', locals())
