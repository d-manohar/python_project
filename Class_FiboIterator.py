class FiboIterator:
    def __init__(self,A=2,B=3,N=10):
        print('Init is called')
        self.A=A
        self.B=B
        self.N=N
    def __iter__(self):
        print('iter is called')
        self.i=1
        return self
    def __next__(self):
        print('next is called')
        if self.i<=self.N:
            self.i+=1
            res=self.A
            self.A,self.B=self.B,self.A+self.B
            return res
        raise StopIteration

FIO = FiboIterator()
for k in FIO:
    print(k)        