import json
from pprint import pprint

import scrapy
from scrapy.crawler import CrawlerProcess

import wget

import os

path = os.getcwd()

def LowLevelDownload(DownLink='',SavPath=''):
    PrograssDownload = wget.download(DownLink, SavPath)
    print('Finished download: ', PrograssDownload)

def CrawlSubLevel(Link=None):

    class CrawlList(scrapy.Spider):
        name = 'sublist'
        start_urls = Link

        def parse(self, response):
            capture = response.css('table')
            tag = response.xpath('body/div/div/a/text()')[2].extract()
            os.mkdir(tag)
            for filelst in capture.css('td'):
                if filelst.xpath('a/@href').extract_first() != None:
                    FullDownloadURL = 'http://kitsunekko.net/'+filelst.xpath('a/@href').extract_first()
                    print('===============================Test============: - ',tag)
                    print(FullDownloadURL)
                    LowLevelDownload(FullDownloadURL,path+'\\'+tag+'\\')
    
    process = CrawlerProcess(
        settings={
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            'LOG_LEVEL': 'CRITICAL'
        }
    )

    process.crawl(CrawlList)
    process.start()


def ReadJson():
    with open('AnimeRawList.json') as jsonfile:
        content = json.load(jsonfile)
    return content

if __name__ == "__main__":
    DownloadList = []
    for JsonObj in ReadJson():
        if 'zip' in JsonObj['title'][0] or 'rar' in JsonObj['title'][0] :
            continue
        else:
            print(JsonObj['URL'], " | ", JsonObj['title'][0])
            FullURL = 'http://kitsunekko.net'+JsonObj['URL']
            DownloadList.append(FullURL)
    #print(DownloadList)
    CrawlSubLevel(DownloadList)