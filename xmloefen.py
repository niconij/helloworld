#!/usr/bin/python
import json
import lxml.etree as ET
import pprint
import simplejson
import sys
import xmltodict
import xmljson


class Person:
    def __init__(self, fname):
        self.fname = fname

class Vader(Person):
    def __init__(self, fname):
        Person.__init__(self, fname)
        self.vadervan = kinderen

    
def main():
    if len(sys.argv)>1:
        print 'We gaan beginnen'
        print sys.argv[1]
    else:
        print 'Zo werkt ie niet'
        raise Exception ('Dit is heel erg')
    doc = ET.Element(sys.argv[1])
    subelement = ET.SubElement(doc, 'Vader', name='Nico', lastname='Nijenhuis', birthplace='Assen'').text = 'Komt uit Assen'
    subelement = ET.SubElement(doc, 'Moeder', name='Astrid', lastname='Roelands').text = 'Komt uit Emmeloord'
    subelement = ET.SubElement(doc, 'Kind', name='Iyan', lastname='Nijenhuis').text = 'Lentenaar'
    tree=ET.ElementTree(doc)
    with open('output.xml', 'w') as myfile:
              ET.ElementTree(doc).write(myfile, encoding='utf-8', xml_declaration = True, pretty_print = True)

    with open('output.xml') as myfile:
        jdoc = xmltodict.parse(myfile.read())
    ET.dump(doc)
    print 'jdoc xxx' 
    print jdoc['xxx']
    print 'jdoc xxx Kind'
    print jdoc['xxx']['Kind']
    print 'alles in JSON'
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(json.dumps(jdoc))


if __name__ == "__main__":
    main()
