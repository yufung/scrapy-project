# Scraping Food Items

A quick scrapy project to get food items from restaurants from http://chubbygrub.com/.

## Extracted data

This project extracts food name, category, calories, carbs and fat from every restaurant. The extracted data looks like this sample:

restaurant|category|name|calories|carbs|fat
-|-|-|-|-|-
Chipotle Mexican Grill|Entrees|Barbacoa|170|2|7
Chipotle Mexican Grill|Entrees|Barbacoa|60|1|2.5
Chipotle Mexican Grill|Sides|Black Beans|120|23|1

## Spiders

This project contains 1 spider and you can list it using the `list` command:

    $ scrapy list
    chubbygrub

## Running the spider

You can run a spider using the `scrapy crawl` command:

    $ scrapy crawl chubbygrub

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl chubbygrub -o food.csv

## Requirements

* Python
* Scrapy
