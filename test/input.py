def interact( ):
    print 'Hello stream world'                      # print sends to sys.stdout
    while 1:
        try:
            reply  = raw_input('Enter a number>')   # raw_input reads sys.stdin
        except EOFError:
            break                                   # raises an except on eof
        else:                                       # input given as a string
            num = int(reply)
            print "%d squared is %d" % (num, num ** 2)
    print 'Bye'

#we can run it using "< input.txt"
interact()

