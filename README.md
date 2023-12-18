# Goodreads Book Metadata Scraper
This is a web scraper built using the Scrapy framework to extract book metadata from Goodreads book pages. The scraper navigates through Goodreads book pages, retrieving information such as title, author(s), book format, number of pages, etc.


## Installation
1. Clone this repository.
    ```
    git clone https://github.com/noahslik/goodreads-scraper.git
    ```
2. Make sure you have Python installed. If not, download and install Python from python.org.
3. Install Scrapy using pip:
    ```
    cd goodreads-scraper
    pip install scrapy
    ```

## Usage
1. Run the scraper:
    ```
    scrapy crawl goodreads_spider -o output.json
    ```
    The scraped data will be saved in the output.json file in the root directory.
2. By default the scraper starts on the Goodreads homepage. You can set a different starting url like so:
    ```
    scrapy crawl goodreads_spider -o output.json -a url={starting_url}
    ```
    Replace {starting_url} with the URL of the Goodreads page from which you want to begin scraping.
3. Optionally, you can set the maximum amount of requests using the `-s CLOSESPIDER_PAGECOUNT={max_number_of_requests}` option. Example:
    ```
    scrapy crawl goodreads_spider -o output.json -a url={starting_url} -s CLOSESPIDER_PAGECOUNT={max_number_of_requests}
    ```
    Replace {max_number_of_requests} with the maximum amount of requests you want the spider to make.
    
## Data Extracted
The following data is extracted from the book pages:
- Title
- Author(s)
- ISBN
- Book Format
- Number of Pages
- Language
- Awards
- Rating
- Rating Count
- Review Count

## Disclaimer
This scraper is for educational purposes only. Ensure compliance with Goodreads' terms of service and respect website policies while using this tool.
