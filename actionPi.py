
def actFormatTime(hrTr, minTr):
	if minTr < 10 and hrTr < 10:
		alarm2Display = "0" + str(hrTr) + ":" + "0" + str(minTr)
	elif minTr < 10:
		alarm2Display = str(hrTr) + ":" + "0" + str(minTr)
	elif hrTr < 10:
		alarm2Display = "0" + str(hrTr) + ":" + str(minTr)
	else:
		alarm2Display = str(hrTr) + ":" + str(minTr)

	return(alarm2Display)