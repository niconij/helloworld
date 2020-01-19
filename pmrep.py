#!/usr/bin/python
import sys

def objectexport(*argv):
    print 'performing objectexport with ' , argv
    print 'checking list'
    for c in argv:
        print 'this is a',c
    print 'hmpf'
    string=''
    for i in range(len(argv)):
        if i == 0:
            string = argv[i]
        else:
            string += ' ' + argv[i]
    print 'string:',string

class pmrep:
    def __init__(self, function, *argv):
        self.function = function
        self.argv = argv
        if function == 'objectexport':
            objectexport(argv)
        if function == 'help':
            print 'Read the manual'
        
if __name__ == "__main__":
    if len(sys.argv)>1:
        x = pmrep(sys.argv[1], sys.argv[2:])
        #print x.function
        #print x.argv
    else:
        c = raw_input('pmrep command to perform: ')
        while True:
            if c.strip() == 'exit':
                print 'exit'
                break
            elif 'objectexport' in c:
                print 'objectexport'
            else:
                print 'whateffa', c
                break

        
