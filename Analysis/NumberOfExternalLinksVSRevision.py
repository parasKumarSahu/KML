import xml.etree.cElementTree as ec
import numpy as np
import os
import matplotlib.pyplot as plt
import mwparserfromhell
import time


path = "/home/paras/KML/resources/Indian Institute of Technology Ropar.xml"
path2 = "/home/paras/KML/compressed-KML/compressedIIT.kml"

XML_article_len = []
KML_article_len = []


def ArticleLength(articleName):
    tree = ec.parse(articleName) 
    root = tree.getroot()

    sizeOfArticle = 0
    pageElement = root[1]
    total = 0
    reverts = {}
    contributors = {}

    for child in pageElement:
        if 'revision' in child.tag:
            for each in child:
                if 'text' in each.tag:
                    wikicode = mwparserfromhell.parse(each.text)
                    count = 0
                    for each in wikicode.filter_external_links():
                        count += 1
                    XML_article_len.append(count)   



def ArticleLengthKML(articleName):
    tree = ec.parse(articleName) 
    root = tree.getroot()

    sizeOfArticle = 0
    pageElement = root[0]
    total = 0
    reverts = {}
    contributors = {}

    for child in pageElement:
        if 'Instance' in child.tag:
            for each in child:
                if 'Body' in each.tag:
                    wikicode = mwparserfromhell.parse(each[0].text)
                    count = 0
                    for each in wikicode.filter_external_links():
                        count += 1
                    KML_article_len.append(count)   


def main(x, y):
    start = time.time()
    ArticleLength(x)
    mid = time.time()
    ArticleLengthKML(y)
    end = time.time()
    # line 1 points 
    y1 = XML_article_len 
    x1 = [i+1 for i in range(len(XML_article_len))] 
    # plotting the line 1 points  
    plt.plot(x1, y1, label = "XML") 
      
    # line 2 points 
    y2 = KML_article_len 
    x2 = [i+1 for i in range(len(KML_article_len))] 
    # plotting the line 2 points  
    plt.plot(x2, y2, label = "KML", linestyle='dashed') 
      
    # naming the x axis 
    plt.xlabel('Revision number') 
    # naming the y axis 
    plt.ylabel('Number of External Links ') 
    # giving a title to my graph 
    plt.title('Number of External Links vs Revision') 
      
    # show a legend on the plot 
    plt.legend() 
 
    plt.savefig('AnalysisFigs/Number of External Links vs Revision')  

    plt.close()
      
    return [start, mid, end]

