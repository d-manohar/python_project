def outer(arg):#arg=wishFaddress
    print('outer is started')
    print('arg value is ',arg)
    def inner():
        print('inner has started')
        arg()
        print('inner has ended')
    print('outer is ended')
    return inner

@outer#wish=outer(wishFaddress)#wish=innerFunctionaddress
def wish():
    print('started wish')
    print('endd wish')

print('wish value is',wish)
wish()