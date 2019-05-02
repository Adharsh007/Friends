"""demoproject URL Configuration

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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from testapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.hello_view,name='index'),
    url(r'^login/', views.log,name='login'),
    url(r'^register/', views.reg,name='register'),
    url(r'^add/', views.add,name='adddata'),
    url(r'^homepage/', views.saw,name='admin/homepage'),
    url(r'^nurse/', views.nur,name='addnurse'),
    url(r'^doctor_add/', views.doc, name='adddoctor'),
    url(r'^nursereg/', views.nursereg, name='nurseadd'),
    url(r'^doctor/', views.doct, name='doctoradd'),
    url(r'^doctorhomepage/', views.docto,name='doctorhomepage'),
    url(r'^nursehomepage/', views.nurs,name='nursehomepage'),
    url(r'^patienthomepage/', views.users,name='patienthomepage'),
    url(r'^signin/', views.signin,name='signin'),
    url(r'^signout/', views.signout, name='signout'),
    url(r'^profi/', views.pofiles, name='profi'),
    url(r'^addmedicine/', views.med, name='addmedicine'),
    url(r'^medicineadd/', views.medic, name='medicineadd'),
    url(r'^equipadd/', views.equipadd, name='equipadd'),
    url(r'^equp/', views.equp, name='equp'),
    url(r'^editp/', views.edit, name='editp'),
    url(r'^feedba(?P<id>\d+)$', views.feed, name='feedba'),
    url(r'^feedback(?P<id>\d+)$', views.feedbak, name='feedback'),
    url(r'^feedbackuser/', views.feedbackuser, name='feedbackuser'),
    url(r'^viewnurse/', views.viewnurse, name='nursedetails'),
    url(r'^viewdoctor/', views.viewdoctor, name='doctorsdetails'),
    url(r'^viewmedicine/', views.viewmedicine, name='medicinedetails'),
    url(r'^viewequip/', views.viewequip, name='viewequip'),
    url(r'^questinot/', views.questi, name='questinot'),
    url(r'^questo/', views.questo, name='questo'),
    url(r'^prodel(?P<id>\d+)$', views.prodel, name='prodel'),
    url(r'^pp(?P<id>\d+)$', views.pp, name='pp'),
    url(r'^medde(?P<id>\d+)$', views.medde, name='medde'),
    url(r'^eqdde(?P<id>\d+)$', views.eqdde, name='eqdde'),
    url(r'^questlist/', views.questlist, name='questlist'),
    url(r'^approve(?P<id>\d+)$', views.approve, name='approve'),
    url(r'^reject(?P<id>\d+)$', views.reject, name='reject'),
    url(r'^nurseprofi(?P<id>\d+)$', views.nurseprofi, name='nurseprofi'),
    url(r'^response_view/', views.response_view, name='response_view'),
    url(r'^response_send/', views.response_send, name='response_send'),
    url(r'^case/', views.case_view,name='case'),
    #url(r'^dresponse/(?P<id>\d+)/$', views.doctor_response,name='dresponse'),
    url(r'^doctresponse(?P<id>\d+)/$', views.doctor_response_view,name='doctresponse'),
    url(r'^request_appoint/', views.request_appoint,name='request_appoint'),
    url(r'^s_feedback/', views.student_feedback),
    url(r'^s_update/', views.update_student_view),




]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
