from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('csvImport', views.csvImport, name='csvImport'),
    path('stu', views.students, name='students'),
    path('pro', views.professors, name='professors'),
    path('cou', views.countries, name='countries'),
    path('cov', views.covid, name='covid'),
    path('search', views.searchPage, name='search')
]