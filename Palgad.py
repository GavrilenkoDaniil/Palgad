from modul import *

while True:
	a=input("lisa-1, kustuta-2, suurim palk-3, vaiksem palk-4, otsing-5: ")
	if a=="1":
		ad()
	elif a=="2":
		kustuta()
	elif a=="3":
		suurimpalk()
	elif a=="4":
		vaiksempalk()
	elif a=="5":
		otsi()
	else:
		print("Sisesta number 1-5")