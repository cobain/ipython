def salesgirl(method):
    def serve(*args):
        print "Salesgirl:Hello, what do you want?", method.__name__
        return method(*args)
    return serve
   
@salesgirl
def try_this_shirt(size):
    if size < 35:
        print "I: %d inches is to small to me" %(size)
        return False
    else:
        print "I:%d inches is just enough" %(size)
        return True
result = try_this_shirt(38)
print "Mum:do you want to buy this?", result
