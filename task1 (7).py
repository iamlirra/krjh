import requests
import threading
import os

os.mkdir('user_data')


def f():
    for i in range(int(threading.current_thread().name) * 3, int(threading.current_thread().name) * 3 + 3):
        responce = requests.get('https://randomuser.me/api/')
        json = responce.json()
        os.mkdir(f'user_data/{i}')
        with open(f'user_data/{i}/user_info.txt', 'w', encoding='utf-8') as file:
            file.write(responce.text)
        with open(f'user_data/{i}/image.jpg', 'wb') as image:
            image_link = json['results'][0]['picture']['large']
            image_bytes = requests.get(image_link).content
            image.write(image_bytes)
        with open(f'user_data/{i}/cat_fact.txt', 'w') as file:
            responce = requests.get('https://catfact.ninja/fact')
            json = responce.json()
            fact = json['fact']
            file.write(fact)


if __name__ == '__main__':
    th1 = threading.Thread(target=f, name='0')
    th1.start()
    th2 = threading.Thread(target=f, name='1')
    th2.start()
    th3 = threading.Thread(target=f, name='2')
    th3.start()
    th4 = threading.Thread(target=f, name='3')
    th4.start()
