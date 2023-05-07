from credentials import mobile_number
import requests
import schedule
import time

def send_message():
    res = requests.post('https://textbelt.com/text', {
        'phone': mobile_number,
        'message': 'Hello and Good Morning',
        'key' : 'textbelt'
    })
    print(res.json())

schedule.every(10).seconds.do(send_message) # Testing to see if a sample message is sent every 10s, for the library the limit to send text message is restricted to 1"

while True:
    schedule.run_pending()
    time.sleep(1)