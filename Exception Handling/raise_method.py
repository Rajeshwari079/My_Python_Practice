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
            try:
                raise Insuf_Bal_Error('Entered amt is less than Balance')
            except Insuf_Bal_Error as ibe:
                print(ibe)

    def deposit(self):
        amt=self.get_int_val()
        if amt>0:
            self.cbalance+=amt
            print("Deposited Sucessfull........")
            print("Balance amt : ",self.cbalance)
        else:
            print("Enter the amount greater than Zero......")


raji=Bank_v1('Rajeshwari',1234,31000,'Bidar')

raji.customer_details()
print()

raji.withdraw()
print()

raji.deposit()

#  & "C:/Program Files/Python311/python.exe" "c:/Users/jadha/OneDrive/Desktop/Python/Exception Handling/raise_method.py"
