import scrapy


class IgnSpider(scrapy.Spider):
    name = "ign_spider"
    start_urls = ['https://www.reddit.com/r/todayilearned']

    def parse(self,resposne):
        titles = resposne.xpath(".//div[@class='title']/descendant::text()").extract()
        yield {'ign_spider': ' \n '.join(titles)}