# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.http import Request

class AbstractSpider(Spider):
    name = 'abstract'
    allowed_domains = ['ijaweb.org']
    start_urls = ['http://ijaweb.org/showBackIssue.asp?issn=0019-5049;year=2018;volume=62;issue=11;month=November']

    def parse(self, response):
        links = response.xpath('//*[@title="Click to View ABSTRACT of the article."]/@href').extract()
        for link in links:
            absolute_url = 'http://www.ijaweb.org/' + link
            yield Request(absolute_url, callback = self.parse_issue)

    def parse_issue(self,response):
        title = response.xpath('//*[@class="sTitle"]/text()').extract_first()
        author = response.xpath('//*[@class="articleAuthor"]/a/text()').extract()
        type = response.xpath('//*[@class="tocAT"]/b/text()').extract_first()
        abstr = response.xpath('//table[@class="articlepage"]/tr/td/text()').extract()[7]
        full_text_url = response.xpath('//a[text()="FULL TEXT"]/@href').extract_first()
        absolute_full_text_url = 'http://www.ijaweb.org/' + full_text_url

        yield {
        'Title': title,
        'Author': author,
        'Article Type': type,
        'Abstract': abstr,
        'Full Text Link': absolute_full_text_url,
        }
