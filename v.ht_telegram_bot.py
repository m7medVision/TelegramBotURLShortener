from pyrogram import Client,filters
from pyrogram import *
import requests
import config
app = Client("my_bot")
@app.on_message(filters.command(commands="vht",prefixes="."))
def start_command(client, message):
    app.send_message(chat_id=message.chat.id, text="plase wait") 
    ask1 = message.text
    ask = ask1.replace(".vht ", "")
    ask2 = ask.split()
    url = str(ask2[0])
    name = str(ask2[1])
    m = requests.get("https://v.ht/").headers
    r = m['Set-Cookie']
    removeal = r.replace("; path=/", "")
    data = {
        'txt_url': url,
        'txt_name': name
    }
    m = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '58',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': removeal,
        'Host': 'v.ht',
        'Origin': 'https://v.ht',
        'Referer': 'https://v.ht/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    r = requests.post('https://v.ht/processreq.php', data = data , headers=m).text
    if "Sorry, the entered suffix is already in use, please choose another one..!!" in r:
        app.send_message(chat_id=message.chat.id, text="suffix is already in use")
    elif "Sorry, the entered suffix contains invalid characters," in r:
        app.send_message(chat_id=message.chat.id, text="suffix contains invalid characters")
    elif 'The Short URL: ' in r:
        app.send_message(chat_id=message.chat.id, text=(f"https://v.ht/{name}"))
    else:
        app.send_message(chat_id=message.chat.id, text="There are mistake in my code :(")
@app.on_message(filters.command("start"))
def start_command(client, message):
    app.send_message(chat_id=message.chat.id, text="Type .vht URL suffix \n\n .vht https://example.com/ example \n\n The shorten URL will be v.ht/example \n\n This bot coded by MAJHCC \n Bot files: https://github.com/majhcc/TelegramBotURLShortener")
app.run()
