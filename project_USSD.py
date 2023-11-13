main={1:"Transfer Money", 2:"Airtime",3:"Promo",4:"Financial Services",5:"Account Management"}
transfer_menu={1:"Momo User", 2:"Non-User", 3:"Other Networks",4:"Back"}

airtime={1:"",2:"Back"} 
promo={1:"Big Promo",2:"Back"}
financial={1:"With different",2:"Bank",3:"Back"}
account_management={1:"Help",2:"Customer care",3:"Special Services",4:"Back"}
def main_menu():
    for key,val in main.items():  #This makes the options listed per line
        print(key,val)
def trans_menu():
    for key,val in transfer_menu.items():
        print(key,val)
def airtime_menu():
    for key,val in airtime.items():
        print(key,val)
def prompt_menu():
    for key,val in promo.items():
        print(key,val)
def financial_menu():
    for key,val in financial.items():
        print(key,val)
def back_menu():
    for key,val in main.items():
        print(key,val)
def account_menu():
    for key,val in account_management.items():
        print(key,val)

def start():
    main_menu()
    a=int(input("select a number :"))
    if(a in main):                  #compare if the user input is in the dictionary
           opt_1=main[a]
           if(opt_1=="Transfer Money"):
                print("Transfer Money")
                trans_menu()
                a=int(input("select a number :"))
                if(a in transfer_menu):
                    opt_1=transfer_menu[a]
                    if(opt_1=="Momo User"):
                        print("Feature would be updated")
                    elif(opt_1=="Non-User"):
                        print("Feature would be updated")
                    elif(opt_1=="Other Networks"):
                        print("Feature would be updated")
                    elif(opt_1=="Back"):
                        start()
                    else:
                        print("Invalid input")
                else:
                    print("Invalid input")         

           elif(opt_1=="Airtime"):
                print("Airtime")
                airtime_menu()
                a=int(input("Select a number : "))
                if(a in airtime):
                    opt_1=airtime[a]
                    if(opt_1==""):
                        print("Not yet")

                    else :
                        if (opt_1=="Back"):
                         start()

           elif(opt_1=="Promo"):
                print("Promo")
                prompt_menu()
                a=int(input("Select a number : "))
                if(a in promo):
                    opt_1=promo[a]
                    if(opt_1=="Big Promo"):
                        print("Welcom to the Big Promo")
                    elif(opt_1=="Back"):
                        start()
                    else:
                        print("Invalid option")
                else:
                    print("Invalid option")

           elif(opt_1=="Financial Services"):
                print("Financial Services")
                financial_menu()
                a=int(input("Select a number : "))
                if(a in financial):
                    opt_1=financial[a]
                    if(opt_1=="With different"):
                        print("Welcome to the Financial Services")
                    elif(opt_1=="Bank"):
                        print("Futher Information Would be sent to you")
                    elif(opt_1=="Back"):
                        start()
                    else:
                        print("Invalid option")
                else:
                    print("Invalid option")
            

           elif(opt_1=="Account Management"):
                print("Account Management")
                account_menu()
                a=int(input("Select an option : "))
                if(a in account_management):
                    opt_1=account_management[a]
                    if(opt_1=="Help"):
                        print("Pleae how may we help you")
                    elif(opt_1=="Customer care"):
                        print("Please be patient as we get you to customer service")
                    elif(opt_1=="Special Services"):
                        print("Please input your request")
                    elif(opt_1=="Back"):
                        start()
                    else:
                        print("Invalid input. Please try again")
                        #a=int(input("Please try again"))
                        start()
                else:
                    print("Invalid input. Exiting.")






           else:
                print("Unknown option,exiting...")
    else:
        print("Invalid input,exiting...")




user_ussd=input("Please enter the Ussd code ")
if(user_ussd =="*170#"):
    main_menu()
    a=int(input("select a number :"))
    if(a in main):                  #compare if the user input is in the dictionary
        opt_1=main[a]
        if(opt_1=="Transfer Money"):
            print("Transfer Money")
            trans_menu()
            a=int(input("select a number :"))
            if(a in transfer_menu):
                opt_1=transfer_menu[a]
                if(opt_1=="Momo User"):
                    print("Feature would be updated")
                elif(opt_1=="Non-User"):
                    print("Feature would be updated")
                elif(opt_1=="Other Networks"):
                    print("Feature would be updated")
                elif(opt_1=="Back"):
                    start()
                else:
                    print("Invalid input")
            else:
                print("Invalid input")         
        





        elif(opt_1=="Airtime"):
            print("Airtime")
            airtime_menu()
            a=int(input("Select a number : "))
            if(a in airtime):
                opt_1=airtime[a]
                if(opt_1==""):
                    print("Not yet")

                else :
                    if (opt_1=="Back"):
                     start()



        elif(opt_1=="Promo"):
            print("Promo")
            prompt_menu()
            a=int(input("Select a number : "))
            if(a in promo):
                opt_1=promo[a]
                if(opt_1=="Big Promo"):
                    print("Welcom to the Big Promo")
                elif(opt_1=="Back"):
                    start()
                else:
                    print("Invalid option")
            else:
                print("Invalid option")





        elif(opt_1=="Financial Services"):
            print("Financial Services")
            financial_menu()
            a=int(input("Select a number : "))
            if(a in financial):
                opt_1=financial[a]
                if(opt_1=="With different"):
                    print("Welcome to the Financial Services")
                elif(opt_1=="Bank"):
                    print("Futher Information Would be sent to you")
                elif(opt_1=="Back"):
                    start()
                else:
                    print("Invalid option")
            else:
                print("Invalid option")

        elif(opt_1=="Account Management"):
            print("Account Management")
            account_menu()
            a=int(input("Select an option : "))
            if(a in account_management):
                opt_1=account_management[a]
                if(opt_1=="Help"):
                    print("Pleae how may we help you")
                elif(opt_1=="Customer care"):
                    print("Please be patient as we get you to customer service")
                elif(opt_1=="Special Services"):
                    print("Please input your request")
                elif(opt_1=="Back"):
                    start()
                else:
                    print("Invalid input. Please try again")
                    #a=int(input("Please try again"))
                    start()
            else:
                print("Invalid input. Exiting.")



        else:
            print("Unknown option,exiting...")

    else:
        print("Invalid input,exiting...")

    # print("1.")
else:
    print("No valid Ussd code")
    user_ussd=input("Please enter the Ussd code ")
    if(user_ussd=="*170#"):
     start()
    else:
        print("Invalid Ussd code,exiting")