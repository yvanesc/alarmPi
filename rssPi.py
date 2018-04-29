import feedparser


def newsUpdate(numN):
    d=feedparser.parse("http://feeds.reuters.com/Reuters/worldNews/.rss")
    dta = d["entries"][numN]["title"]
    if len(dta) > 27:
        dta = dta[:27] + ".."
    return (dta)