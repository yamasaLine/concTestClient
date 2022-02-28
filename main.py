import threading
from multiprocessing.dummy import Pool as ThreadPool
import requests
import time
import random
import logging


logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

def print_hi(name):
    logging.info(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def send_req(num):
    while True:
        time.sleep(0.5)
        logging.info("cur tid:" + str(threading.get_ident()))
        if random.randint(1, 1000) % 2 == 0:
            resp = requests.get("http://127.0.0.1:80/order/create/aabb", headers={"user": "forv1"})
        else:
            resp = requests.get("http://127.0.0.1:80/order/create/aabb")

        logging.info("resp status code:" + str(resp.status_code))
        if resp.status_code == 200:
            logging.info(resp.text)


if __name__ == '__main__':
    print_hi('PyCharm')
    pool = ThreadPool(30)
    results = pool.map(send_req, range(0, 29))
    pool.close()
    pool.join()



