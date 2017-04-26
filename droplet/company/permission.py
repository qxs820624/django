#coding=utf-8
from django.shortcuts import render
from company import models
from django.db.models import Q
from django.core.urlresolvers import resolve   

def perm_check(request, *args, **kwargs):
    url_obj = resolve(request.path_info)
    url_name = url_obj.url_name
    perm_name = ''
    
    if url_name:
        
        url_method, url_args = request.method, request.GET
        url_args_list = []
        
        for i in url_args:
            url_args_list.append(str(url_args[i]))
        url_args_list = ','.join(url_args_list)
        
        get_perm = models.Permission.objects.filter(Q(url=url_name) and 
            Q(per_method=url_method) and Q(argument_list=url_args_list))
        if get_perm:
            for i in get_perm:
                perm_name = i.name
                # print(i)
                # print(perm_name)
                perm_str = 'company.%s' % perm_name
                print(perm_str, request.user)
                if request.user.has_perm(perm_str):
                    print('====>> perm matched')
                    return True
                else:
                    print('---->perm not match')
                    return False
        else:
            print("get_perm is null")
            return False
    else:
        return False   #


def check_permission(fun):    #
    def wapper(request, *args, **kwargs):
        if perm_check(request, *args, **kwargs):  #
            return fun(request, *args, **kwargs)
        return render(request, '403.html', locals())
    return wapper
