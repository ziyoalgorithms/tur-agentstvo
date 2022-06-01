from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('users/read/', adminapp.TraveUserListView.as_view(), name='users'),
    path('user/create/', adminapp.user_create, name='user_create'),
    path('user/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('user/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),

    path('countries/read/', adminapp.countries, name='countries'),
    path('countries/create/', adminapp.CountryCreateView.as_view(), name='country_create'),
    path('countries/update/<int:pk>/', adminapp.CountryUpdateView.as_view(), name='country_update'),
    path('countries/delete/<int:pk>/', adminapp.CountryDeleteView.as_view(), name='country_delete'),

    path('accomodation/read/countries/<int:pk>/', adminapp.accomodations, name='accommodations'),
    path('accomodation/update/<int:pk>/', adminapp.accomodation_update, name='accommodation_update'),
    path('accomodation/create/countries/<int:pk>/', adminapp.accomodation_create, name='accommodation_create'),
    path('accomodation/read/<int:pk>/', adminapp.AccomodationDetailView.as_view(), name='accommodation_read'),
    path('accomodation/delete/<int:pk>/', adminapp.accomodation_delete, name='accommodation_delete'),
]

