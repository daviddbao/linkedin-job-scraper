# linkedin-job-scraper
Uses Selenium + BeautifulSoup in Python to automatically login to LinkedIn, make a job search based on your inputs in a config.py file, and store the results (title, company name, location, link to application page) in a CSV file for easy offline tracking of your jobs and applications. Made this small project to learn a little about web scraping, headless browsers, front-end, and git.

Instructions:
1. Download Selenium, BeautifulSoup, and Chrome Webdriver. The first two can be pip installed, e.g. "pip install selenium" on Windows. The third one can be found here: https://chromedriver.chromium.org/
2. Rename "config_sample.py" to "config.py" and fill in inputs
3. Run "python app.py"

Script fully working as of 7/21/20. Was going to continue to make more improvements and possibly expand the project, but started running into LinkedIn's bot detection.
