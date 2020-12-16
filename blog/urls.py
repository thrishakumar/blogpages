from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home-url'),
    path('createpost', views.createpost, name='createpost-url'),

]
