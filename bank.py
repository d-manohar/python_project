class Bank:
    bank_name='union'
    bank_roi=8
    bank_branch='Rajamandary'
    def __init__(self,cn,ca,cb):
       self.cname=cn
       self.caccount=ca
       self.cbal=cb
    def customer_details(self):
        print(f'name of the customer is {self.cname}')
        print(f'account of the customer is {self.caccount}')
        print(f'balance of the customer is {self.cbal}')
    def withdraw(self):
        amount=int(input('enter amount'))
        if amount<=self.cbal:
            self.cbal-=amount
            print('withdrawal is successfull')
        else:
            print('Insufficient Balance')
        print('Available Balance is',self.cbal)
    def deposit(self):
        amount=int(input('enter amount'))
        self.cbal+=amount
        print('Deposite is Successfull')



Manohar = Bank('D.manohar',987654321009,100000)

Manohar.customer_details()
