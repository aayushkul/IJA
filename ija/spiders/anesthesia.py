# -*- coding: utf-8 -*-
import scrapy


class AnesthesiaSpider(scrapy.Spider):
    name = 'anesthesia'
    allowed_domains = ['ijaweb.org/backissues.asp']
    start_urls = ['http://ijaweb.org/backissues.asp']

    def parse(self, response):
        urls = response.xpath('//a[@title="Table of Contents"]')
        for url in urls:
            issue_url = url.xpath('.//@href').extract_first()
            absolute_url = response.urljoin(issue_url)
            text = url.xpath('.//text()').extract_first()

            yield {'No.': text,
                    'Link': absolute_url}
