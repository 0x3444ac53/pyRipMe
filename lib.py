from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def imgur_scraper(url : str) -> list:
    """
    Takes an imgur album url and return a list of
    a picture urls
    """
    raw_page_source = get_html(url)
    return BeautifulSoup(raw_page_source, 'html.parser')
    #images = soup.find_all('img', {'class' : 'post-image-placeholder'})
    #for i in images:
    #    print(i)

def get_html(url : str) -> str:
    """
    uses Selenium module to grab html then closes
    I really hate selenium so this is very much a temporary fix
    """
    options = Options()
    options.headless = True
    driver = webdriver.Firefox()
    driver.get(url)
    html = driver.page_source
    driver.quit()
    return html

fuck = imgur_scraper('https://imgur.com/gallery/rBarn')
