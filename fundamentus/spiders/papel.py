import scrapy


class PapelSpider(scrapy.Spider):
    name = 'papel'
    start_url = 'http://www.fundamentus.com.br/'
    start_urls = [start_url+'detalhes.php/']
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

    def start_requests(self):

        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers)
    def parse(self, response): 

        funds = response.xpath('//*[@id="test1"]/tbody/tr')
        for papel in funds:
            url = self.start_url+papel.xpath('.//a/@href').extract_first()
            #print(url)
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse_detail)

    def parse_detail(self, response):

        papel = response.xpath('/html/body/div[1]/div[2]/table[1]/tr[1]/td[2]/span/text()').extract_first()
        nome = response.xpath('/html/body/div[1]/div[2]/table[1]/tr[3]/td[2]/span/text()').extract_first()
        cotacao  = response.xpath('/html/body/div[1]/div[2]/table[1]/tr[1]/td[4]/span/text()').extract_first()
                                
        #print(title)
        yield {
            'papel': papel,
            'nome': nome,
            'cotacao': cotacao
            
        }
