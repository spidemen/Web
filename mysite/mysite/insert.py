# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf

def insert(request):
	ctx={}
	if request.POST:
		ctx['rlt']=request.POST['q']
	else:
		message='You are not in the database or WRONG INFO'
	return render(request,"insert.html",ctx)
