from handler import *

man = test()
band = True
while band:
    print ("==========================")
    print ("1.Register \n2.Listing \n3.Search Name \n4.Exit")
    print ("==========================")
    op = input("Enter Op")
    if(op==1):        
        name = input("Enter name")
        lname = input("Enter lname")
        age = input("Enter age")
        rankin = input("Enter ranking")
        man.savePlayer (name, lname, age, rankin)
        print ("Player registration OK")
        pass
    elif(op==2):
        man.listAll()
        pass
    elif(op==3):
        name = raw_input("Enter Name")
        man.searhName(name)
    elif(op==4):
        band=False
    
    else:
        print ("Invalid Option")
        
        
        
        
        
        
        
        
    