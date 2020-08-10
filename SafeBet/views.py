from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from . import Bet
from .models import Wager
from django.shortcuts import redirect

def index(response):
    return redirect('/login/')

def Home(response):
    Bet_List = Bet.Bet_Finding()
    if (response.method == 'POST'):
        if response.POST.get('Confirm'):
            B=Wager(Sport = response.POST['Sport'],
					Bovada_Link = response.POST['L-Bovada'],
					OnexBet_Link =response.POST['L-OnexBet'],
					Team_OnexBet = response.POST['T-OnexBet'],
					Team_Bovada = response.POST['T-Bovada'],
					Bet_Bovada = response.POST['B-Bovada'],
					Bet_OnexBet = response.POST['B-OnexBet'],
					Remine_Time = response.POST['RemainTime'],
					Profit_Percent = response.POST['Profit'],
					Odd_OnexBet = response.POST['O-OnexBet'],
					Odd_Bovada = response.POST['O-Bovada'],
					OnexBet_Limit = response.POST['Limit-1x'],
					Bovada_Limit = response.POST['Limit-Bovada'],
					OnexBet_Win = False,
					OpenBet = True,
					Money_Bet_on_OnexBet = response.POST['Money-on-1x'],
					Money_Bet_on_Bovada = response.POST['Money-on-Bovada'],
					Final_Profit = 0)
            B.save()
            response.user.wager.add(B)
            return HttpResponseRedirect("/home/")
        if response.POST.get('Confirm2'):
            print(response.POST)
            K = Wager.objects.get(id=int(response.POST['ID']))
            K.OpenBet=False
            if response.POST['WIN'] == 'BOVADA':
                K.Final_Profit=K.Money_Bet_on_Bovada*(K.Odd_Bovada-1)-K.Money_Bet_on_OnexBet
            else:
                K.OnexBet_Win = True
                K.Final_Profit=K.Money_Bet_on_OnexBet*(K.Odd_OnexBet-1)-K.Money_Bet_on_Bovada
            K.save()
            return HttpResponseRedirect("/home/")
    return render(response, "SafeBet/Home.html", {"Bet_L":Bet_List })	
