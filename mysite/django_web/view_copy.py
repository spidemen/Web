# Create your views here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from mysite import models
from django.shortcuts import render
from django_web.models import user,blog
from django.db import connection,transaction


def dictfetchall(cursor):
    "将游标返回的结果保存到一个字典对象中"
    desc = cursor.description
    return [
    dict(zip([col[0] for col in desc], row))
    for row in cursor.fetchall()
    ]

#insert function
def insert(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        #dept= request.POST.get("dept", None)
        #People = user.objects.get(username=username, password=password,dept=dept)
        sql='select * from user where username='+'\''+username+'\''+'and password='+'\''+password+'\''#+' and dept='+'\''+dept+'\''
        print (sql)
        cursor = connection.cursor()
        #cursor.execute('select * from user where username=%s and password=%s',[username,password])
        cursor.execute(sql)
        People =dictfetchall(cursor)
        # print (People)
        #People = user.objects.raw(sql)
        #People.save()
        #People = user.objects.get(username=’bill‘)
        if People == []:
            error_msg="Error!"
            return render(request, 'insert.html',{"error_msg":error_msg})
        else:
            return render(request,'insert.html',{"People":People})
    if request.method == "POST" :
        content = request.POST.get("content", None)
        tw = blog.objects.create(content=content)
        tw.save()
        return render(request,'insert.html',{"tw":tw})
    return render(request,'insert.html')

def signup(request):
    if request.method=='POST':
        username1 = request.POST.get("username", None)
        password1 = request.POST.get("password", None)
        dept1 = request.POST.get("dept", None)
        if username1 and password1 and dept1:
          #  test1=user.objects.get(username=username1,password=password1,dept=dept1)
            test1=user.objects.create(username=username1,password=password1,dept=dept1)
            test1.save()
            return render(request,'insert.html')
        else:
            error_msg='Wrong input! Please re-enter your information.'
            return render(request,'signup.html',{'error_msg':error_msg})
    return render(request,'signup.html')


#define display function
def list(request):
    #cursor = connection.cursor()
    #cursor.execute('select * from user')
    #people_list = dictfetchall(cursor)
    #print people_list
    #people_list = user.objects.all()
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
       	
    people_list = user.objects.all()
    return render(request, 'show.html', {"people_list":people_list})
