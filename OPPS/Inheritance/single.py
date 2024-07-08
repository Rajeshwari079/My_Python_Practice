class Bank_v1:
    b_name='SBI'
    b_roi=6
    b_ifsc=1234
    b_address='kenya'

    def __init__(self,n,ac,bl,ad):
        self.cname=n
        self.account=ac
        self.cbalance=bl
        self.caddress=ad

    def customer_details(self):
        print('cutomer name is : ',self.cname)
        print('cutomer account is : ',self.account)
        print('cutomer cbalance is : ',self.cbalance)
        print('cutomer caddress is : ',self.caddress)

    @staticmethod
    def get_int_val():
        val=int(input("Enter a value : "))
        return val
    
    def withdraw(self):
        amt= self.get_int_val()
        if self.cbalance>amt:
            self.cbalance-=amt
            print('Withdrawn amt susscess....')
        else:
            print("Insufficient balance")

    def deposit(self):
        amt=self.get_int_val()
        if amt>0:
            self.cbalance+=amt
            print("Deposited Sucessfull........")
            print("Balance amt : ",self.cbalance)
        else:
            print("Enter the amount greater than Zero......")

class Bank_v2(Bank_v1):
    b_address='Bangalore'
    b_mob='76543'

    @classmethod
    def Bank_details(cls):
        print(f'Banke name is : {cls.b_name}')
        print(f'Bank roi is : {cls.b_roi}')
        print(f'Bank b_ifsc is : {cls.b_ifsc}')
        print(f'Bank b_address is : {cls.b_address}')
        print(f'Bank b_mob is : {cls.b_mob}')

    @classmethod
    def change_roi(cls):
        newroi=cls.get_int_val()
        cls.b_roi=newroi
        print("Bank roi has changes successfully......")

raji=Bank_v2('Rajeshwari',1234,31000,'Bidar')

raji.customer_details()
print()

raji.Bank_details()
print()

raji.deposit()
