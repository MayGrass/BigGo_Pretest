FROM python:3.10.2

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt


CMD ["scrapy", "crawl", "shopee", "-O", "shopee.csv"]