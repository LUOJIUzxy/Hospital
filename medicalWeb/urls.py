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
from django.conf.urls import url
from django.contrib import admin
from myweb.views import doctor_list
from myweb.views import doctor_detail,reservation,home,fastlogin,normallogin,yanzheng,register,text,login,loginsend,person,search,loginsend2
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$',home,name = 'home'),
    url(r'/$^',home,name="home"),
    url(r'^department/(?P<department_id>[^/]+)/$',doctor_list,name='department'),
    url(r'^doctors/(?P<doctor_id>[^/]+)/$',doctor_detail,name='doctor'),
    url(r'^reservation/$',reservation,name='reservation'),
    url(r'^personal/$',person,name='personal'),
    url(r'^search/$',search,name='se'),
    url(r'^text/$',text,name='te'),
    url(r'^register/$',register,name = 'register'),
    url(r'^yanzheng/$', yanzheng, name='yz'),
    url(r'^log/$',login,name='login'),
    url(r'^login_send/$', loginsend2 ,name = 'loginsend'),
    url(r'^loginsend2/$', loginsend2 ,name = 'loginsend'),
    url(r'^fastlogin/$', fastlogin ,name = 'fastlogin'),
    url(r'^normallogin/$',normallogin, name='normallogin'),
]
