# Creating an object of a class inside the constructor of another class


class Address:
    def __init__(self,a,ct,s):
        self.area=a
        self.city=ct
        self.state=s

    def disp_add(self):
        print('Area is : ',self.area)
        print('city is : ',self.city)
        print('state is : ',self.state)


class Student:
    def __init__(self,n,a,cl):
        self.name=n
        self.age=a
        self.sclass=cl
        

        ar = input('enter area : ')
        c = input('enter city : ')
        st = input('enter state : ')

        arcst = Address(ar,c,st)
        self.address=arcst
        


    def std_details(self):
        print('student name is : ',self.name)
        print('student age is : ',self.age)
        print('student sclass is : ',self.sclass)
        print('student address is : ')

        self.address.disp_add()

        # print(self.address.disp_add())

raji = Student('Rajeshwari',22,'Graduate')
raji.std_details()
         
        