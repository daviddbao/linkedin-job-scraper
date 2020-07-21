# linkedin-job-scraper
Uses Selenium + BeautifulSoup in Python to automatically login to LinkedIn, make a job search, store results (title, company name, location, link to application page) in a CSV file for easy offline tracking

Instructions:
1. Download Selenium, BeautifulSoup, Chrome Webdriver
  a. First two can be pip installed, e.g. "pip install Selenium" on Windows
  b. Third one can be found here: https://chromedriver.chromium.org/
2. Rename "config_sample.py" to "config.py" and fill in inputs
3. Run "python linkedin_scraper.py"
