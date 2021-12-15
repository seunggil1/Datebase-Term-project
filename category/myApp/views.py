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
