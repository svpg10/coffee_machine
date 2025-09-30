tank ={"milk" : 200 , "water" : 200 , "coffee" : 50 }
profit=0
menu = {"latte" : {"ingredeints":{"milk" : 20 ,"water": 30 , "coffee" : 5 } , "cost" : 150 } , "cappa" : {"ingredeints" :{"milk": 20,"water" :30 ,"coffee" : 5},"cost" : 170},"frappa" : { "ingredeints" :{"milk" :30,"water": "15","coffee":7},"cost":200},}
def check_resource(order_items,n):
    for things in order_items:
        if (order_items[things]*n) > tank [things] :
          print(f"sorry cannot process further since {things} is not suffceint")
          return False 
        else :
         return True
def coffee_making(coffee_ingredeints,n) :
    for item in coffee_ingredeints :
         tank[item] -= (coffee_ingredeints[item]*n)
    print(f"coffee is prepared ........... ENJOY")
    return  True
def payment_successful(payment,coffee_cost,n) :
      if payment > coffee_cost*n : 
       global profit 
       profit+=(coffee_cost*n)
       change=payment-(coffee_cost*n) 
       print(f"here is your change of {change} Rs")
       return True
      else :
        print(f"the amount entered is not enough")
        return False
def collect_coins():
       total=0
       t1=int(input("enter how many 5 Rs coins :"))
       t2=int(input("enter how many 10 Rs coins :"))   
       t3=int(input("enter how many 20 Rs coins :"))
       total=t1*5  + t2*10 +  t3*20
       return total  
machine_over=True 
while machine_over :
    userchoice=input("enter what would you like to have cappa or latte or frappa:")
    

    if userchoice== "off" :
        machine_over = False 
    elif userchoice== "report" :
        print(f"{tank["milk"]} ml of milk is present")
        print(f"{tank["water"]} ml of water is present")
        print(f"{tank["coffee"]} g of coffee is present")
        machine_over= False
    else:
        alpha=int(input("how many would you like to have:"))
        coffee_choice=menu[userchoice]  
        print(coffee_choice)
        if check_resource(coffee_choice['ingredeints'],alpha):
            print(f"The cost of your {userchoice} is {coffee_choice['cost']*alpha} Rs.")
            payment = collect_coins()
            if payment_successful(payment, coffee_choice["cost"],alpha):
                coffee_making(coffee_choice['ingredeints'],alpha)  
    