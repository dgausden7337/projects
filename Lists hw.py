Num = [1,2,3,4,5,6,7,8,9]
def FindLargest(List):
    Max = 0
    for each in List:
        if each > Max:
            Max = each
    print(Max)
Words = ["sliver","slime","potatoe","salad"]

def beginWs(List):
    numofS = 0
    for each in (List):
        if each[0] == "s" or "S":
            numofS = numofS + 1
            print(each)
    print(numofS)
           

def Average(List):
    total = 0
    for each in List:
        total = total + each
    average = total/len(List)
    print(average)


animals = ["cow","pig","chicken"]
def additions(List):
    check = False
    for each in range(1,7):
        List.append(input("what do you want to add to the list?"))
    check = input("do you want the me to list it backwards?").lower
    if check == "y" or "yes":
        check = True
    else:
        check = False
    if check == True:
        print(List[::-1])
    else:
        print(List[:])
    print(List[input("what number in the list do you want to see?")-1])
additions(animals)
     print(List[input("what number in the list do you want to see?")-1])
