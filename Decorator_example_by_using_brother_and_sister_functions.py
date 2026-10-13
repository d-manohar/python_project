def brother(arg):
    def inner():
        print('brother attempted the call')
        print('connecting to sister')
        arg()
        print('brother ended the call')
    return inner

@brother#sister=brother(sisterFaddress)#sister=innerFaddress
def sister():
    print('startint speaking to sister')
    print('ended speaking to sister')

sister()