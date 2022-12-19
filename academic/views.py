# from django.shortcuts import render
# import json
# import requests
# import time
# from datetime import date

# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login
#
# from django.contrib.auth.decorators import login_required
# from django.core.files.storage import FileSystemStorage
# from django.http import HttpResponseRedirect, HttpResponse
# from django.template import RequestContext, loader

# from main.database_functions.database_utility import __db_fetch_values_dict, __db_fetch_values, __db_fetch_single_value, \
#     __db_commit_query, __db_insert_query, row_query

# import pandas
# from django.db import connection
# import json


# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
# from rest_framework.response import Response
# from rest_framework import status
# from django.forms.models import model_to_dict

from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from academic.models import Students
from django.shortcuts import render, redirect
from django.http import (
    HttpResponseRedirect, HttpResponse)


# @csrf_exempt
# @login_required
def student_data_add(request):
    if request.method == 'POST':
        student_add = Students()
        student_add.name = request.POST.get('name')
        student_add.st_class = request.POST.get('st_class')
        student_add.section = request.POST.get('section')
        student_add.roll = request.POST.get('roll')
        student_add.age = request.POST.get('age')
        student_add.save()

        messages.success(request, '<i class="fa fa-check-circle"></i> নতুন Content সফলভাবে সংযুক্ত হয়েছে !',
                         extra_tags='alert-success crop-both-side')

        return HttpResponseRedirect('/academic/student-data/list/')

    return render(request, 'student_data_add.html', {})


def student_list(request):
    students = Students.objects.all()
    return render(request, 'student_list.html', {
        'student_list': students
    })


def student_data_edit(request, student_id):
    student_data = Students.objects.filter(id=student_id).last()
    if request.method == 'POST':
        student_data.name = request.POST.get('name')
        student_data.st_class = request.POST.get('st_class')
        student_data.section = request.POST.get('section')
        student_data.roll = request.POST.get('roll')
        student_data.age = request.POST.get('age')
        student_data.save()

        messages.success(request, '<i class="fa fa-check-circle"></i> নতুন Content সফলভাবে সংযুক্ত হয়েছে !',
                         extra_tags='alert-success crop-both-side')

        return HttpResponseRedirect('/academic/student-data/list/')

    return render(request, 'student_data_edit.html', {
        'student_data': student_data
    })
def student_data_delet(request, student_id):
    student_data = Students.objects.filter(id=student_id).last()
    if request.method == 'POST':
        student_data.name = request.POST.get('name')
        student_data.st_class = request.POST.get('st_class')
        student_data.section = request.POST.get('section')
        student_data.roll = request.POST.get('roll')
        student_data.age = request.POST.get('age')
        student_data.save()

        messages.success(request, '<i class="fa fa-check-circle"></i> নতুন Content সফলভাবে সংযুক্ত হয়েছে !',
                         extra_tags='alert-success crop-both-side')

        return HttpResponseRedirect('/academic/student-data/list/')

    return render(request, 'student_data_delet.html', {
        'student_data': student_data
    })

