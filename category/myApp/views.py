from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse


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
    print(1)
    return render(request, "myApp/import.html")