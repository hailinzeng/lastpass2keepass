#!/usr/bin/python

import csv
import sys

class lastpassdb:
    db = []

    def __init__(self, filepath):
        self.db = []
        self.fromcsv(filepath)

    def fromcsv(self, filepath):
        '''
        format:
        url, username, password, extra, name, grouping, fav
        xxx, xxx, ...
        '''
        with open(filepath, 'rb') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                (url, username, password, extra, name, grouping, fav) = tuple(row)
                self.db.append(tuple(row))
                #print url


    def exportxml(self):
        '''
        to keepass xml format
        '''
        print "<!DOCTYPE KEEPASSX_DATABASE>\n"\
              "<database>\n"
        print "  <group>\n"\
              "  <title>LastPass</title>\n"\
              "  <icon>48</icon>"
        for item in self.db:
            (url, username, password, extra, name, grouping, fav) = item 
            print "  <entry>\n"\
                  "    <title>%s</title>\n"\
                  "    <username>%s</username>\n"\
                  "    <password>%s</password>\n"\
                  "    <url>%s</url>\n"\
                  "    <comment>%s</comment>\n"\
                  "    <icon>48</icon>\n"\
                  "    <expire>Never</expire>\n"\
                  "  </entry>" % (name, username, password, url, extra)
        print "  </group>"
        print "</database>"

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print "Usage : python lastpassdb.py csv_file"
        exit(0)
    filepath = sys.argv[1]

    lpdb = lastpassdb(filepath)
    lpdb.exportxml()
        
