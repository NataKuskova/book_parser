import scrapy
from book_parser.items import BookParserItem


class BuchreportSpider(scrapy.Spider):
    name = 'buchreport_spider'
    allowed_domains = ['buchreport.de']
    start_urls = [
        'https://www.buchreport.de/spiegel-bestseller/hardcover/']

    def parse(self, response):
        books = response.xpath(
            '//div[contains(@class, "bestseller-list-row")]')

        for book in books:
            if not book.xpath('div[contains(@class, "information")]'):
                continue
            item = BookParserItem()
            item['position'] = book.xpath(
                './/div[contains(@class, "bestseller-list-book-position")]'
                '/text()').extract_first().strip()
            item['author'] = book.xpath(
                './/div[contains(@class, "author")]'
                '/text()').extract_first().strip()
            item['title'] = book.xpath(
                './/div[contains(@class, "title")]/a'
                '/text()').extract_first().strip()
            item['image'] = book.xpath(
                './/img[contains(@class, "bestseller-list-image-bookcover")]'
                '/@src').extract_first()
            yield item

        next_page = response.xpath(
            '//a[contains(@class, "bestseller-list-button") and '
            'contains(@class, "active")]/following-sibling::a'
            '/@href').extract_first()

        if next_page:
            url = response.urljoin(self.start_urls[0] + next_page)
            yield scrapy.Request(url, self.parse)