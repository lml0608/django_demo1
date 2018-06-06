# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''
from django.shortcuts import render,redirect,HttpResponse

from app01.models import Classes,Teachers



def get_classes(request):


    cls_list = Classes.objects.all()


    for item in cls_list:
        print(item.id,item.title,item.m.all())

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


def edit_classes(request):

    if request.method == "GET":
        nid = request.GET.get('nid')

        obj = Classes.objects.filter(id=nid).first()

        return render(request,"edit_classes.html",{"obj":obj})


    elif request.method == "POST":

        nid = request.GET.get('nid')
        title = request.POST.get('xxoo')

        Classes.objects.filter(id=nid).update(title=title)

        return redirect('/classes.html')




def set_teacher(request):

    if request.method == 'GET':
        nid = request.GET.get('nid')
        cls_obj = Classes.objects.filter(id=nid).first()
        cls_teacher_list = cls_obj.m.all().values_list('id','name')
        # [Teacher obj,obj,obj,]
        # [(1,'hf'),(2,"Al"),(3,'uh')]
        # ==> [1,2,3]
        # 当前班级任课教师的id列表
        id_list = list(zip(*cls_teacher_list))[0] if list(zip(*cls_teacher_list)) else []
        all_teacher_list = Teachers.objects.all()
        return render(request,
                      'set_teacher.html',
                      {
                          'id_list': id_list,
                          'all_teacher_list': all_teacher_list,
                          'nid':nid
                       }
                      )
    elif request.method == "POST":
        nid = request.GET.get('nid')
        ids = request.POST.getlist('teacher_ids')
        print('当前班级的ID', nid, '分配的老师ID', ids)

        obj = Classes.objects.filter(id=nid).first()
        obj.m.set(ids)
        return redirect('/classes.html')
