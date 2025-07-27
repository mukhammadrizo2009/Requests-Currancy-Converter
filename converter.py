from printer import print_menu , print_currency_price , print_change_currency , print_bye , end_or_no , print_change_currency2 , print_change_currency3 , print_change_currency4
from termcolor import colored
import requests
import sys
while True:
    print_menu()

    choose = input("Amalni tanlang: ")

    if choose == "1":
        print_currency_price()
        
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
                url = 'https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD'
                price = requests.get(url)
                
                result = currecy * price
                print(colored(f"Bugungi kundagi natiga: {result:,.2f} (EUR)" , "green"))
                end_or_no()
                choosess = input("Amalni tanlang: ")
        
                if choosess == "1":
                    choosess = False
                else:
                    print_bye()
                    break
            
            if chose == "2":
                currecy = float(input("USD miqdorini kiriting: "))
                price = 12_700
                
                result = currecy * price
                print(colored(f"Bugungi kundagi natiga: {result:,.2f} (UZS)" , "green"))
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
        
        if chooses == "2":
            print_change_currency3()
            chose = input("Amalni tanlang: ")
            if chose == "1":
                currecy = float(input("EUR miqdorini kiriting: "))
                price = 1.2
                
                result = currecy * price
                print(colored(f"Bugungi kundagi natiga: {result:,.2f} (USD)" , "green"))
                
                end_or_no()
                choosess = input("Amalni tanlang: ")
        
                if choosess == "1":
                    choosess = False
                else:
                    print_bye()
                    break
            
            if chose == "2":
                currecy = float(input("EUR miqdorini kiriting: "))
                price = 13_700
                
                result = currecy * price
                print(colored(f"Bugungi kundagi natiga: {result:,.2f} (UZS)" , "green"))
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
        
        if chooses == "3":
            print_change_currency4()
            chose = input("Amalni tanlang: ")
            if chose == "1":
                currecy = float(input("UZS miqdorini kiriting: "))
                price = 0.01
                
                result = currecy * price
                print(colored(f"Bugungi kundagi natiga: {result:,.2f} (USD)" , "green"))
                
                end_or_no()
                choosess = input("Amalni tanlang: ")
        
                if choosess == "1":
                    choosess = False
                else:
                    print_bye()
                    break
            
            if chose == "2":
                currecy = float(input("UZS miqdorini kiriting: "))
                price = 0.009
                
                result = currecy * price
                print(colored(f"Bugungi kundagi natiga: {result:,.2f} (EUR)" , "green"))
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