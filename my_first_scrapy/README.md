# introduction
This is a demo scrapy project ,which is to crawl movie leaderboard from Douban .
# The main operation
1. Create item
2. Create spider-> extract data from html -> convert source data to the item created above
3. Exec command to start crawl
# Tips
The entrypoint.py is the main function for debugging in IDE

# User Guide
```python
# use case 1
    #movie top list
    scrapy crawl doubanTop250 -o douban.csv
    #books top list
    scrapy crawl doubanBookTop250 -o douban_book.csv
# use case 2 --------- just run the entrypoint.py
```