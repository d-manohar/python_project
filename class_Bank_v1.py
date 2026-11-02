class Bank_v1:
    bank_name='SBI'
    bank_roi=5
    bank_ifsc=12345
    def __init__(self,cn,ca,cb):
      self.cname=cn
      self.caccount=ca
      self.cbal=cb
    @classmethod
    def bank_details(cls):
       print(f'Name of the Bank is {cls.bank_name}')
       print(f'roi of the Bank is {cls.bank_roi}')
       print(f'ifsc of the Bank is{cls.bank_ifsc}')
    @staticmethod
    def get__init__value():
       intvalue=int(input('enter value'))
       return intvalue
    def customer_details(self):
       print(f'name of the customer is {self.caccount}')
       print(f'account of the customer is{self.caccount}')
       print(f'balance of the customer is {self.cbal}')
    def withdraw(self):
       amount=self.get_int_value()
       if amount<=self.cbal:
          self.cbal-=amount
          print('withdrawal is SuccessFull')
       else:
          print('inSuffient balance')
       print('Available Balance is',self.cbal)
class Bank_v2(Bank_v1):
   bank_roi=7
   bank_branch='Bangalore'
   def __init__(self,cn,ca,cb,cp):
      self.cname=cn
      self.caccount=ca
      self.cbal=cb
      self.cpin=cp
   @classmethod
   def bank_details(cls):
      print(f'Name of the Bank is {cls.bank_name}')
      print(f'roi of the Bank is{cls.bank_rai}')
      print(f'ifsc of the Bank is{cls.bank_ifsc}')
      print(f'branch of the Bank is {cls.bank_branch}')



   def withdraw(self):
       pin=self.get_int_value()
       if pin==self.cpin:
          amount=self.get_int_value()
          if amount<=self.cbal:
             self.cbal-=amount
             print('withdrawal is SuccessFull')
          else:
            print('Insufficicent Balance')
          print('Available Balance is',self.cbal)

       else:
          print('Incorrect pin')


def deposite(self):
    amount=self.get_int_value()
    self.cbal+=amount
    print('Deposite is Successfull')


        

    
       