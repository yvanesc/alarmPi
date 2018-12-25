
def actFormatTime(hr, min):
		if alMin < 10 and alHour < 10:
			alarm2Display = "0" + str(alHour) + ":" + "0" + str(alMin)        
        elif alMin < 10:
                alarm2Display = str(alHour) + ":" + "0" + str(alMin)
        elif alHour < 10:
                alarm2Display = "0" + str(alHour) + ":" + str(alMin)
        else:
                alarm2Display = str(alHour) + ":" + str(alMin)   
        return(alarm2Display)