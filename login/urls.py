from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/', views.login_box, name='login'),
    url(r'^logout/$', views.logout_page, name='logout'),
    url(r'^account-settings/$', views.account_settings, name="account-settings"),
]
