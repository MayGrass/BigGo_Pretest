# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pygtrie
import json


class Zh2HantPipeline:
    def open_spider(self, spider):
        with open("zh2Hant.json", "r") as f:
            zh2Hant_dict = json.load(f)
        # 建立分詞字典
        self.trie = pygtrie.CharTrie()
        for traditional, simplified in zh2Hant_dict.items():
            self.trie[traditional] = simplified

    def process_item(self, item, spider):
        simplified_chinese = str()
        traditional_chinese = item["name"]

        while traditional_chinese:
            longest_prefix = self.trie.longest_prefix(traditional_chinese)  # 用最長前綴來比對

            # 如果有找到前綴，就把前綴刪掉，並加入簡化字串
            if longest_prefix:
                simplified_chinese += longest_prefix.value
                traditional_chinese = traditional_chinese[len(longest_prefix.key) :]
            # 如果沒有找到前綴，就把現在的字元加入簡化字串，並刪除現在的第一個字元
            else:
                simplified_chinese += traditional_chinese[0]
                traditional_chinese = traditional_chinese[1:]

        item["name"] = simplified_chinese
        return item
