from django.db import models
from django.contrib.auth.models import User

class Wager(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wager", null=True)
	Sport = models.CharField(max_length=200)
	Bovada_Link = models.CharField(max_length=200)
	OnexBet_Link = models.CharField(max_length=200)
	Team_OnexBet = models.CharField(max_length=200)
	Team_Bovada = models.CharField(max_length=200)
	Bet_Bovada = models.CharField(max_length=200)
	Bet_OnexBet = models.CharField(max_length=200)
	Remine_Time = models.DecimalField(max_digits=19, decimal_places=10)
	Profit_Percent = models.FloatField()
	Odd_OnexBet = models.FloatField()
	Odd_Bovada = models.FloatField()
	OnexBet_Limit = models.FloatField()
	Bovada_Limit = models.FloatField()
	OnexBet_Win = models.BooleanField()
	OpenBet = models.BooleanField()
	Money_Bet_on_OnexBet = models.FloatField()
	Money_Bet_on_Bovada = models.FloatField()
	Final_Profit = models.FloatField()
