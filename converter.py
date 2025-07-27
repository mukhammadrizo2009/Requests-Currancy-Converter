from printer import (print_menu , print_currency_price ,
print_change_currency ,print_bye , end_or_no ,
print_change_currency2 , print_change_currency3 ,print_change_currency4)

from termcolor import colored
import sys
import json
import requests

while True:
    print_menu()

    choose = input("Amalni tanlang: ")

    if choose == "1":
        print_currency_price()
        url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/'
        response = requests.get(url)       
        content = response.content.decode()
        data = json.loads(content)       
        price_usd = float(data[0]['Rate'])
        
        url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/EUR/'
        response = requests.get(url)           
        content = response.content.decode()
        data = json.loads(content)        
        price_eur = float(data[0]['Rate'])
        
        print(colored(f"USD qiymati: {price_usd} (UZS)", "green"))
        print(colored(f"EUR qiymati: {price_eur} (UZS)", "green"))
        
        end_or_no()
        choosess = input("Amalni tanlang: ")
        
        if choosess == "1":
            choosess = False
            
        else:
            print_bye()
            break
            
    
    if choose == "2":
        print_change_currency()
        chooses = input("Amalni tanlang: ")
        if chooses == "1":
            print_change_currency2()
            chose = input("Amalni tanlang: ")
            if chose == "1":
                
                currecy = float(input("USD miqdorini kiriting: "))
                usd_url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/'
                usd_response = requests.get(usd_url)
                usd_data = json.loads(usd_response.content.decode())
                usd_to_uzs = float(usd_data[0]['Rate'])
                
                eur_url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/EUR/'
                eur_response = requests.get(eur_url)
                eur_data = json.loads(eur_response.content.decode())
                eur_to_uzs = float(eur_data[0]['Rate'])
                
                result01 = currecy * usd_to_uzs
                result = result01 / eur_to_uzs
                
                print(colored(f"{currecy} USD = {result:,.2f} (EUR)" , "green"))
                
                end_or_no()
                choosess = input("Amalni tanlang: ")
        
                if choosess == "1":
                    choosess = False
                else:
                    print_bye()
                    break
            
            if chose == "2":
                currecy = float(input("USD miqdorini kiriting: "))
                usd_url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/'
                usd_response = requests.get(usd_url)
                usd_data = json.loads(usd_response.content.decode())
                usd_to_uzs = float(usd_data[0]['Rate'])
                            
                uzs = 12_657
                            
                result = currecy * uzs
                            
                print(colored(f"{currecy} USD = {result:,.2f} (UZS)" , "green"))
                            
                end_or_no()
                tanlash = input("Amalni tanlang: ")
                            
                if tanlash == "1":
                    tanlash = False
                    
                else:
                    print_bye()
                    break
   
            if chose == "3":
                    print_bye()
                    sys.exit()
        
        if chooses == "2":
            print_change_currency3()
            chooses = input("Amalni tanlang: ")
            if chooses == "1":
                currecy = float(input("EUR miqdorini kiriting: "))
                eur_url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/EUR/'
                eur_response = requests.get(eur_url)
                eur_data = json.loads(eur_response.content.decode())
                eur_to_uzs = float(eur_data[0]['Rate'])
                        
                usd_url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/'
                usd_response = requests.get(usd_url)
                usd_data = json.loads(usd_response.content.decode())
                usd_to_uzs = float(usd_data[0]['Rate'])
                        
                result02 = currecy * eur_to_uzs
                result = result02 / usd_to_uzs

                print(colored(f"{currecy} EUR ≈ {result:,.2f} USD", "green"))
                        
                end_or_no()
                tanlamoq = input("Amalni tanlang: ")
                    
                if tanlamoq == "1":
                    tanlamoq = False
                    
                else:
                    print_bye()
                    break
                        
            
            if choose == "2":
                currecy = float(input("EUR miqdorini kiriting: "))
                eur_url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/EUR/'
                eur_response = requests.get(eur_url)
                eur_data = json.loads(eur_response.content.decode())
                eur_to_uzs = float(eur_data[0]['Rate'])
                    
                uzs = float(14_871)
                    
                result = currecy * uzs
                
                print(colored(f"{currecy} EUR ≈ {result:,.2f} UZS", "green"))
                    
                end_or_no()
                choosess = input("Amalni tanlang: ")
        
                if choosess == "1":
                    choosess = False
                        
                else:
                    print_bye()
                    break
                
            
            if choose == "3":
                print_bye()
                sys.exit()
        
        if chooses == "3":
            print_change_currency4()
            chose = input("Amalni tanlang: ")
            if chose == "1":
                currecy = float(input("UZS miqdorini kiriting: "))
                usd_url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/'
                usd_response = requests.get(usd_url)
                usd_data = json.loads(usd_response.content.decode())
                usd_to_uzs = float(usd_data[0]['Rate'])
                
                result = currecy / usd_to_uzs
                
                print(colored(f"{currecy} UZS ≈ {result:,.2f} USD", "green"))
                
                end_or_no()
                choosess = input("Amalni tanlang: ")
        
                if choosess == "1":
                    choosess = False
                else:
                    print_bye()
                    break
            
            if chose == "2":
                currecy = float(input("UZS miqdorini kiriting: "))
                eur_url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/EUR/'
                eur_response = requests.get(eur_url)
                eur_data = json.loads(eur_response.content.decode())
                eur_to_uzs = float(eur_data[0]['Rate'])
                
                result = currecy / eur_to_uzs
                
                print(colored(f"{currecy} UZS ≈ {result:,.2f} EUR", "green"))
                end_or_no()
                choosess = input("Amalni tanlang: ")
        
                if choosess == "1":
                    choosess = False
                else:
                    print_bye()
                    break
            
            if chose == "3":
                print_bye()
                sys.exit()    
            
        
        if chooses == "4":
            print_bye()
            sys.exit()
            
    if choose == "3":
        print_bye()
        sys.exit()