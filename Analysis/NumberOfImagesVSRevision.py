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

def NumberOfImages(currentText):
    imageFormates = ['.jpg','.jpeg','.svg','.gif','.png','.bmp','.tiff']
    count = 0
    for image in imageFormates:
        count += currentText.count(image)   
    return count



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
                    XML_article_len.append(NumberOfImages(each.text))   



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
                    KML_article_len.append(NumberOfImages(each[0].text))    


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
    plt.ylabel('Number of Images') 
    # giving a title to my graph 
    plt.title('Number of Images vs Revision') 
      
    # show a legend on the plot 
    plt.legend() 

    plt.savefig('AnalysisFigs/Number of Images vs Revision')  
 
    plt.close()
  
    return [start, mid, end]

