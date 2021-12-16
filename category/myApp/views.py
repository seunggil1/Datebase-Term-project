from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
from django.http.response import HttpResponseNotAllowed, Http404
import csv

def index(request):
    result = dict()
    try:
        # cursor = connection.cursor()
        # connection.commit()
        # connection.close()
        cursor = connection.cursor()
        sqlQuery = "Select * from students;"
        cursor.execute(sqlQuery)
        row = cursor.fetchall()
        result["students"] = row

        # with connection.cursor() as cursor:


    except Exception as e:
        print(e)
    return render(request, "myApp/index.html", result)

def csvImportPage(request):
    return render(request, "myApp/import.html")

def students(request):
    result = dict()
    try:
        with connection.cursor() as cursor:
            sqlQuery = "Select * from students;"
            cursor.execute(sqlQuery)
            row = cursor.fetchall()

            result["type"] = "Student"
            result["column"] = ('studentID','name','score','country')
            result["datas"] = row

    except Exception as e:
        print(e)

    return render(request, "myApp/import.html", result)

def professors(request):
    result = dict()
    try:
        with connection.cursor() as cursor:
            sqlQuery = "Select * from professors;"
            cursor.execute(sqlQuery)
            row = cursor.fetchall()

            result["type"] = "Professor"
            result["column"] = ('facultyID','name','age','country')
            result["datas"] = row

    except Exception as e:
        print(e)

    return render(request, "myApp/import.html", result)

def countries(request):
    result = dict()
    try:
        with connection.cursor() as cursor:
            sqlQuery = "Select * from countries;"
            cursor.execute(sqlQuery)
            row = cursor.fetchall()

            result["type"] = "Country"
            result["column"] = ('countryName','population','city')
            result["datas"] = row

    except Exception as e:
        print(e)

    return render(request, "myApp/import.html", result)

def covid(request):
    result = dict()
    try:
        with connection.cursor() as cursor:
            sqlQuery = "Select * from covid;"
            cursor.execute(sqlQuery)
            row = cursor.fetchall()

            result["type"] = "Covid"
            result["column"] = ('patientID','city')
            result["datas"] = row

    except Exception as e:
        print(e)

    return render(request, "myApp/import.html", result)

def csvImport(request):
    if request.method == 'GET':
        return HttpResponseNotAllowed("Not Allowed")
    a = request.FILES['csv'].read()
    b = a.decode('utf-8')

    for row in b.split():
        for r in row.split(','):
            print(r, end=' ')
        print()
    if request.POST['type'] == 'Student':
        return students(request)
    elif request.POST['type'] == 'Professor':
        return professors(request)
    elif request.POST['type'] == 'Country':
        return countries(request)
    elif request.POST['type'] == 'Covid':
        return covid(request)
    return Http404("Internal Error")