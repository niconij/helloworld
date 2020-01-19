#!/usr/bin/python
import sys
class Backup:
    def __init__(self, keep):
        self.keep = keep

    def parms(self):
        print 'Number of backups to keep', self.keep

    def fnct(self):
        return self.keep

SVN = Backup(8)
SVN.parms()
print SVN.fnct()+3


