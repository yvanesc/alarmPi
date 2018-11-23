# module time calendar timePi

import time
import datetime

nowTime = datetime.datetime.now()

timePi = nowTime.strftime("%H:%M")

# month
nowMonth = datetime.datetime.now()
nowMonth = nowMonth.strftime("%m")
nbMonth = nowMonth
# day
nowDay = datetime.datetime.now()
nowDay = nowDay.strftime("%d")
nbDay = nowDay

if nbMonth == "04":
	nbMonth="Avril"
elif nbMonth == "05":
	nbMonth="Mai"
elif nbMonth == "06":
	nbMonth="Juin"
elif nbMonth == "07":
	nbMonth="Juil."
elif nbMonth == "08":
	nbMonth="Aout"
elif nbMonth == "09":
    nbMonth="Septembre" 
elif nbMonth == "10":
    nbMonth="Octobre"       
elif nbMonth == "11":
    nbMonth="Novembre"
elif nbMonth == "12":
    nbMonth="Decembre"
else:
    nbMonth="Nothing"

# day of the week
dayOfWeek = datetime.datetime.today().weekday()

if dayOfWeek == 0:
    dayOfWeek = "Lundi"
elif dayOfWeek == 1:
    dayOfWeek = "Mardi"
elif dayOfWeek == 2:
    dayOfWeek = "Mercredi"
elif dayOfWeek == 3:
    dayOfWeek = "Jeudi"
elif dayOfWeek == 4:
    dayOfWeek = "Vendredi"
elif dayOfWeek == 5:
    dayOfWeek = "Samedi"
elif dayOfWeek == 6:
    dayOfWeek = "Dimanche"
# year
nowYear = datetime.datetime.now()
nowYear = nowYear.strftime("%Y")
