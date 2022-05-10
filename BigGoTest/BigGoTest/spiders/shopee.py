import scrapy
from BigGoTest.items import ShopeeItem


class ShopeeSpider(scrapy.Spider):
    name = "shopee"
    allowed_domains = ["shopee.tw"]

    def start_requests(self):
        page = 0  # 第一頁從0開始
        # 最多一百頁
        while page < 100:
            url = f"https://shopee.tw/api/v4/search/search_items?by=pop&fe_categoryids=11041645&limit=60&newest={page * 60}&order=desc&page_type=search&scenario=PAGE_OTHERS&version=2"
            yield scrapy.Request(
                url,
                callback=self.parse,
                headers={
                    "x-api-source": "pc",  # 不加會導致資料與電腦版本不同
                },
                errback=self.errback,
                dont_filter=True,
            )
            page += 1

    def parse(self, response):
        item = ShopeeItem()

        response_json = response.json()

        for product in response_json["items"]:
            item_basic = product["item_basic"]
            item["name"] = item_basic["name"]
            item["price"] = str(
                f"{item_basic['price_min']} - {item_basic['price_max']}"
                if item_basic["price_min"] != item_basic["price_max"]
                else item_basic["price"]
            ).replace("00000", "")

            yield item

    def errback(self, failure):
        # log all failures
        self.logger.error(repr(failure))
