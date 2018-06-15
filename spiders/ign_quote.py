import scrapy


class IgnSpider(scrapy.Spider):
    name = "ign_spider"
    start_urls = ['http://www.ign.com/xbox-one']

    def parse(self,resposne):
        titles = resposne.xpath(".//div[@class='title']/descendant::text()").extract()
        yield {'ign_spider': ' \n '.join(titles)}