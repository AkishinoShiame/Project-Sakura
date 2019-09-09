import scrapy
from scrapy.crawler import CrawlerProcess

class CrawlAnimeList(scrapy.Spider):
    name = 'animelist'
    start_urls = [
        'http://kitsunekko.net/dirlist.php?dir=subtitles%2Fjapanese%2F',
    ]

    def parse(self, response):
        capture = response.css('table')
        for animelst in capture.css('td'):
            print('==================Checkpoint =========\n', animelst)
            if animelst.xpath('a/@href').extract_first() != None:
                yield {
                    'URL': animelst.xpath('a/@href').extract_first(),
                    'title': animelst.css('strong::text').extract()
                }

if __name__ == '__main__':
    process = CrawlerProcess(
        settings={
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            'FEED_FORMAT': 'csv',
            'FEED_URI': 'AnimeRawList.csv'
        }
    )
    process.crawl(CrawlAnimeList)
    process.start()