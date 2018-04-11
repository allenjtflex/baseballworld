from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Schedule

# Create your views here.
class ScheduleList(ListView):
    model = Schedule
    # queryset = Schedule.objects.all()


class ScheduleDetail(DetailView):
    model = Schedule
    # template_name ='playgame/schedule_detail.html'
