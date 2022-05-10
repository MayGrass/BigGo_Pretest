# BigGo python developer pretest

#### Q1

- Try to finish this project via Python:
  Use below Wikipedia Simplified / Traditional Chinese conversion tables to **create** a Python converter(Create it yourself, Do not use the third-party opensource convert library).

  > https://doc.wikimedia.org/mediawiki-core/REL1_31/php/ZhConversion_8php_source.html

- Then you need to write a crawler that will get the product title and price from every page in this EC catalog and use the above-mentioned converter table to perform the conversion from traditional Chinese to simplified Chinese.

  > https://shopee.tw/%E5%A8%9B%E6%A8%82%E3%80%81%E6%94%B6%E8%97%8F-cat.11041645

#### Q2

- Suppose you are given the following code:

  ```python
  class FooBar():
      def __init__(self, n):
              self.n = n
  
      def foo(self):
          for _ in range(self.n)
          	print("foo")
  
      def bar(self):
          for _ in range(self.n)
          	print("bar")
  
      def yeah(self):
          for _ in range(self.n)
          	print("yeah")
  ```

  The same instance of FooBar will be passed to two different threads:

  \* thread A will call foo(), while

  \* thread B will call bar(),

  \* thread c will call yeah(),

  Modify the given program to output "foobaryeah" n times.

  

  Input: n = 3

  Output:

  ​    foobaryeah

  ​    foobaryeah

  ​    foobaryeah

------

##### Q1 Usage

```bash
docker-compose up
```

After finish, it will output a file, shopee.csv

**NOTE:** Only 34 products on 76 page

##### TestLog

```json
{"downloader/request_bytes": 85772,
 "downloader/request_count": 100,
 "downloader/request_method_count/GET": 100,
 "downloader/response_bytes": 5378788,
 "downloader/response_count": 100,
 "downloader/response_status_count/200": 100,
 "elapsed_time_seconds": 4.523218,
 "feedexport/success_count/FileFeedStorage": 1,
 "finish_reason": "finished",
 "finish_time": datetime.datetime(2022, 5, 4, 11, 17, 40, 284826),
 "httpcompression/response_bytes": 24560026,
 "httpcompression/response_count": 100,
 "item_scraped_count": 5974,
 "log_count/DEBUG": 6079,
 "log_count/INFO": 11,
 "memusage/max": 70782976,
 "memusage/startup": 70782976,
 "response_received_count": 100,
 "scheduler/dequeued": 100,
 "scheduler/dequeued/memory": 100,
 "scheduler/enqueued": 100,
 "scheduler/enqueued/memory": 100,
 "start_time": datetime.datetime(2022, 5, 4, 11, 17, 35, 761608)}
```

