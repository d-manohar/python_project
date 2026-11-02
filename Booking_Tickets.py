class Multiplex:
    def __init__(self):
        self.availableTickets=500
    def booking(self):
        tickets=int(input('enter how many tickets u need'))
        if self.availableTickets>=tickets:
            self.availableTickets-=tickets
            print('Tickets are Booked sucessFully')
        else:
            print('House Full')
        print('available Tickets are',self.availableTickets)



Manohar=Multiplex()
print(Manohar)
Manohar.booking()
Sandeep=Multiplex()
print(Sandeep)
Sandeep.booking()        