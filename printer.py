from termcolor import colored

def print_menu():
    print(colored("==== M E N U ====","magenta"))
    print(colored("1. Kurs narxini ko'rish!", "blue"))
    print(colored("2. Valyuta almashterish!" , "blue"))
    print(colored("3. Dasturdan chiqish!" , "blue"))
    
def print_currency_price():
    print(colored("= Bugungi kurs narxlari =" , "cyan"))
    
def print_change_currency():
    print(colored("= Valyutani tanlang =", "cyan"))
    print(colored("==== M E N U ====","magenta"))
    print(colored("1. USD (Dollar)" , "cyan"))
    print(colored("2. EUR (Euro)" , "cyan"))
    print(colored("3. UZS (So'm)" , "cyan"))
    print(colored("4. Dasturni yakunlash!" , "cyan"))
    
def print_bye():
    print(colored("Dasturimizdan foydalanganingiz uchun, Tashakkur!","cyan"))
    
def end_or_no():
    print(colored("==== M E N U ====","magenta"))
    print(colored(" Yana amal bajarasizmi?" , "cyan"))
    print(colored("1. Ha!" , "cyan"))
    print(colored("2. Yo'q!" , "cyan"))
    
def print_change_currency2():
    print(colored("= Qaysi valyutaga almashmoqchisiz! =", "cyan"))
    print(colored("==== M E N U ====","magenta"))
    print(colored("1. EUR (Euro)" , "cyan"))
    print(colored("2. UZS (So'm)" , "cyan"))
    print(colored("3. Dasturni yakunlash" , "cyan"))
    
def print_change_currency3():
    print(colored("= Qaysi valyutaga almashmoqchisiz! =", "cyan"))
    print(colored("==== M E N U ====","magenta"))
    print(colored("1. USD (Dollar)" , "cyan"))
    print(colored("2. UZS (So'm)" , "cyan"))
    print(colored("3. Dasturni yakunlash" , "cyan"))
    
def print_change_currency4():
    print(colored("= Qaysi valyutaga almashmoqchisiz! =", "cyan"))
    print(colored("==== M E N U ====","magenta"))
    print(colored("1. USD (Dollar)" , "cyan"))
    print(colored("2. EUR (Euro)" , "cyan"))
    print(colored("3. Dasturni yakunlash" , "cyan"))