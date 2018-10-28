## Airbnb Spider

### How to run

First time:
`pip install scrapy`

Inside this repo,
`scrapy crawl listing -a query=Austin -o Austin.json`

This is the same as searching "Austin" in the airbnb website and store the raw API result in Austin.json (might contain duplicates)

### Samples

- RAW json data from the API: test.json
- Generated result from scrapy: Austin.json 

### Note
This module might not be able to exhaust all the listing in the scrapy database, you can specify zipcode / subarea of a city to get more results.