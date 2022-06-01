from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.accommodations, name='index'),
    path('accomodation_details/<int:pk>/', mainapp.accomodation, name='accomodation'),
]
