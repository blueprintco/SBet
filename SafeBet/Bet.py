import json
import requests
import time
from difflib import SequenceMatcher
from .models import Wager


def Calc(Odd1,Odd2):
	if (Odd1*Odd2) < (Odd1+Odd2):
		return 0;
	return (Odd2/(Odd1+Odd2))
def Calc2(Odd1,Odd2):
	return ((Odd1*Odd2)/(Odd1+Odd2))

def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()

def Bet_Finding():
	Bet_List = []
	URL_Bovada = "https://www.bovada.lv/services/sports/event/coupon/events/A/description/table-tennis?marketFilterId=def&preMatchOnly=true&lang=en"
	URL_1xBet = "https://1xbet.com/LineFeed/Get1x2_VZip?sports=10&count=5000&lng=en&tf=2200000&mode=4"

	OnexBet = json.loads(requests.get(URL_1xBet).text)
	Bovada = json.loads(requests.get(URL_Bovada).text)

	for i in OnexBet['Value']:
		for j in Bovada:
			for k in j['events']:
				try:
					if (similar(i['O1'],k['competitors'][0]['name']) > 0.70 and similar(i['O2'],k['competitors'][1]['name']) > 0.70 and i['S']*1000 == k['startTime']) :
						for l in k['displayGroups'][0]['markets']:
							for h in i['E']:
								try:
									if(l['descriptionKey'] == 'Head To Head' and h['G'] == 1):    
										if(h['T'] == 1):    
											if(Calc(float(l['outcomes'][1]['price']['decimal']),h['C']) > 0):
												B = Wager(Sport = i['SN'],
															Bovada_Link = f"https://www.bovada.lv/sports{k['link']}",
															OnexBet_Link =f"https://1xbet.com/line/{i['SN'].replace(' ','-').replace('.','')}/{i['LI']}-{i['L'].replace(' ','-').replace('.','')}/{i['CI']}-{i['O1'].replace(' ','-').replace('.','')}-{i['O2'].replace(' ','-').replace('.','')}",
															Team_OnexBet = f"{i['O1']}-{i['O2']}",
															Team_Bovada = f"{k['competitors'][0]['name']}-{k['competitors'][1]['name']}",
															Bet_Bovada = "W2",
															Bet_OnexBet = "W1",
															Remine_Time = 0-(int(time.time())-(k['startTime']/1000))/3600,
															Profit_Percent = Calc2(float(l['outcomes'][1]['price']['decimal']),h['C'])*100-100,
															Odd_OnexBet = h['C'],
															Odd_Bovada = l['outcomes'][1]['price']['decimal'],
															OnexBet_Limit = 0,
															Bovada_Limit = 0,
															OnexBet_Win = False,
															OpenBet = True,
															Money_Bet_on_OnexBet = 0,
															Money_Bet_on_Bovada = 0,
															Final_Profit = 0)
												Bet_List.append(B)
										if(h['T'] == 3):
											if(Calc(float(l['outcomes'][0]['price']['decimal']),h['C']) > 0):
												B = Wager(Sport = i['SN'],
															Bovada_Link = f"https://www.bovada.lv/sports{k['link']}",
															OnexBet_Link =f"https://1xbet.com/line/{i['SN'].replace(' ','-').replace('.','')}/{i['LI']}-{i['L'].replace(' ','-').replace('.','')}/{i['CI']}-{i['O1'].replace(' ','-').replace('.','')}-{i['O2'].replace(' ','-').replace('.','')}",
															Team_OnexBet = f"{i['O1']}-{i['O2']}",
															Team_Bovada = f"{k['competitors'][0]['name']}-{k['competitors'][1]['name']}",
															Bet_Bovada = "W1",
															Bet_OnexBet = "W2",
															Remine_Time = 0-(int(time.time())-(k['startTime']/1000))/3600,
															Profit_Percent = Calc2(float(l['outcomes'][0]['price']['decimal']),h['C'])*100-100,
															Odd_OnexBet = h['C'],
															Odd_Bovada = l['outcomes'][0]['price']['decimal'],
															OnexBet_Limit = 0,
															Bovada_Limit = 0,
															OnexBet_Win = False,
															OpenBet = True,
															Money_Bet_on_OnexBet = 0,
															Money_Bet_on_Bovada = 0,
															Final_Profit = 0)
												Bet_List.append(B)
								except:
									pass
								try:
									if(l['descriptionKey'] == 'Total Points O/U' and h['G'] == 17):
										for t in i['AE']:
											if t['G'] == 17:
												for g in t['ME']:
													if(g['P'] == float(l['outcomes'][1]['price']['handicap'])):
														if(g['T'] == 9):
															if(Calc(float(l['outcomes'][1]['price']['decimal']),g['C']) > 0):
																B = Wager(Sport = i['SN'],
																			Bovada_Link = f"https://www.bovada.lv/sports{k['link']}",
																			OnexBet_Link =f"https://1xbet.com/line/{i['SN'].replace(' ','-').replace('.','')}/{i['LI']}-{i['L'].replace(' ','-').replace('.','')}/{i['CI']}-{i['O1'].replace(' ','-').replace('.','')}-{i['O2'].replace(' ','-').replace('.','')}",
																			Team_OnexBet = f"{i['O1']}-{i['O2']}",
																			Team_Bovada = f"{k['competitors'][0]['name']}-{k['competitors'][1]['name']}",
																			Bet_Bovada = f"U{g['P']}",
																			Bet_OnexBet = f"O{g['P']}",
																			Remine_Time = 0-(int(time.time())-(k['startTime']/1000))/3600,
																			Profit_Percent = Calc2(float(l['outcomes'][1]['price']['decimal']),g['C'])*100-100,
																			Odd_OnexBet = g['C'],
																			Odd_Bovada = l['outcomes'][1]['price']['decimal'],
																			OnexBet_Limit = 0,
																			Bovada_Limit = 0,
																			OnexBet_Win = False,
																			OpenBet = True,
																			Money_Bet_on_OnexBet = 0,
																			Money_Bet_on_Bovada = 0,
																			Final_Profit = 0)
																Bet_List.append(B)
														if(g['T'] == 10): 
															if(Calc(float(l['outcomes'][0]['price']['decimal']),g['C']) > 0):
																B = Wager(Sport = i['SN'],
																			Bovada_Link = f"https://www.bovada.lv/sports{k['link']}",
																			OnexBet_Link =f"https://1xbet.com/line/{i['SN'].replace(' ','-').replace('.','')}/{i['LI']}-{i['L'].replace(' ','-').replace('.','')}/{i['CI']}-{i['O1'].replace(' ','-').replace('.','')}-{i['O2'].replace(' ','-').replace('.','')}",
																			Team_OnexBet = f"{i['O1']}-{i['O2']}",
																			Team_Bovada = f"{k['competitors'][0]['name']}-{k['competitors'][1]['name']}",
																			Bet_Bovada = f"O{g['P']}",
																			Bet_OnexBet = f"U{g['P']}",
																			Remine_Time = 0-(int(time.time())-(k['startTime']/1000))/3600,
																			Profit_Percent = Calc2(float(l['outcomes'][0]['price']['decimal']),g['C'])*100-100,
																			Odd_OnexBet = g['C'],
																			Odd_Bovada = l['outcomes'][0]['price']['decimal'],
																			OnexBet_Limit = 0,
																			Bovada_Limit = 0,
																			OnexBet_Win = False,
																			OpenBet = True,
																			Money_Bet_on_OnexBet = 0,
																			Money_Bet_on_Bovada = 0,
																			Final_Profit = 0)
																Bet_List.append(B)
								except:
									pass
				except:
					pass


	return Bet_List 