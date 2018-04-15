from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import login,logout


urlpatterns = [
    url(r'^setup/', views.setup),
    url(r'^bill/', views.bill),
    url(r'^products/(?P<id>[-\w]+)', views.addProduct),
    url(r'^products/', views.product),
    url(r'^register/', views.register),
    url(r'^cart/', views.bill),
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    url(r'^empty/', views.empty),
    url(r'^$', views.index),
]