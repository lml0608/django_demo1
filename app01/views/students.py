# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

from django.shortcuts import render,redirect

from app01.models import Classes,Student



def get_students(request):

    stu_list = Student.objects.all()


    for stu in stu_list:

        print(stu.id,stu.age,stu.username,stu.gender,stu.cs.id,stu.cs.title)




    return render(request,'get_students.html',{"stu_list":stu_list})


def add_students(request):
    if request.method == "GET":

        cs_list = Classes.objects.all()
        return render(request,"add_students.html",{'cs_list':cs_list})

    elif request.method == "POST":

        username = request.POST.get('username')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        cs = request.POST.get('cs')


        Student.objects.create(username=username,age=age,gender=gender,cs_id=cs)
        return redirect('/students.html')


def del_students(request):
    sid = request.GET.get('sid')

    Student.objects.filter(id=sid).delete()

    return redirect('/students.html')

def edit_students(request):


    if request.method == "GET":

        sid = request.GET.get('sid')

        obj = Student.objects.filter(id=sid).first()

        cls_list = Classes.objects.values('id','title')

        # print(cls_list)

        # for row in cls_list:
        #
        #     print(row)
        #
        #     print(row['id'])

        return render(request,"edit_students.html",{"obj":obj,"cls_list":cls_list})

    elif request.method == "POST":

        sid = request.GET.get('sid')

        print(sid)

        u = request.POST.get('username')

        a = request.POST.get('age')

        g = request.POST.get('gender')

        class_id = request.POST.get('class_id')

        Student.objects.filter(id=sid).update(username=u, age=a, gender=g, cs_id=class_id)

        return redirect('/students.html')