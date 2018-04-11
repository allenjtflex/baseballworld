from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from .views import ScheduleList, ScheduleDetail

urlpatterns = [

    url(r'^$', ScheduleList.as_view( template_name ='schedules/schedule_list.html') , name="schedule_list" ),
    url(r'^(?P<pk>\d+)/$', ScheduleDetail.as_view(), name="schedule_detail"  ),
    # url(r'^(?P<pk>\d+)/$', ScheduleDetail.as_view( template_name ='schedules/schedule_detail.html'), name="schedule_detail"  ),
    # url(r'^create/$', CustomerCreate.as_view( template_name = 'customers/customer_form.html' ), name="customer_create" ),
    # url(r'^(?P<pk>\d+)/edit/$', CustomerUpdate.as_view( template_name = 'customers/customer_form.html' ), name="customer_edit" ),

]
