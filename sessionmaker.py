from telethon import TelegramClient
from telethon.sessions import StringSession


API_KEY = int(input("13157166"))
API_HASH = input("783f9253986d313c50d0c0a309d40df4") 


bot = TelegramClient(StringSession(), API_KEY, API_HASH)
bot.start()
string_session = bot.session.save()
print(string_session)
