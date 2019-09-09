import scrapy
from scrapy.crawler import CrawlerProcess

URLs = []

for i in range(1,100,1):
    URLs.append('https://nyaa.si/?f=0&c=1_4&p='+str(i))


class CrawlRAWAnimeList(scrapy.Spider):
    name = 'animelist'
    start_urls = URLs

    def parse(self, response):
        capture = response.css('tbody')
        for animelst in capture.css('tr'):
            print('==================Checkpoint =========')
            if animelst.xpath('td/a/text()').extract_first() != None:
                yield {
                    'NAME': animelst.xpath('td/a/text()')[-1].extract(),
                    'TorrentURL': animelst.xpath('td/a/@href')[-2].extract(),
                    'Magnet': animelst.xpath('td/a/@href')[-1].extract()
                }

if __name__ == '__main__':
    process = CrawlerProcess(
        settings={
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            'LOG_LEVEL': 'CRITICAL',
            'FEED_FORMAT': 'json',
            'FEED_URI': 'RawAnimeTorrentList.json'
        }
    )
    process.crawl(CrawlRAWAnimeList)
    process.start()