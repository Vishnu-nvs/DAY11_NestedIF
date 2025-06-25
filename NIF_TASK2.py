#Declare list with values ["Python","Django",["django","python",(1,4,5,6,"Vishnu")]]
#in the given list elements if u find any tuple elements are there then find out Last element  
# if the last element is  String then reverse that String and print reversed String otherwise Print Tuple elements.

V=["Python","Django",["django","python",(1,4,5,6,1)]]
print(V[2][2])
print(type(V[2][2]))

    
if tuple is type(V[2][2]):
    #print("We have tuple elemts")   -->testing purpose
    print(V[2][2][-1])
    if type(V[2][2][-1]) is str:
        print(V[2][2][-1][-1:-7:-1])
    else:
        print(V[2][2])

