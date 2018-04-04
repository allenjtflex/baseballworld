from django.db import models

# Create your models here.
# #守備位置
# class PlayPosition(models.Model):
#     position = models.CharField(primary_key =True,max_length=2 )
#     description = models.CharField(max_length=30, null=False, blank=False)

class League(models.Model):
    title = models.CharField(max_length=30,null=False, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

#打擊結果選項
class BatResult(models.Model):
    catcode = models.CharField(primary_key =True,max_length=2 )
    description = models.CharField(max_length=30, null=False, blank=False)
    batseats = models.IntegerField(default = 1)#打席數
    batcount = models.IntegerField(default = 1)#打數

    def __str__(self):
        return '%s - %s' %(self.catcode, self.description)


#球員
class Member(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

#球隊
class Team(models.Model):
    team_title = models.CharField(max_length=30, null=False, blank=False)
    is_active = models.BooleanField(default=True, verbose_name="會員資格")# True代表有效的
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_title

#球隊成員
class TeamMember(models.Model):
    team = models.ForeignKey( Team, on_delete=models.CASCADE )
    member = models.ForeignKey( Member, on_delete=models.CASCADE )
    is_active = models.BooleanField(default=True, verbose_name="可登錄")# True代表有效
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.member.name



#系列盃賽
class Cup(models.Model):
    cup_title = models.CharField(max_length=30, null=False, blank=False)
    league = models.ForeignKey( League,on_delete=models.CASCADE )
    is_finished = models.BooleanField(default=False, verbose_name="季賽結束")# True代表盃賽結束

    class Meta:
        ordering = []

    def __str__(self):
        return self.cup_title

#盃賽分組
class CupGroup(models.Model):
    cup = models.ForeignKey( Cup, on_delete=models.CASCADE,limit_choices_to = { 'is_finished': False  } )
    team = models.ForeignKey( Team, on_delete=models.CASCADE )
    GROUP = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    )
    group = models.CharField(
        max_length=2,
        choices=GROUP,
        default = 'A'
    )

    def __str__(self):
        return self.cup.cup_title

    class Meta:
        unique_together = ("cup", "team", "group")




#盃賽分組賽程時間
class Schedule(models.Model):
    dif_date = models.DateField()  #預定日期
    cup = models.ForeignKey( Cup, on_delete=models.CASCADE ,limit_choices_to = { 'is_finished': False  })    #盃賽
    playdate = models.DateField()#比賽日期
    guest = models.OneToOneField( Team, on_delete=models.CASCADE )    #客隊
    home =  models.OneToOneField( Team, on_delete=models.CASCADE,related_name="home" )    #主隊
    guest_score = models.IntegerField( default=0, null=False, blank=False ) #客隊分數
    home_score = models.IntegerField( default=0, null=False, blank=False )  #主隊分數
    is_finished = models.BooleanField(default=False, verbose_name="比賽完成")# True代表已經打完

    def __str__(self):
        return '%s : %s' %(self.guest , self.home)

    class Meta:
        unique_together = ("cup", "guest", "home")


#比賽
class Game(models.Model):
    schedule = models.ForeignKey( Schedule, on_delete=models.CASCADE )    #盃賽
    is_finished = models.BooleanField(default=True, verbose_name="")# True代表已經打完

#   攻守名單
class BatterOrder(models.Model):
    schedule = models.ForeignKey( Schedule, on_delete=models.CASCADE )    #盃賽
    POSITION = (
        ('1', 'P'),
        ('2', 'C'),
        ('3', '1B'),
        ('4', '2B'),
        ('5', '3B'),
        ('6', 'SS'),
        ('7', 'LF'),
        ('8', 'CF'),
        ('9', 'RF'),
        ('DH','DH'),
    )

    # game = models.ForeignKey( Game, on_delete=models.CASCADE )#比賽場次
    team = models.ForeignKey( Team, on_delete=models.CASCADE )#球隊
    player = models.ForeignKey( TeamMember, on_delete=models.CASCADE  )#球員
    position = models.CharField(
        max_length=2,
        choices=POSITION
        )
    batseat1 = models.OneToOneField( BatResult, on_delete=models.CASCADE, null=True, blank=True ,related_name="batseat1")#打席1
    batseat2 = models.OneToOneField( BatResult, on_delete=models.CASCADE, null=True, blank=True ,related_name="batseat2")#打席2
    batseat3 = models.OneToOneField( BatResult, on_delete=models.CASCADE, null=True, blank=True ,related_name="batseat3")#打席3
    batseat4 = models.OneToOneField( BatResult, on_delete=models.CASCADE, null=True, blank=True ,related_name="batseat4")#打席4
    batseat5 = models.OneToOneField( BatResult, on_delete=models.CASCADE, null=True, blank=True ,related_name="batseat5")#打席5
    # batseat6 = models.OneToOneField( BatResult, on_delete=models.CASCADE, null=True, blank=True ,related_name="batseat6")#打席6
# #
#
# # #   打擊結果
# # #class Plays(models.Model):
from django.db import models

# Create your models here.
