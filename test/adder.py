import sys
sum = 0
while True:
    try:
        line = raw_input()                 # or call sys.stdin.readlines( )
    except EOFError:                       # or for line in sys.stdin:
        break                              # raw_input strips \n at end
    else:
        sum += int(line)                   # was sting.atoi( ) in 2nd ed
print sum

