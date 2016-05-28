import pickle
import feedparser
import telegram
from time import sleep

feed_list =["https://zaufanatrzeciastrona.pl/feed/",
            "http://feeds.feedburner.com/niebezpiecznik/",
            "http://feeds.feedburner.com/sekurak",
            "http://www.cyberdefence24.pl/rss/zagrozenia",
            "http://feeds.feedburner.com/CertPolska?format=xml"]

last_feeds = pickle.load(open("db.p", 'rb'))
fee_links = []

bot = telegram.Bot(token='228955506:AAGmwy8-a7b5PKjuZjiPk_7OJ0kJ6LiHBvM')

print(last_feeds)
print("-----ostatnie feedy---")

def feederek():
    for i in feed_list:
        fee = feedparser.parse(i)
        fee_title = fee.feed.title
        for x in range(5):
            fee_links.append(fee['entries'][x]['id'])
            if fee['entries'][x]['id'] in last_feeds:
                print("Nic nowego - " + fee_title)
            else:
                sleep(5)
                entry_title = fee['entries'][x]['title']
                entry_id = fee['entries'][x]['id']
                print("Aktualizacja - " + fee_title)


                message = str(fee_title +"\n" + entry_title +"\n" + entry_id)
                bot.sendMessage(chat_id="@CyberSecPL", text=message)

    pickle.dump(fee_links, open("db.p", 'wb'))
    return

feederek()