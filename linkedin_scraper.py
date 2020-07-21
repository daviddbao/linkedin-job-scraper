from config import credentials, params
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import datetime
import math

driver = webdriver.Chrome(credentials["driverpath"])
linkedin_url = 'https://www.linkedin.com'
driver.get(linkedin_url)

driver.find_element_by_class_name('nav__button-secondary').click()
sleep(1)

username = driver.find_element_by_id('username')
username.send_keys(credentials["username"])
sleep(1)
password = driver.find_element_by_id('password')
password.send_keys(credentials["password"], Keys.RETURN)
sleep(4)

#click jobs tab on homepage
driver.find_element_by_id('jobs-nav-item').click()
sleep(4)


# Finds the main search input - title, skill, or company recommended
role = driver.find_elements_by_class_name('jobs-search-box__text-input')[0]
role.send_keys(params["Query"])
sleep(1)

# search location input box
location = driver.find_elements_by_class_name('jobs-search-box__text-input')[2]
location.send_keys(params["Location"], Keys.RETURN)
sleep(4)

#further job filtering - first find and click "All filters"
filter_button = driver.find_element(by='xpath', value='/html/body/div[8]/div[3]/div[2]/section/div/div/button')
filter_button.click()
sleep(2)

#unsure where to find exact xpath for filters, trial and error after reading tutorial
#Date Posted filter - ///span[2] corresponds to the index-1 (2nd) choice
date_posted = driver.find_element(by='xpath', value='(//*[@class="ember-view"]/ul/li[2]/label/p/span[2])[1]')
date_posted.click()
sleep(1)

#full-time filter
job_type = driver.find_element(by='xpath', value='(//*[@class="ember-view"]/ul/li[1]/label/p/span[1])[5]')
job_type.click()
sleep(1)

#entry level filter -- ///span[1] corresponds to the index-1 (2nd) choice
entry_level = driver.find_element(by='xpath', value='(//*[@class="ember-view"]/ul/li[2]/label/p/span[1])[10]')
entry_level.click()
sleep(1)

#click Apply when done applying filters
apply_button = driver.find_element(by='xpath', value='/html/body/div[4]/div/div/div[1]/div/div[2]/button[2]')
apply_button.click()
sleep(2)

num_results = driver.find_element(by='xpath', value='/html/body/div[8]/div[3]/div[2]/div[2]/div/div/section/header/div[1]/small').text
num_results = int(num_results[:-8])
pages = math.ceil(num_results / 25)

soup = BeautifulSoup(driver.page_source)
today = str(datetime.date.today().strftime("%b-%d-%Y"))

filename = "jobs_" + today + ".csv"
f = open(filename, "w")
headers = "Title, Company, Location, Link\n"
f.write(headers)

for tag in soup.findAll('div', {"data-test-job-card-container":"true"}):
	job_container = tag.find('div', attrs={'class':"flex-grow-1 artdeco-entity-lockup__content ember-view"})
	job_title = job_container.find('a').text.replace(',', ' -').replace('\n', "")
	job_link = linkedin_url + job_container.find('a')['href']
	company_container = job_container.find('div', attrs={'class':"artdeco-entity-lockup__subtitle ember-view"})
	company_name = company_container.find('a').text.replace(',', ' -').replace('\n', "")
	location = job_container.find('div', attrs={'class':"artdeco-entity-lockup__caption ember-view"}).text.replace(',', ' /').replace('\n', "")

	f.write(job_title + ',' + company_name + ',' + location + ',' + job_link + '\n')
f.close()

#Iterating through each job posting on a page
# def job_page_iter(page_source, f):
# soup = BeautifulSoup(driver.page_source)
# for tag in soup.findAll('div', {"data-test-job-card-container":"true"}):
# 	job_container = tag.find('div', attrs={'class':"flex-grow-1 artdeco-entity-lockup__content ember-view"})
# 	job_title = job_container.find('a').text
# 	job_link = job_container.find('a')['href']
# 	company_container = job_container.find('div', attrs={'class':"artdeco-entity-lockup__subtitle ember-view"})
# 	company_name = company_container.find('a').text
# 	location = job_container.find('div', attrs={'class':"artdeco-entity-lockup__caption ember-view"}).text

# 	f.write(job_title + ',' + company_name + ',' + location + ',' + job_link + '\n')


# for i in range(1, pages+1):
# 	pg_src = driver.page_source
# 	job_page_iter(pg_src, f)
# 	print("Extracted page", i, "of", pages)
# 	if i == pages:
# 		break
# 	#go to next page?
