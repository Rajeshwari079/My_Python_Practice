class Book:
    def __init__(self,n,a,p):
        print('Object created')
        self.bname=n
        self.bauthor=a
        self.bprice=p

        def __str__(self):
            return self.bname,self.bauthor,str(self.bprice)
        
        def __del__(self):
            print(f'{self} object deleted ')

B1=Book('Da vinci code ','Dan Brown',800)
B2=Book('Divergent','allen solley',600)

print(B1) #prints the object addr
