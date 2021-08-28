import json
print("***************WELL COME TO RIDE SERVICES**********")
print("@@@@COVER YOUR MASK AND SPRAY YOUR SANITISOR@@@@")
with open("ride.json","r") as f:
    data=json.load(f)
keys=["Id","Name","Isriding","Cardetails","Cash","Location","Type"]
Ride=input("Do you want to ride or not:")
list1=[]
if Ride=="yes":
    Id=input("enter your id number:")
    destination=input("ENTER your current location to destination point:")
    km=int(input("enter how many kilomiters you want:"))
    amount=km*5
    print("****THANK YOU FOR SELECTING MY CAB***")
    print("YOUR RIDE IS STARTING PLESE WAIT FOR SOME TIME")
    print("WAITING.....................")
    import time
    print("Ride the exact timing is",end="")
    print(time.ctime())
    time.sleep(2)
    list1=[]
    for i in data:   
        if i["Id"]==Id:
            if i["Isriding"]!=True:   
                print("******GET IN TO UBER CAB*******") 
                i["Location"]=destination
                i["Cash"]=amount
                # list1=[]
                for key in keys:
                    print(key,":",i[key])
                Rating=input("How much you want giving the rating:")
                Feedback=input("Enter the feedback about my car:")
                dict={}
                dict["Rating"]=Rating
                dict["Feedback"]=Feedback
                list1.append(dict)
                print(list1)
                # with open("uber.json","a") as f:
                #     json_string=json.dump(list1,f,indent=4)
            else:
                print("he is already in driving") 
    with open("uber.json","a") as f:
        json_string=json.dump(list1,f,indent=4)

else:
    print("*********CANCLLED THE CAB*******")
# with open("uber.json","a") as f:
#     json_string=json.dump(list1,f,indent=4)
# with open("uber.json","a") as f:
#        json_string=json.dump(list1,f,indent=4)
