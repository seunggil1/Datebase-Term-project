from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse


def index(request):
    print(1)
    try:
        # cursor = connection.cursor()
        # connection.commit()
        # connection.close()
        with connection.cursor() as cursor:
        
            sqlQuery = "Select * from students;"
            cursor.execute(sqlQuery)
            row = cursor.fetchall()
            row = cursor.fetchone()
            print(1)

    except Exception as e:
        print(e)
    return HttpResponse("Hello, world. You're at the polls index.")
