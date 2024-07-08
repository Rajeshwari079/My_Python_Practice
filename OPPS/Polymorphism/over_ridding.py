class Bank_v1:
    b_name='SBI'
    b_roi=6
    b_ifsc=123
    b_add='Bidar'

    def __init__(self,n,ac,b,ad):
        self.cname=n
        self.account=ac
        self.balance=b
        self.address=ad

    def customer(self):
        print(f'name of custome = {self.cname}')
        print(f'account of custome = {self.account}')
        print(f'balance of custome = {self.balance}')
        print(f'address of custome = {self.address}')

    @staticmethod
    def get_int_val():
        val = int(input('Enter value'))
        return val


class Bank_v2():

    b_add='Bangalore'
    b_mob=987

    def __init__(self, n, ac, b, ad,cp):
        super().__init__(n, ac, b, ad)
        self.cpin=cp

    def customer(self):
         super().customer()
         print(f'cpin of custome = {self.cpin}')

    @classmethod
    def change_roi(cls):
        newroi=cls.get_int_val()
        cls.b_roi=newroi
        print('roi changed')

raji = Bank_v2('Rajeshwari',3445,4000,'NK',560037)
raji.customer()

    
