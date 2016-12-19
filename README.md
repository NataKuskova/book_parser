This application was built on Python 3.5 using Scrapy 1.2.2

To run the application, you must create a virtual environment and set the requirements.
To install this requirement you need to run the command: 
"pip install -r requirements.txt"

To run the scrapy you need to run the command:
"scrapy crawl buchreport_spider"

Spider goes through all pages and parses the following information about the books and stores them in a file - "items.json":<br>
- The position at the top of best-seller;<br>
- Book author;<br>
- The title of the book;<br>
- Book Cover;
