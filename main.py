#program to convert any value to ascii code and vice versa by Not Krishna
#defining functions
def binary():                                        #normal to ascii
    a = input("Enter value: ")
    for i in a:
        print("══════════════════════════")
        print("The ASCII code of",i,'is',ord(i))
        print("══════════════════════════")
def alpha():                     #ascii to normal
    a=[]
    v = int(input("Enter length of ASCII codes to be converted: "))
    for i in range(0,v):
        print("Enter number at position", i,": ")
        item = int(input())
        a.append(item)
    print(a)
    for i in a:
        print("══════════════════════════")
        print("The ASCII of",i,"is",chr(i))
        print("══════════════════════════")
#main
while True:
    print("☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵\n ASCII CODDE CONVERTER\n☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵")
    print("")
    print('Convert character to ASCII: 1')
    print('Convert ASCII to character: 2')
    print('Exit: 3')
    print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
    choice=input('Your choice: ')
    print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
    if choice=="1":
        binary()
    if choice=="2":
        alpha()
    if choice=="3":                #direct exit
        break
    end=input("Continue?? ")
    if end=="yes":
        print("╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍")
        print("")
        print("")
        continue
    if end=="no":              #exit after program is used
        print("〄⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉The End⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉⑉〄")
        break
    
