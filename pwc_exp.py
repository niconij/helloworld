#!/usr/bin/python
import lxml.etree as ET
import shlex
import subprocess
import sys
import threading

if len(sys.argv)>1:
    print 'We gaan beginnen'
    print sys.argv[1]
    FileName = sys.argv[1]
    Label = sys.argv[2]
else:
    print 'Zo werkt ie niet'
    raise Exception ('Dit is heel erg')
'''
PWCFile will contain the objects
exported from Powercenter in xml-format
'''
class PWCFile:
    def __init__(self, FileName, Label=None):
        self.FileName = FileName
        self.Label = Label
    def exp(self):
        cmd='grep f'
        cmd=shlex.split(cmd)
        print cmd
        e=subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        grep_stdout = e.communicate(input=b'one\ntwo\nthree\nfour\nfive\nsix\n')[0]
        print(grep_stdout.decode())
        cmd='./pmrep.py'
        o=open('output.txt', 'w')
        o.close
        o=open('output.txt', 'a')
        #o = []
        print cmd
        e=subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=o, stderr=subprocess.PIPE, bufsize=0)
        
        
        #e.stdin.write(b'objectexport\n')
        #grep_stdout = e.communicate(input=b'objectexport\n')
        #grep_stdout = e.communicate(input=b'exit\n')
        #print grep_stdout.decode()

        print 'wat is er in output.txt'
        f=open('output.txt','r')
        for line in f:
            print line
        '''for line in e.stdout:
            print line
        e.stdin.write(b'exit\n')
        for line in e.stdout:
            print line
        '''
        e.stdin.write(b'objectexport\n')
        #output=e.stdout.readline().decode()

        #output=e.stdout.readline().decode()
        #print output
        #print e.stdout.readline().decode()
        e.stdin.write(b'objectexport\n')
        #print e.stdout.readline().decode()

##        while True:
##            for line in e.stdout:
##                if  'objectexport' in line:
##                    print 'exporting object'
##                    break
        e.stdin.write(b'exit\n')
        
        o.close
        e.communicate()
        print 'wat is er nu in output.txt'
        with open('output.txt','r') as f:
            for line in f:
                print line
            for value in f.readlines():
                print value

        
    def splits(self):
        print self.Label
        self.Label, self.Version = self.Label.split('#')
        print self.Label
        print self.Version
        


def main():
    p1 = PWCFile(FileName, Label)
    p1.splits()
    p1.exp()
    print 'en nu?'
    with open('/home/nico/Python/output.txt','r') as f:
        for line in f:
            print line
        for value in f.readlines():
            print value    
if __name__ == "__main__":
    main()
    
