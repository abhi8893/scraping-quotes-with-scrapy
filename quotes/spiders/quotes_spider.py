import scrapy
from scrapy.http import FormRequest
from ..items import QuotesItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/login'
    ]
    page_num = 1


    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        data = {
            'username': 'myusername',
            'password': 'supersecretpassword',
            'csrf_token': token
        }

        return FormRequest.from_response(response, formdata=data, callback=self.start_scraping)


    def start_scraping(self, response):
        all_div_quotes = response.css('div.quote')

        item = QuotesItem()

        for quote_info in all_div_quotes:
            item['quote'] = quote_info.css('.text::text').extract()[0]
            item['author'] = quote_info.css('.author::text').extract()[0]
            item['tags'] = quote_info.css('.tag::text').extract()
            item['page_num'] = self.page_num

            yield item

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            self.page_num += 1
            yield response.follow(next_page, callback=self.start_scraping)


    