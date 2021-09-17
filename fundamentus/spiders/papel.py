import scrapy


class PapelSpider(scrapy.Spider):
    name = 'papel'
    
    start_urls = ['http://www.fundamentus.com.br/']

    def parse(self, response):
        pass
