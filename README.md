# Scraping Quotes with scrapy

This is a Scrapy project to scrape quotes from famous people from [http://quotes.toscrape.com](http://quotes.toscrape.com/) 

Followed the [Python Scrapy tutorial](https://www.youtube.com/playlist?list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t) on youtube

## Extracted Data
The we scraper iteratively scraps the entire 10 pages, and extracts the info about the quote as follows:

```
{
	 'author': 'J.R.R. Tolkien',
	 'page_num': 7,
	 'quote': '“Not all those who wander are lost.”',
	 'tags': ['bilbo', 'journey', 'lost', 'quest', 'travel', 'wander']
}

```
- I have used a mix of `XPATH` and `CSS` selectors to achieve the results.
- The default setting of the scraper stores the extracted data in a `MongoDB` database. (You will need to set it up for your system)
- However I have also implemented the pipeline using `sqlite3` and `MySQL` (using `python-mysql-connector` api)
- The appropriate Pipeline for the database can be changed in the `settings.py` file


Offical scrapy tutorial - [Scrapy Tutorial](http://doc.scrapy.org/en/latest/intro/tutorial.html).


## Clone the repository
```
$ git clone git@github.com:abhi8893/scraping-quotes-with-scrapy.git
```
## Install the required packages
```
$ cd git@github.com:abhi8893/scraping-quotes-with-scrapy.git
$ pip install -r requirements.txt
```
## Running the spider

You can run a spider using the `scrapy crawl` command as follows:

```
$ scrapy crawl quotes
```
## Saving to a file 

To save the scraped data to a file, you can pass the `-o` option and specify the output extension as `.csv`, `.json`, or `.xml`:

```
$ scrapy crawl quotes -o output/quotes.csv
```