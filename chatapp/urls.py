from django.conf.urls import url
from chatapp import views
urlpatterns=[
    url(r'^user/create$', views.getdata)
]