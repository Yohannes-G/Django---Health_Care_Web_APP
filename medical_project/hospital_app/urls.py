from django.conf.urls import url
from hospital_app import views

app_name = 'temp'
urlpatterns = [
    #url(r'^$', views.index, name = 'index'),
    
    #url(r'^$', views.login_page, name = 'login_page'),
    url(r'^$', views.homeandh, name = 'homeandh'),
    url(r'^login_page/', views.login_page, name = 'login_page'),
    url(r'^users/', views.users, name = 'users'),
     url(r'^patient_profile/', views.patient_profile, name = 'patient_profile'),
    url(r'^sign_up_page/', views.sign_up_page, name = 'sign_up_page'),
]