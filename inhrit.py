class person:
    def __init__(self,name,contact):
        self.name=name
        self.contact=contact
        print(self.name,self.contact)
class Doctor(person):
    pass
class patient(person):
    pass
doc1=Doctor("Hameed",1222534)
pat1=patient("Anil",3333222)


    