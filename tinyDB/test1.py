from tinydb import TinyDB, Query, where


class test:    
    def savePlayer(self, name, lname, age, rankin):
        
        db = TinyDB("players.json")
        lista = db.search(where("name")==name)
        if(len(lista)==0):
            db.insert({"name":name, "lname":lname, "age":age, "rankin":rankin})
        else:
            print ("this player is already registered in database")
            
    def listAll(self):
        db = TinyDB ("players.json")
        lista = db.all()
        for elem in lista:
            print ("==========================")
            print ("Name    :" , elem["name"])
            print ("Lname   :" , elem["name"])
            print ("Age     :" , elem["name"])
            print ("Ranking :" , elem["name"])
            print ("==========================")
    
    def searchName(self, name):
        db = TiniDB("players.json")
        lista = db.search(were("name")==name)
        for elem in lista:
            print ("==========================")
            print ("Name    :" , elem["name"])
            print ("Lname   :" , elem["name"])
            print ("Age     :" , elem["name"])
            print ("Ranking :" , elem["name"])
            print ("==========================")