# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy

class ChubbyGrubSpider(scrapy.Spider):
    name = "chubbygrub"
    allowed_domains = ["chubbygrub.com"]
    start_urls = [
        "http://chubbygrub.com/"
    ]

    def parse(self, response):
        # follow links to restaurant pages
        for href in response.xpath('/html/body/div[4]/div/div/div//@href').getall():
            yield response.follow(href, self.parse_food)

    def parse_food(self, response):
        for foods in response.xpath('/html/body/div[2]/div[3]/div/table/tbody/tr'):
            yield {
                'calories': foods.xpath('./td[3]/text()').get(),
                'carbs': foods.xpath('./td[5]/text()').get(),
                'category': foods.xpath('./td[2]/a/text()').get(),
                'fat': foods.xpath('./td[4]/text()').get(),
                'name': foods.xpath('./td[1]/text()').get(),
                'restaurant': response.xpath('/html/body/div[2]/div[1]/div/div/h1/span/text()').get()
            }