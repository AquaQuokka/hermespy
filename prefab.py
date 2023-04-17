import os
import re
import getpass
import smtplib
import subprocess
import configparser
import time
import ctypes
import json

config = configparser.ConfigParser()

paths = [
    'config.ini',
    './config.ini',
    os.path.join(os.path.dirname(__file__), 'config.ini')
]

config.read(paths)

email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if not os.path.exists('sent'):
    os.makedirs('sent')

if not os.path.exists('drafts'):
    os.makedirs('drafts')

if not os.path.exists('prefabs'):
    os.makedirs('prefabs')

host = config['config']['host']
user = config['config']['username']
recipient = input("To: ")

if not re.match(email_regex, recipient):
    print('Invalid email address!')
    exit()

if config['config']['port'] != "*":
    port = config['config']['port']
else:
    port = 587

if config['config']['password'] != "*":
    password = config['config']['password']
else:
    password = getpass.getpass('Password:\n')

folder = input('Enter prefab ID: ')
path = os.path.join('prefabs', folder)

if not os.path.isdir(path):
    print(f'{folder} not found in prefabs folder!')
    exit()

template_path = os.path.join(path, 'template.json')
reg_path = os.path.join(path, 'varfile')

if not os.path.isfile(template_path):
    print(f'{template_path} not found!')
    exit()

with open(f"{template_path}", 'r') as f:
    template = json.load(f)

response = ctypes.windll.user32.MessageBoxW(None, "Do you want to send the email?", "HermesPy", 0x30 | 0x01 | 0x1000)

if response == 1:

    message = f'Subject: {template["subject"]}\n\n{template["body"]}'

    """
    if os.path.isfile(reg_path):
        with open(os.path.join(path, '.var'), 'r') as f:
            regl = f.readlines()

            for line in regl:
                tval = input(f"Define {line}: ")
                message = message.replace(f"{line}",f"{tval}")
    """

    if os.path.isfile(reg_path):
        with open(reg_path, 'r') as f:
            regl = f.readlines()

            for line in regl:
                tval = input(f"Define {line.strip()}: ")
                message = message.replace(line.strip(), tval)


    try:
        server = smtplib.SMTP(host, port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, recipient, message)
        server.quit()
        print("Succesfully sent email!")

    except Exception as e:
        print(f"Something went wrong...\nWe think it started here:\n\n\u001b[31m{type(e).__name__}: {e}\u001b[0m")
    
    with open(f'sent/{int(time.time())}.txt', 'w') as f:
        f.write(message)

else:

    exit()
