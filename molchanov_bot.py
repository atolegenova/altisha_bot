import  requests
import config
#import json
from molchanov_parse import get_btc
from time import sleep



global last_update_id
last_update_id = 0
token = config.TOKEN
URL ='https://api.telegram.org/bot' + token + '/'
#https://api.telegram.org/bot1474480112:AAGD0RkYTbmqdZVVTDZAUASLZ7T4Dd4xGgo/sendmessage?chat_id=1029994960&text=hi
def get_updates():
    url =URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()
    last_object = data['result'][-1]
    curent_update_id = last_object['update_id']
    global last_update_id
    if last_update_id != curent_update_id:
        last_update_id = curent_update_id
        chat_id = last_object['message']['chat']['id']

        message_text = last_object['message']['text']
        message = {'chat_id': chat_id,
                   'text': message_text}
        return message
    return None

def send_message(chat_id, text='Wait a seccond please...'):
    url = URL + f'sendmessage?chat_id{chat_id}&text={text}'
    print(url)
    requests.get(url)


def main():
    #d = get_updates()
    while True:
    #print(get_massage())
    # with open('updates.json', 'w') as file:
    #     json.dump(d, file, indent =2, ensure_ascii=False)
    #send_message(13,'hi')
        answer = get_message()
        if answer !=None:

            chat_id = answer['chat_id']
            text = answer['text']
            #send_message(chat_id, text)


            if text == '/btc':
                send_message(chat_id, get_btc())
        else:
            continue
        sleep(2)


if __name__ == '__main__':
    main()