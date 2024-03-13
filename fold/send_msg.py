import requests
import fyers_apiv3
import telegram
import matplotlib.pyplot as plt
def send_msg(message):
    TOKEN = "6832260988:AAH9i3B-HGAN-M8B4TgCr6tfdXOcR2pJn_U"
    chat_id = "5113043642"
    # message = "hello from your telegram bot"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    # print(requests.get(url).json())
    requests.get(url)
i=0
while i<5:
    send_msg(f"hello {i}")
    i+=1