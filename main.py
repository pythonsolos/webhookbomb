import os
import sys
import time
import requests
from colorama import Fore

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./75)

def title():
    os.system('cls')
    os.system('title WebhookBomb --- gui!#9165')
    print(Fore.MAGENTA + '██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗██████╗  ██████╗ ███╗   ███╗██████╗ ')
    print(Fore.MAGENTA + '██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝██╔══██╗██╔═══██╗████╗ ████║██╔══██╗')
    print(Fore.MAGENTA + '██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ ██████╔╝██║   ██║██╔████╔██║██████╔╝')
    print(Fore.MAGENTA + '██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗')
    print(Fore.MAGENTA + '╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝')
    print(Fore.MAGENTA + '╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝  ')
    print(Fore.MAGENTA + '                                                                           by pythonsolos')

def menuChoice():
    sprint(Fore.MAGENTA + '\n[1] Spammer\n[2] Deleter')
    menuInput = input(Fore.MAGENTA + '\nEnter input: >>> ')
    if menuInput == '1':
        spammer()
    if menuInput == '2':
        deleter()
    else:
        sprint(Fore.MAGENTA + '\nThe amount you have entered is invalid, please re-launch the program and enter a valid input.')
        time.sleep(1)
        exit()


def spammer():
    title()
    time.sleep(1)
    spammerInput = input(Fore.MAGENTA + '\nEnter the webhook URL: ')
    spammerMessage = input(Fore.MAGENTA + 'Enter the message: ')
    try:
        spammerAmount = int(input(Fore.MAGENTA + 'Enter the amount to spam: '))
    except:
        sprint(Fore.MAGENTA + '\nThe amount you have entered is invalid, please re-launch the program and enter a valid input.')
        time.sleep(1)
        exit()
    print('')
    while True:
        try:
            for i in range(int(spammerAmount)):
                spammerData = requests.post(spammerInput, json={'content':spammerMessage})
                if spammerData.status_code == 204:
                    print(Fore.GREEN + '[+] Sent')
                else:
                    print(Fore.RED + '[-] Ratelimited')
            sprint(Fore.MAGENTA + '\nSpamming complete.\nhttps://github.com/pythonsolos on top.')
            time.sleep(2)
            title()
            menuChoice()
        except Exception as e:
            sprint(Fore.RED + '\nBad webhook. Please re-launch the program and enter a valid webhook.')
            time.sleep(1)
            exit()

def deleter():
    title()
    time.sleep(1)
    deleterInput = input(Fore.MAGENTA + '\nEnter the webhook URL that you want to delete: ')
    deleterChoice = input(Fore.MAGENTA + 'Are you sure you want to delete this webhook? (y or n): ')
    if deleterChoice == 'y':
        try:
            deleterData = requests.delete(deleterInput)
            checkData = requests.get(deleterInput)
            if checkData.status_code == 404:
                sprint(Fore.MAGENTA + '\nWebhook successfully deleted.\nhttps://github.com/pythonsolos on top.')
                time.sleep(2)
                title()
                menuChoice()
        except:
            sprint(Fore.RED + '\nBad webhook. Please re-launch the program and enter a valid webhook.')
            time.sleep(1)
            exit()
    else:
        sprint(Fore.MAGENTA + '\nCancelling action...')
        time.sleep(2)
        title()
        menuChoice()
    

title()
menuChoice()