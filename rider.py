import json
print(" *********WELLCOME TO UBER RIDER********")
print("@@@@COVER YOUR MASK AND SPRAY YOUR SANITISOR@@@@")
vechile=input("SELECT your vechile:")
print("****THANK YOU FOR SELECTING MY CAB***")
print("YOUR RIDE IS STARTING PLESE WAIT FOR SOME TIME")
print("WAITING.....................")
list1=[{"mini":{"id":1,"name":"Nani","location":"huskur","isriding":"false"}},
    {"auto":{"id":2,"name":"Chinna","location":"hyd","isriding":"false"}},
    {"primeplay":{"id":3,"name":"Mosha","location":"medak","isriding":"false"}},
    {"primesedan":{"id":4,"name":"Hanok","location":"mumbai","isriding":"false"}}]
car_details=[{"id":1,"color":"red","carnum":4085,"mobilenum":9989454089,"brand":"ODY"},
            {"id":2,"color":"blue","carnum":5066,"mobilenum":885188889,"brand":"BMW"},
            {"id":3,"color":"black","carnum":4055,"mobilenum":7893592978,"brand":"SUZUKI"},
            {"id":4,"color":"white","carnum":8055,"mobilenum":9951998456,"brand":"ETOES"}]
destination=input("Enter the Destion place:")
km=input("Enter the how many kilomiters do want ride:")
def details(): 
    for k in list1:
        if  vechile in k:
            k[vechile]["location"]=destination
            print(k)
            for j in car_details:
                if k[vechile]["id"]==j["id"]:
                    print(j)
ride=input("Do you want to u ride:")
if ride=="yes":
    details()
    dict={}
    otp=int(input("Enter the otp number:"))
    print("******GET IN TO UBER CAB*******")
    amount=int(km)*5
    print("Totalcash",amount)
    cash=input("do you want phonepay/googlepay/cash: ")
    import time
    print("Ride the exact timing is",end="")
    print(time.ctime())
    time.sleep(20)
    rating=input("How much you want giving the rating:")
    feedback=input("Enter the feedback about my car:")
    dict["otp"]=otp
    dict["cash"]=cash
    dict["rating"]=rating
    dict["feedback"]=feedback
    print(dict)
    with open("uber.json","a") as f:
        json_string=json.dump(dict,f, indent=4)
else:
    print("Canclled the ride")
    print("**********DONT BOOK MY CAB AGIAN****")
