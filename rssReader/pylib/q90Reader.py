
#   Python Responsories
from csv import DictWriter
import time

from os import remove
from PIL import Image
from xml.etree import ElementTree as ET
from urllib.request import urlretrieve

#   Selenium Responsories

import requests

class Q90():

    """         Created following tutorials

            Q9-0 scrapes XML files 
            Working as RSS reader 
    """

    #   Initializing the configurations for Chrome Crawler

    def __init__(self):

                #   File paths
        self.csvPath = 'ScrapingBots/rssReader/docs/CSV/news.csv'
        self.xmlPath = 'ScrapingBots/rssReader/docs/xml/topnewsfeed.xml'

        return

    def LoadXML(self, url):

        """         LoadXML()

                Loading the website,
                writing the website into a file with .xml 

        """

        #   Initializing a connection to the xml file
        req = requests.get(url)

        #   Saving the xml
        with open(f'{self.xmlPath}', 'wb') as f:
            f.write(req.content)

        return

    def praseXML(self):

        """         ParseXML
            Prasing through the xml file 
        """


        #   Initializing the ElementTree
        tree = ET.parse(self.xmlPath)
        rootree = tree.getroot()

        content = []
        unavailable = []

        #   Initializing a Dictionary for the news
        for item in rootree.findall('./channel/item'):
            newsItems = {}

            #   Initializing the child elemets of the content
            for child in item:

                #   Checking for namespace object
                if child.tag == '{http://search.yahoo.com/mrss/}content':

                    newsItems['media'] = child.attrib['url']

                elif child.tag == '{http://www.w3.org/2005/Atom}link' or child.tag == '{http://purl.org/dc/elements/1.1/}creator' or child.tag == '{http://search.yahoo.com/mrss/}credit':
                        pass

                elif child.tag == '{http://search.yahoo.com/mrss/}description' or child.tag == 'guid':
                    pass
                    
                else:

                    newsItems[child.tag] = child.text.encode('utf-8')

            content.append(newsItems)

        #   Saving the xml file as csv
              #   Column names in .csv
        columns = ['category', 'title', 'pubDate', 'description', 'link', 'media']

        with open(self.csvPath, 'w') as csvf:

            author = DictWriter(csvf, fieldnames = columns)
            author.writeheader()
            author.writerows(content)
        
        remove(f'{self.xmlPath}')

        return content

    def SaveCSV(self, content, cvsPath):

        """     SaveCSV
            Saving the items, into CSV file
        """

  
        return

    def openImage(self, url, name):

        #   Downloading image
        urlretrieve(url, name)

        #   Opens the image
        img = Image.open(name)
        img.show()

        return
