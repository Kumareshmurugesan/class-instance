i=1
data=()
for i in range(0,i):
    sno=int(input("Enter serial-number:"))
    name=input("Enter student name:")
    tamil=int(input("Enter your tamil mark:"))
    english=int(input("Enter your english mark:"))
    maths=int(input("Enter your maths mark:"))
    science=int(input("Enter your science mark:"))
    social=int(input("Enter your social mark:"))
    total=tamil+english+science+maths+social
    print("Total:",total,"/500")
    average=total/5
    lst=list(data)
    print("Average:",average)
    print(type(lst))
    lst.append(sno)
    lst.append(name)
    lst.append(tamil)
    lst.append(english)
    lst.append(maths)
    lst.append(science)
    lst.append(social)
    lst.append(total)
    lst.append(average)
    print(lst)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@")



print(lst[i])