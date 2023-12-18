import scrapy
from scrapy import Spider
import json

class GoodreadsSpider(Spider):
    name = "goodreads_spider"
    
    def start_requests(self):
        url = getattr(self, "url", "https://www.goodreads.com")
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        try:
            data = json.loads(response.xpath('//script[@type="application/ld+json"]/text()').get())

            yield {
                "title": data.get("name"),
                "authors": parseAuthors(data),
                "isbn": data.get("isbn"),
                "book_format": data.get("bookFormat"),
                "number_of_pages": data.get("numberOfPages"),
                "language": data.get("inLanguage"),
                "awards": data.get("awards"),
                "rating": data.get("aggregateRating").get("ratingValue"),
                "rating_count": data.get("aggregateRating").get("ratingCount"),
                "review_count": data.get("aggregateRating").get("reviewCount"),
            }
        except:
            print("An error occured while getting data from page.")
        finally:
            anchors = response.css('a::attr(href)').getall()
            for a in anchors:
                if '/book/show' in a:
                    yield response.follow(a, callback=self.parse)

    
def parseAuthors(data):
    authors = []
    for item in data["author"]:
        author = {
            "name": item["name"],
        }
        authors.append(author)
    return authors
