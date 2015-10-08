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

# destinyFile = '/Users/Xuan/Desktop/newprogram/'  This is for Mac OS

destinyFile = 'F:\downloadPDF\\temp\\'
trueUrlAAlist = []

# This is the main function to get each article url and retrieve it

def getArticleFromNet(inputURL):
    req = urllib2.Request(inputURL)
    f = urllib2.urlopen(req)
    html = f.read()
    Newhtml = unicode(html,"gb2312").encode("utf-8")
    FinalIndexUrlList = []
    FinalArticleUrlList = []
    a = re.findall(r'\bonclick=window\.open(\S*)',Newhtml)
    string_convert_a = ''.join(a)
    allUrl = re.findall(r'(\w*\.html)',string_convert_a)
    string_convert_b = ''.join(allUrl)
    indexUrl = re.findall(r'(lnrb\w{2,3}\.html|index.html)',string_convert_b)

    for eachUrl in indexUrl:
        urlpartA = 'http://epaper.lnd.com.cn/html/lnrb'
        trueindexUrl = [urlpartA, truedyearmonths, eachUrl]
        a = '/'
        finalindexUrl = a.join(trueindexUrl)
        FinalIndexUrlList.append(finalindexUrl)


    for everyUrl in FinalIndexUrlList:
        req2 = urllib2.Request(everyUrl)
        f2 = urllib2.urlopen(req2)
        html2 = f2.read()
        Newhtml2 = unicode(html2,"gb2312").encode("utf-8")
        a2 = re.findall(r'\bonclick=window\.open(\S*)',Newhtml2)
        string_convert_a2 = ''.join(a2)
        allUrl2 = re.findall(r'(\w*\.html)',string_convert_a2)
        string_convert_b2 = ''.join(allUrl2)
        articleUrl2 = re.findall(r'(lnrb\w{4,8}\.html)',string_convert_b2)

        for eachUrl in articleUrl2:
            trueindexUrl2 = [urlpartA, truedyearmonths, eachUrl]
            FinalArticleUrl = a.join(trueindexUrl2)
            print FinalArticleUrl
            localPath = FileFolderName + '\\' + eachUrl
            print 'Now Saving File to ' + FileFolderName
#            urllib.urlretrieve(FinalArticleUrl, localPath)

d11 = datetime.datetime(2015, 9, 14)
d22 = datetime.datetime(2015, 9, 12)

daysCount = (d11 - d22).days
for i in range(0, daysCount + 1):
    d33 = d22 + datetime.timedelta(days=i)
    dyear = '%d' % d33.year
    if d33.month < 10:
        temp = '%d' % d33.month
        dmonth = '0' + temp
    else:
        dmonth = '%d' % d33.month
    if d33.day < 10:
        temp2 = '%d' % d33.day
        dday = '0' + temp2
    else:
        dday = '%d' % d33.day
    tempdyearmonths = dyear + dmonth
    truedyearmonths = tempdyearmonths + dday
    FileFolderName = destinyFile + truedyearmonths
#    os.mkdir(FileFolderName)
    urlpartAA = 'http://epaper.lnd.com.cn/html/lnrb'
    urlpartCC = 'index.html'
    trueUrlAA = [urlpartAA, truedyearmonths, urlpartCC]
    m = '/'
    UrlAA = m.join(trueUrlAA)
    getArticleFromNet(UrlAA)



