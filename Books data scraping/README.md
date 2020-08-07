# Book Data Scraping using Python
The code in this notebook is written to automate the process of scraping book's details from a online Turkish book store. However, the approach and underline methods can be used to scrap such data from any websiet of your choice.  

# Tech Stack
Python
Selenium WebDriver 
Beautiful Soup

# Prerequisites 
Python 3.7 
Jupyter Server
Libraries: Selenium.webdriver, BeautifulSoup, matplotlib.pyplot,requests, numpy, json, collection 

# Installation 
I have used chromdriver to make the automated queries to the webpage, install it using following referece link:
[Download WebDriver for Chorme](https://chromedriver.chromium.org/downloads)


Or just update it if you already have it (this command is of Mac, you can easily find for other OSs): 

```brew cask upgrade chromedriver```

You can use following command to install all the other libraries as well using pip:

```pip install -user beautifulsoup4```


**Part1: In the first part, we will scrape a web site.** 

<p>
The web site is "https://www.idefix.com". You will get the information of the books in "Bilim" category.
In short, you can use "https://www.idefix.com/kategori/Kitap/Bilim/grupno=00052?Page=1" as a link.
In the "Bilim" category, there are 2531 books in 71 pages at the time when I'm writing this code
</p>


**Part2: In the second part, you will use statistical and probability tools to understand data.**

<p>
You need the find mean and median and stdev values of the book prices.
You need to draw the histogram of the reviewers' number. Use discrete values such as 10,20 on the x-axis.
You need to find out if there is a relationship between between the book price and the book rate.
You need to find the distribution of the words and the most used word in the book names. You can draw a histogram.
</p>
