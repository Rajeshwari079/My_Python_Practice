class Address:
    def __init__(self,a,c,s):
        self.area=a
        self.city=c
        self.state=s

    def disp_add(self):
        print('Area is : ',self.area)
        print('city is : ',self.city)
        print('state is : ',self.state)

Bangalore = Address('Marathahalli','Bangalore','Karanataka')

class Student:
    def __init__(self,n,a,c,ad):
        self.name=n
        self.age=a
        self.sclass=c
        self.address=ad

    def std_details(self):
        print('student name is : ',self.name)
        print('student age is : ',self.age)
        print('student sclass is : ',self.sclass)
        print('student address is : ',self.address)

        # print(self.address.disp_add())

raji = Student('Rajeshwari',22,'Graduate','Bangalore')
raji.std_details()
         
        
