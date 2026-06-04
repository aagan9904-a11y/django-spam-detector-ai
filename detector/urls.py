from django.urls import path

from .views import home, api_predict


urlpatterns = [

    # Website
    path('', home, name='home'),

    # API
    path('api/', api_predict),
]