from handler import *


man = test()
band=True
while band:
    print ("==========================")
    print ("1.Register \n2.Listing \n3.Search Name \n4.Exit")
    print ("==========================")
    op=eval(input("Ingrese op "))
    if(op==1):        
        name = input("Enter name ")
        lname = input("Enter lname ")
        age = eval(input("Enter age "))
        rankin = eval(input("Enter rankin "))
        man.savePlayer(name, lname, age, rankin)
        print ("Player registration OK")
        pass
    elif(op==2):
        man.listAll()
        pass
    elif(op==3):
        name = input("Enter name ")
        man.searhName(Nombre)
    elif(op==4):
        band=False
    
    else:
        print ("Invalid Option")
        
        
        
        
        
        
        
        
    