from django.contrib import admin
from .models import (Member,Team, TeamMember,Cup, CupGroup,BatResult,Schedule, Game,BatterOrder,League, Place)
# Register your models here.




admin.site.register(League)



admin.site.register(Place)
admin.site.register(Member)


class TeamMemberInline(admin.TabularInline):
    model = TeamMember



class TeamAdmin(admin.ModelAdmin):
    list_display = ( 'team_title', 'is_active' )
    list_display_links = (  'team_title', )
    list_per_page = 10
    inlines = [
           TeamMemberInline,
      ]


    #search_fields = ['t
    #search_fields = ['title']
admin.site.register(Team,TeamAdmin)


class CupGroupAdmin(admin.ModelAdmin):
    list_display = ( 'cup', 'group','team' )
    list_display_links = (  'cup','team', )
    list_per_page = 10
    ordering = ['group']
    #search_fields = ['title']

# admin.site.register(CupGroup,CupGroupAdmin)


class CupGroupInline(admin.TabularInline):
    model = CupGroup



class CupAdmin(admin.ModelAdmin):
    list_display = ('league', 'cup_title'  )
    list_display_links = (  'league', 'cup_title', )
    inlines = [
           CupGroupInline,
       ]

admin.site.register(Cup,CupAdmin)



class BatResultAdmin(admin.ModelAdmin):
    list_display = ( 'catcode', 'description','batseats','batcount' )
    list_display_links = (  'catcode','description', )
    list_per_page = 10
    #search_fields = ['tit
admin.site.register(BatResult,BatResultAdmin)







class GameInline(admin.TabularInline):
    model = Game

# class GameAdmin(admin.ModelAdmin):
#     inlines = [
#            BatterOrderInline,
#        ]
# admin.site.register(Game,GameAdmin)
#
class BatterOrderInline(admin.TabularInline):
    model = BatterOrder


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ( 'dif_date', 'cup','guest_score','guest' ,'home', 'home_score','playdate')
    list_display_links = (  'cup','playdate', )
    list_per_page = 10
    fieldsets = (
          ('Game info', { 'fields': ['cup','dif_date', 'playdate','guest', 'home'], }),
          ('Score info', { 'fields': ['guest_score', 'home_score'], }),
      )
    inlines = [
           # GameInline,
           BatterOrderInline,
       ]


admin.site.register(Schedule,ScheduleAdmin)
