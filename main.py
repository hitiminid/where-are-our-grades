import pdb
import smtplib
from bs4 import BeautifulSoup
import requests
import time
import random
import datetime
import json


def get_data(config_path='config.json'):
    with open(config_path, 'r') as f:
        return json.load(f)


def send_email(mailing_data):
    user, password = mailing_data['emailAddress'], mailing_data['emailPassword']
    mailing_list, email_text =  mailing_data['mailingList'], mailing_data['emailText']
    server = mailing_data['server']

    try:
        server = smtplib.SMTP_SSL(server, 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, mailing_list, email_text)
        server.close()
        print('Emails sent')
    except:
        print('Something went wrong while sending emails')


def perform_check(address, wait_time, mailing_data=None, element=None):
    site = requests.get(address)
    soup = BeautifulSoup(site.content, 'html.parser')
    previous_state = current_state = soup if element is None else soup.find(element['tag'], element['details'])

    while True:
        site = requests.get(address)
        soup = BeautifulSoup(site.content, 'html.parser')
        current_state = soup if element is None else soup.find(element['tag'], element['details'])

        if previous_state != current_state:
            print(f'[{datetime.datetime.now()}] New Content Appeared')
            send_email(mailing_data)
            break
        else:
            print(f'[{datetime.datetime.now()}] Still waiting :(')

        previous_state = current_state
        t = wait_time
        t += random.uniform(wait_time // 20, wait_time // 10)
        print(f'Waiting for {t} seconds')
        time.sleep(t)


def main():
    data = get_data()
    perform_check(data['address'], data['waitTime'], data['mailingData'], data['element'])


if __name__ == '__main__':
    main()
