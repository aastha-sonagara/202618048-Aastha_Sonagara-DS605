import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    custom_settings = {
        "FEEDS": {
            "../../data/books.csv": {
                "format": "csv",
                "overwrite": True,
            }
        },
        "FEED_EXPORT_ENCODING": "utf-8",
        "DOWNLOAD_DELAY": 1,
        "ROBOTSTXT_OBEY": True,
    }

    book_count = 0
    max_books = 100

    def parse(self, response):

        books = response.css("article.product_pod")

        for book in books:

            if self.book_count >= self.max_books:
                return

            product_url = response.urljoin(
                book.css("h3 a::attr(href)").get()
            )

            yield scrapy.Request(
                product_url,
                callback=self.parse_book,
            )

            self.book_count += 1

        next_page = response.css("li.next a::attr(href)").get()

        if next_page and self.book_count < self.max_books:

            next_page = response.urljoin(next_page)

            yield scrapy.Request(
                next_page,
                callback=self.parse,
            )

    def parse_book(self, response):

        title = response.css("div.product_main h1::text").get()

        price = response.css("p.price_color::text").get()

        availability = (
            response.css("p.availability::text")
            .getall()
        )

        availability = "".join(availability).strip()

        rating = response.css(
            "p.star-rating::attr(class)"
        ).get()

        rating = rating.replace("star-rating", "").strip()

        description = response.css(
            "#product_description + p::text"
        ).get()

        upc = response.xpath(
            '//th[text()="UPC"]/following-sibling::td/text()'
        ).get()

        category = response.xpath(
            '(//ul[@class="breadcrumb"]/li/a/text())[3]'
        ).get()

        reviews = response.xpath(
            '//th[text()="Number of reviews"]/following-sibling::td/text()'
        ).get()

        yield {

            "Title": title,

            "Category": category,

            "Price": price,

            "Rating": rating,

            "Availability": availability,

            "Product Description": description,

            "UPC": upc,

            "Number of Reviews": reviews,

            "Product URL": response.url,

        }