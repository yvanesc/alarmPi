import sqlite3

table_name='menu'

def reqMenu(chpsGet, butGet, rectGet, triGet, croixGet, upGet, downGet):
        conn = sqlite3.connect('menu.db')
        c = conn.cursor()
        #table_name='menu'
        c.execute( "SELECT "+ chpsGet +" FROM menu WHERE but LIKE '" +butGet + "' AND rect="+rectGet+" AND tri ="+triGet+" AND croix ="+croixGet+" AND up ="+upGet+" AND down ="+downGet+"".\
                format(name=chpsGet, menu=table_name))
        all_rows = c.fetchall()
        
        conn.close()
        return(all_rows[0][0])

def reqMainMenu(top):
        conn = sqlite3.connect('/home/pi/alarmPi/mainMenu.db')
        c = conn.cursor()
        #table_name='menu'
        c.execute( "SELECT "+ top +" FROM mainMenu" .\
        	format(name=top, menu='mainMenu'))
        all_rows = c.fetchall()
        
        conn.close()
        return(all_rows[0][0])
