from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseNotFound
from django.http.response import HttpResponseNotAllowed, Http404

from myApp.query import Query

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
        cursor.close()
        # with connection.cursor() as cursor:


    except Exception as e:
        print(e)
    return render(request, "myApp/index.html", result)

def searchPage(request):
    if request.method == 'GET':
        return render(request, "myApp/search.html")
    elif request.method == 'POST':
        queryType = int(request.POST['type'])
        result = dict()
        if queryType == 1:
            result["column"] = ('countryName','averageScore')
            result["datas"] = Query.queryType1()

        elif queryType == 2:
            result["column"] = ('cityName','averageScore')
            result["datas"] = Query.queryType2()

        elif queryType == 3:
            result["column"] = ('professorName','studentName')
            result["datas"] = Query.queryType3()

        elif queryType == 4:
            result["column"] = ('professorName','studentName')
            result["datas"] = Query.queryType4()

        elif queryType == 5:
            result["column"] = ('studentName','cityName')
            result["datas"] = Query.queryType5()
        return render(request, "myApp/search.html", result)
    else :
        return HttpResponseNotFound("")

def students(request, message = ""):
    result = dict()
    try:
        with connection.cursor() as cursor:
            sqlQuery = "Select * from students;"
            cursor.execute(sqlQuery)
            row = cursor.fetchall()

            result["type"] = "Students"
            result["column"] = ('studentID','name','score','country')
            result["datas"] = row
            result["result"] = message

    except Exception as e:
        print(e)

    return render(request, "myApp/import.html", result)

def professors(request, message = ""):
    result = dict()
    try:
        with connection.cursor() as cursor:
            sqlQuery = "Select * from professors;"
            cursor.execute(sqlQuery)
            row = cursor.fetchall()

            result["type"] = "Professors"
            result["column"] = ('facultyID','name','age','country')
            result["datas"] = row
            result["result"] = message

    except Exception as e:
        print(e)

    return render(request, "myApp/import.html", result)

def countries(request, message = ""):
    result = dict()
    try:
        with connection.cursor() as cursor:
            sqlQuery = "Select * from countries;"
            cursor.execute(sqlQuery)
            row = cursor.fetchall()

            result["type"] = "Countries"
            result["column"] = ('countryName','population','city')
            result["datas"] = row
            result["result"] = message

    except Exception as e:
        print(e)

    return render(request, "myApp/import.html", result)

def covid(request, message = ""):
    result = dict()
    try:
        with connection.cursor() as cursor:
            sqlQuery = "Select * from covid;"
            cursor.execute(sqlQuery)
            row = cursor.fetchall()

            result["type"] = "Covid"
            result["column"] = ('patientID','city')
            result["datas"] = row
            result["result"] = message

    except Exception as e:
        print(e)

    return render(request, "myApp/import.html", result)

def csvImport(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed("Not Allowed")
    try:
        a = request.FILES['csv'].read()
        b = a.decode('utf-8')

        datas = ""
        for row in b.splitlines():
            data = "("
            for r in row.split(','):
                data += "'{}',".format(r)
            data = data[:-1] + "),"
            datas += data
        with connection.cursor() as cursor:
            sqlQuery = "Insert INTO {} values {};".format(request.POST['type'], datas[:-1])
            cursor.execute(sqlQuery)
            row = cursor.fetchall()
            connection.commit()
        result = "Success!"
    except Exception as e:
        result = "Error : " + str(e)

    if request.POST['type'] == 'Students':
        return students(request,result)
    elif request.POST['type'] == 'Professors':
        return professors(request,result)
    elif request.POST['type'] == 'Countries':
        return countries(request,result)
    elif request.POST['type'] == 'Covid':
        return covid(request,result)

    return HttpResponseNotFound("")


