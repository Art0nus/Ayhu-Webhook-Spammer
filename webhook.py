import sys
import time
import os
import requests
#Coded by Ayhuuu 
from colorama import Fore, init
#https://github.com/Ayhuuu
class webhook_spam:
    def __init__(self):
        self.choice = int(input(f"{Fore.MAGENTA}Webhook Spam icin (1) yada silmek icin (2){Fore.RESET} >>> "))

        if self.choice not in [1,2]:
            print(f"{Fore.RED}Yanlis Secim!") 
            str(input(f"{Fore.MAGENTA}Cikmak icin bir tusa basiniz..."))
            sys.exit()

        if self.choice == 1:
            self.webhook = str(input(f"{Fore.MAGENTA}Webhook{Fore.RESET} >>> "))

            if not self.check_webhook(self.webhook): 
                print(f"{Fore.RED}Yanlis Webhook!{Fore.RESET}")
                str(input(f"{Fore.MAGENTA}Cikmak icin bir tusa basiniz..."))
                sys.exit()

            self.message = str(input(f"{Fore.MAGENTA}Mesaj{Fore.RESET} >>> "))
            self.iterations = int(input(f"{Fore.MAGENTA}Iterations{Fore.RESET} >>> "))

            if self.iterations < 0:
                print(f"{Fore.RED}Yanlis Iterations!{Fore.RESET}")
                str(input(f"{Fore.MAGENTA}Cikmak icin bir tusa basiniz..."))
                sys.exit()

            self.spam_threads(self.webhook, self.inflate_message(self.message), self.iterations)

        if self.choice == 2:
            self.webhook = str(input(f"{Fore.MAGENTA}Webhook{Fore.RESET} >>> " ))
            print(f"{Fore.GREEN}Webhook Siliniyor!{Fore.RESET}")
            requests.delete(self.webhook)
            print(f"{Fore.GREEN}Webhook Silindi!{Fore.RESET}") 
            str(input(f"{Fore.MAGENTA}Cikmak icin bir tusa basiniz..."))
            sys.exit()

    def spam_threads(self, webhook, message, iterations):
        def spam(webhook, message):
            r = requests.post(
                webhook,
                json = {"content" : message}
            )
            
            if r.status_code == 204:
                print(f"{Fore.GREEN}Yollandi! | {r.status_code}\n{Fore.RESET}")
                
            elif r.status_code == 429:
                print(f"{Fore.RED}Limit Yedi! | {r.status_code}\n{Fore.RESET}")
                return 429
                
            else:
                print(f"{Fore.YELLOW}{r.status_code}\n{Fore.RESET}")
                str(input(f"{Fore.MAGENTA}Cikmak icin bir tusa basiniz..."))
                sys.exit()
                
        for x in range(iterations):
            for y in range(5):
                if spam(webhook, message) == 429:
                    time.sleep(5)
                
            time.sleep(5)
            
    def inflate_message(self, message):
        message = f"@everyone {message}\n"
        message = message * (999//len(message) + 1)
        return message
             
    def check_webhook(self, webhook):
        try:
            with requests.get(webhook) as r:
                if r.status_code == 200:
                    return True
                else:
                    return False
        except:
            return False
    
if __name__ == "__main__":
    init()
    
    if not os.name == "nt":
        os.system("clear")
    else:
        os.system("cls")
    
    try: webhook_spam()
    except KeyboardInterrupt: input(f"\n\n{Fore.YELLOW}KeyboardInterrupt: Cikiliyor...{Fore.RESET}")
    except Exception as e: input(f"\n\n{Fore.RED}Error: {e}{Fore.RESET}")
