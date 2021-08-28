print("--------WELL COME TO UBER APP-----")
import random
l1=[1,1.5,2,2.5,3]
def rider(destination,kilometers,vechile):
    rounds=int(input("enter how many times do you want take  rounds::"))
    amount=0
    index=1
    dict={}
    l2=random.choice(l1)
    contact_information={"Bujji":9063430003,"RANI":7893592978,"chinna":888519989,"mosha":9989454089}
    while index<=rounds:
        dict[destination]=kilometers
        amount=dict1[vechile]*kilometers
        time=dict[destination]*l2
        index=index+1
    print(contact_information)
    call=input("do you  want to call yes/no:")
    if call=="yes":
        name=input("enter driver name here::")
        print(contact_information[name])
    elif call=="no":
        print("no nedd to call")
    print(dict)
    print("time taking for ",rounds,"rounds",time,"min")
    print("total amount",amount)
destination=input("enter the destination point::")
kilometers=int(input(" the distance b/w current location to  destionation point::"))
dict1={"mini":7,"auto":5,"prime_sedan":8,"prime_play":9,"prime_suv":10}
print(dict1)
vechile=input("slect your vechile::")
confarmation=input("enter do you want to ride:")
if confarmation=="yes":
    rider(destination,kilometers,vechile)
elif confarmation=="no":
    print("canclled the vechile")










