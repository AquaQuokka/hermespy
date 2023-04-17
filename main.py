import os
import configparser
import getpass
import smtplib
import subprocess
import time
import re
import ctypes

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

if not os.file.exists('config.ini'):
    with open('config.ini', 'w') as f:
        f.write('[config]\n')
        f.write('host = smtp.example.com\n')
        f.write('port = 587\n')
        f.write('username = john.smith@example.com\n')
        f.write('password = *\n')
    exit()

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

subject = input('Subject: ')

with open('message.txt', 'w') as f:
    subprocess.call(['notepad.exe', f.name])

with open('message.txt', 'r') as f:
    body = f.read()

response = ctypes.windll.user32.MessageBoxW(None, "Do you want to send the email?", "HermesPy", 0x30 | 0x01 | 0x1000)


if response == 1:

    message = f'Subject: {subject}\n\n{body}'

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

    finally:
        os.remove('message.txt')

    with open(f'sent/{int(time.time())}.txt', 'w') as f:
        f.write(message)

elif response == 2:

    message = f'Subject: {subject}\n\n{body}'
    os.remove('message.txt')
    with open(f'drafts/{int(time.time())}.txt', 'w') as f:
        f.write(message)