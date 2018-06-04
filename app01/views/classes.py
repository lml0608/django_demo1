# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
from django.shortcuts import render,redirect

from app01.models import Classes



def get_classes(request):


    cls_list = Classes.objects.all()




    return render(request,'get_classes.html',{"cls_list":cls_list})

def add_classes(request):


    if request.method == "GET":
        return render(request,"add_classes.html")

    elif request.method == "POST":


        title = request.POST.get('title')

        Classes.objects.create(title=title)
        return redirect('/classes.html')


def del_classes(request):

    nid = request.GET.get('nid')

    Classes.objects.filter(id=nid).delete()

    return redirect('/classes.html')




