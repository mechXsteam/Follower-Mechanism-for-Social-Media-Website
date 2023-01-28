from django.urls import path

from . import views

app_name = 'my_app'

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('profile/<int:_id>', views.profile_view, name='profile_view'),
]
