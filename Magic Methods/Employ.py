class Employ():
    cname='TCS'
    caddress='BAnagalore'
    emp_cnt=0

    def __init__(self,n,i,s):
        self.ename=n
        self.eid=i
        self.esal=s

        Employ.emp_cnt+=1

    def __del__(self):
        emp_cnt-=1

emp1=Employ('Raji',7,60000)
emp2=Employ('Riya',9,80000)

print(Employ.emp_cnt)
del emp2
print(Employ.emp_cnt)

    