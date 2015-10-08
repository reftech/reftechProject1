# -*- coding:utf-8 -*-
'''
This program is to download pdfs from different websites.

User need modify three parameter themselves: destinyFile; partA; partC; d1; d2; a

This is the general file. All other download pdf program generated from this one

Kai

'''

import urllib
import urllib2
import re
import datetime
import os

# User can define the file path here

destinyFile = '/Users/Xuan/Desktop/newprogram/'

# This is the main function to get the pdf url and retrieve it

def getPDFFromNet(inputURL, filepath):
    req = urllib2.Request(inputURL)
    f = urllib2.urlopen(req)
    orginalUrlList = []
    newUrlList = []
    for eachLine in f:
        line = eachLine.strip()
        if re.match('.*pdf.*', line):
            wordList = line.split('><img')
            for word in wordList:
                if re.match('.*\.pdf$', word):
                    testlist = word.split('../../../')
                    for pdfList in testlist:
                        if re.match('.*\.pdf$', pdfList):
                            orginalUrlList.append(pdfList)

    for eachUrl in orginalUrlList:
        a = 'http://cswbszb.chinajilin.com.cn/'
        a += eachUrl
        newUrlList.append(a)

    for everyUrl in newUrlList:
        wordItems = everyUrl.split('/')
        for item in wordItems:
            if re.match('.*\.pdf$', item):
                b = wordItems.index(item)
                PDFName = '/' + wordItems[b-1]
                TruePDFName = PDFName + '.pdf'
                localPDF = filepath + TruePDFName
                print localPDF                                    #localPDF is for the ultimate full file path( path+name )
                urllib.urlretrieve(everyUrl, localPDF)

# The following is to find the right main url

##################################################################

partA = 'http://cswbszb.chinajilin.com.cn/html/'
partC = 'node_1.htm'

# partA and partC is the beginning and ending of the url

d1 = datetime.datetime(2015, 8, 2)
d2 = datetime.datetime(2015, 8, 1)

# d1 is for the beginning of the date
# d2 is for the ending of the date

daysCount = (d1 - d2).days
for i in range(0, daysCount + 1):
    d3 = d2 + datetime.timedelta(days=i)
    dyear = '%d' % d3.year
    if d3.month < 10:
        temp = '%d' % d3.month
        dmonth = '0' + temp
    else:
        dmonth = '%d' % d3.month
    if d3.day < 10:
        temp2 = '%d' % d3.day
        dday = '0' + temp2
    else:
        dday = '%d' % d3.day
    tempdyearmonth = dyear + '-'
    truedyearmonth = tempdyearmonth + dmonth
    var_list = [partA, truedyearmonth, dday, partC]
    a = '/'

# The above part is to get the middle part of the url (The datetime part)

    correctUrl = a.join(var_list)
    print correctUrl

# Until this we get correct URL

    var_list2 = [truedyearmonth, dday]
    b = '-'
    filename = b.join(var_list2)
    print filename
    os.mkdir(destinyFile + filename)                                   #To create the folder to store the relevant file
    newFilePath = destinyFile + filename
    print newFilePath
    getPDFFromNet(correctUrl, newFilePath)                             #This is to call getPDFFromNet function

# The above part is to run the function to get the pdf to the filepath