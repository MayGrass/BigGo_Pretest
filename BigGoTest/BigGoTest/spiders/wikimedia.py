import scrapy
import json


class WikimediaSpider(scrapy.Spider):
    name = "wikimedia"
    allowed_domains = ["doc.wikimedia.org"]
    start_urls = ["https://doc.wikimedia.org/mediawiki-core/REL1_31/php/ZhConversion_8php_source.html"]

    def parse(self, response):
        output_dict = dict()

        php_code = response.css(".fragment .line")
        for zh2Hant in php_code:
            if text := zh2Hant.css(".stringliteral::text").getall():
                output_dict[text[1].replace("'", "")] = text[0].replace("'", "")

        with open("zh2Hant.json", "w", encoding="utf-8") as f:
            json.dump(output_dict, f, ensure_ascii=False)
