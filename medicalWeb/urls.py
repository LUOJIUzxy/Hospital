"""medicalWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, re_path
#from django.conf.urls import url
from django.contrib import admin
from myweb.views import doctor_list
from myweb.views import doctor_detail,reservation,home,fastlogin,normallogin,yanzheng,register,text,login,loginsend,person,search,loginsend2
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^home/$',home,name = 'home'),
    re_path(r'$^',home,name="home"),
    re_path(r'^department/(?P<department_id>[^/]+)/$',doctor_list,name='department'),
    re_path(r'^doctors/(?P<doctor_id>[^/]+)/$',doctor_detail,name='doctor'),
    re_path(r'^reservation/$',reservation,name='reservation'),
    re_path(r'^personal/$',person,name='personal'),
    re_path(r'^search/$',search,name='se'),
    re_path(r'^text/$',text,name='te'),
    re_path(r'^register/$',register,name = 'register'),
    re_path(r'^yanzheng/$', yanzheng, name='yz'),
    re_path(r'^log/$',login,name='login'),
    re_path(r'^login_send/$', loginsend2 ,name = 'loginsend'),
    re_path(r'^loginsend2/$', loginsend2 ,name = 'loginsend'),
    re_path(r'^fastlogin/$', fastlogin ,name = 'fastlogin'),
    re_path(r'^normallogin/$',normallogin, name='normallogin'),
]
