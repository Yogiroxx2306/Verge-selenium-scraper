# xpath= '//*[@id="content"]/div/div/div/div[1]/div/div[{}]/div[1]/div/h2/a'
#     xpath_with_text = xpath + '[normalize-space()!=""]'
#     xpath_without_text = '//*[@id="content"]/div/div/div/div[1]/div/div[{}]/div[2]/div[2]'
#     element = WebDriverWait(driver, 60).until(
#     EC.presence_of_all_elements_located((By.XPATH, xpath.format(i)))
#     )
#     # element = driver.find_element_by_xpath(xpath.format(i))
#     if element.text:
#         element = element
#     else:
#         element = WebDriverWait(driver, 60).until(
#     EC.presence_of_all_elements_located((By.XPATH, xpath_without_text.format(i)))
#     )
#     # article_e = driver.find_element_by_xpath(article_name_selector)
#     # print(article_e)
#     print(element)



# article_e = WebDriverWait(driver, 60).until(
#     EC.presence_of_all_elements_located((By.XPATH, article_name_selector))
#     )
#     # article_e = driver.find_element_by_xpath(article_name_selector)
#     print(article_e)










# import requests
# from bs4 import BeautifulSoup
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
# url = 'https://www.theverge.com/archives/1'
# response = requests.get(url, headers=headers)
# # print(response.text)
# soup = BeautifulSoup(response.content,'lxml')
# # print(soup)
# my_all = soup.find_all("span", {"class": "duet--content-cards--content-card-group"})
# print(my_all)

    

# from selenium import webdriver
# from bs4 import BeautifulSoup

# # Set up the webdriver
# driver = webdriver.Chrome()
# headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
# driver.get('https://www.theverge.com/archives/1')

# # Wait for the dynamic content to load
# # (you may need to adjust the sleep time depending on the website)
# import time


# def scroll_down(driver):
#         get_scroll_height_command = ("return (document.documentElement || document.body).scrollHeight;")
#         scroll_to_command = "scrollTo(0, {});"
        
#         # Set y origin and grab the initial scroll height
#         y_position = 0
#         scroll_height = driver.execute_script(get_scroll_height_command)
        
#         while y_position != scroll_height:
#             y_position = scroll_height
#             driver.execute_script(scroll_to_command.format(scroll_height))
            
#             # Page needs to load yet again otherwise the scroll height matches the y position
#             # and it breaks out of the loop
#             time.sleep(4)
#             scroll_height = driver.execute_script(get_scroll_height_command)

# time.sleep(10)
# scroll_down(driver)
# new_url = driver.current_url

# # Extract the HTML source
# html = driver.page_source

# # Parse the HTML source with BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup)
# Find the dynamic content with BeautifulSoup
# (replace "tag" and "attribute" with the actual HTML tag and attribute of the dynamic content)
# dynamic_content = soup.find('tag', {'attribute': 'value'})

# Extract the data from the dynamic content
# (replace "data_attribute" with the actual data attribute of the dynamic content)
# data = dynamic_content['data_attribute']

# Close the webdriver
# driver.quit()







# from selenium import webdriver
# from bs4 import BeautifulSoup

# # Set the options for the headless browser
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')

# # Initialize the driver
# driver = webdriver.Chrome(options=options)

# # Navigate to the webpage
# driver.get('https://www.theverge.com/archives/1')

# # Get the full HTML using the headless browser
# html = driver.page_source

# # Close the driver
# driver.quit()

# # Parse the HTML with BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup)
# Do something with the parsed HTML, for example find all links
# links = soup.find_all('a')
# for link in links:
#     print(link.get('href'))




# from selenium import webdriver

# from selenium.webdriver.chrome.service import Service

# from selenium.webdriver.support.ui import WebDriverWait

# from selenium.webdriver.support import expected_conditions as EC

# from bs4 import BeautifulSoup

# import codecs

# import re

# from webdriver_manager.chrome import ChromeDriverManager


# driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# val = input('https://www.theverge.com/archives/1')

# wait = WebDriverWait(driver, 10)


# driver.get(val)

# get_url = driver.current_url

# wait.until(EC.url_to_be(val))

# print(driver)

# header=driver.find_element_by_class_name('duet--layout--river-container dark w-full bg-gray-13 pt-28 pb-40 lg:pt-40')

# print(header.text)

# driver.quit()













# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# # Launch the browser
# driver = webdriver.Chrome()

# # Navigate to the website
# driver.get("https://www.theverge.com/archives/1")

# # Wait for the page to load
# time.sleep(5)

# # Scroll down to the bottom of the page
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# # Wait for the page to load more articles
# time.sleep(5)

# # Extract the titles of the articles
# article_titles = driver.find_elements_by_css_selector(" ")

# for title in article_titles:
#     print(title.text)

# # Close the browser
# driver.quit()









# from requests_html import HTMLSession 
# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
# import urllib

# # s = HTMLSession()
# url = "https://www.theverge.com/archives/1"
# page = urllib.request.urlopen(url).read()
# def getdata(url):
#     r = s.get(url)
#     soup = BeautifulSoup(r.content,'html.parser')
#     return soup

# print(getdata(url))

# r = requests.get(url)
# r.raise_for_status()

# htmlContent = r.content

# soup = BeautifulSoup(page)
# print(soup.prettify)

# # # print(soup.prettify)
# # # duet--layout--river-container
# # # duet--content-cards--content-card

# # # duet--layout--river
# diva = soup.find_all('a', class_ = 'after:absolute after:inset-0 group-hover:shadow-underline-blurple dark:group-hover:shadow-underline-franklin')
# print(diva)
# # diva2 = diva.find('div')
# # # print(diva2.descendants)
# # for div in diva2.descendants:
# #     print(div)

# # articles = diva2.find('div')
# # print(articles)

# # parent_divs = diva.find('div')
# # print(parent_divs)

# # divs = parent_divs.find('div')
# # print(divs)
# # for div in divs:
# #     print(div)

# parent_div = soup.find('div', class_='mx-auto w-full')
# print(parent_div)

# # for child_div in parent_div.descendants:
# #     print(child_div)

# # content_cards = soup.find_all('div',class_='duet--content-cards--content-card')
# # print(content_cards)
# # for card in content_cards:
# #     print(card)
# # titles= []
# # urls = []
# # for article in articles:
# #     titles.append(article.text.strip())
# #     urls.append(article.find('a')['href'])

# # df = pd.DataFrame({'Title': titles, 'URL': urls})

# # print(df)