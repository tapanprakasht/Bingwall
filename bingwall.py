__author__ = 'tapan'

# Bingwall is a program to fetch daily Bing wallpapers

from urllib.request import urlopen
from xml.dom.minidom import parseString
import re
import os
import sys

class Bingwall:
    def __init__(self):
        pass
        self.imageurl = ''

    def getLink(self):
        try:
            print("Fetching image links....")
            url = "http://feeds.feedburner.com/bingimages"
            xmlfile = urlopen(url)
            data = xmlfile.read()
            xmlfile.close()
            dom = parseString(data)
            xmlTag = dom.getElementsByTagName('description')[1].toxml()
            xmldata = xmlTag.replace('<description>', '').replace('</description>', '')
            getimageurl = re.search('src=&quot;(.*).jpg', xmldata)
            self.imageurl = getimageurl.group(1) + '.jpg'
            print("Image link")
            print(self.imageurl)
        except:
            print("\033[31mFetching image link failed.\033[0m")

    def getImage(self):

        filename = re.search('cache/(.*)', self.imageurl).group(1)

        try:
            if not os.path.exists(os.path.expanduser("~/Pictures/") + filename):
                fh = open(os.path.expanduser("~/Pictures/") + filename, 'wb')
                print("Filename:"+filename)
            else:
                print("\033[31mFile already exists\033[0m")
                sys.exit(0)
        except:
            print("\033[31mOpening file for writing failed!\033[0m")
            sys.exit()
        try:
            imagefile = urlopen(self.imageurl)
            data = imagefile.read()
            fh.write(data)
            print("Bing image fetching finished.")
        except:
            print("\033[31mOpening URL failed!\033[0m")


def main():
    b = Bingwall()
    b.getLink()
    b.getImage()


if __name__ == "__main__": main()
