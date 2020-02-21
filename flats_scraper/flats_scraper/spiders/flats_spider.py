import scrapy

class FlatsListSpider(scrapy.Spider):
    name = 'flats_list'
    start_urls = [
        'https://999.md/ro/list/real-estate/apartments-and-rooms?applied=1&ef=32&eo=12900&o_32_8_12900=13859&eo=13859&o_32_9_12900_13859=15672&o_32_9_12900_13859=15665&o_32_9_12900_13859=15666&o_32_9_12900_13859=15664&o_32_9_12900_13859=15669&o_32_9_12900_13859=15673&o_32_9_12900_13859=15670&o_32_9_12900_13859=15667&o_32_9_12900_13859=15671&o_32_9_12900_13859=15668&eo=12912&eo=12885&ef=33&o_33_1=912&o_30_241=893'
    ]

    def parse(self, response):
        flats = response.css('.ads-list-photo-item')
        print(flats)
        for flat in flats:
            yield {
                'title': flat.css('.ads-list-photo-item-title  a::text').get(),
                'description': flat.css('.ads-list-detail-item-intro::text').get(),
                'price': flat.css('.ads-list-photo-item-price-wrapper::text').get()
            }
            # item['title'] = flat.css('.ads-list-detail-item-title  a::text').get(),
            # item['description'] = flat.css('.ads-list-detail-item-intro::text').get(),
            # item['price'] = flat.css('. ads-list-detail-item-price::text').get()
            # yield item
        next_page = response.xpath("//*[contains(@class, 'current')]/following-sibling::li/a/@href").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    