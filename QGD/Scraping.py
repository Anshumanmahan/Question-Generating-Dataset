def scraping(link):
    from bs4 import BeautifulSoup
    import urllib.request
    import sys
    import os
    import selenium.webdriver
    import time
    from selenium import webdriver
    options = webdriver.FirefoxOptions()
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.dir", "/N/u/anshdixi/Carbonate/Sherlock/sherlock-project-master/QGD/download")
    options.set_preference("browser.download.useDownloadDir", True)
    options.set_preference("browser.download.viewableInternally.enabledTypes", "")
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")
    options.set_preference("pdfjs.disabled", True)

    str = link #my_url

    driver = webdriver.Firefox(executable_path = '/N/u/anshdixi/Carbonate/geckodriver',options=options)
    driver.get(str)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/article/div/section[1]/ul/li[1]/a').click()
    driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/section[1]/div[1]/div[1]/ul/li[1]/div/button/span').click()
    driver.find_element_by_css_selector('.dropdown-menu > li:nth-child(1) > a:nth-child(1) > span:nth-child(1)').click()

    time.sleep(3)


    filename = os.listdir('/N/u/anshdixi/Carbonate/Sherlock/sherlock-project-master/QGD/download')[0]
    filepath = '/N/u/anshdixi/Carbonate/Sherlock/sherlock-project-master/QGD/download/'
    x = os.path.join(filepath,filename)
    y = '/N/u/anshdixi/Carbonate/Sherlock/sherlock-project-master/QGD/data.csv'
    os.replace(x,y)

    #os.remove(x)

    driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/section[1]/div[1]/div[2]/p/a').click()
    driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/article/div/section[1]/ul/li[2]/a').click()
    driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/section[1]/div[1]/div[1]/ul/li[1]/div/button').click()
    driver.find_element_by_css_selector('.dropdown-menu > li:nth-child(1) > a:nth-child(1) > span:nth-child(1)').click()

    time.sleep(3)

    filename = os.listdir('/N/u/anshdixi/Carbonate/Sherlock/sherlock-project-master/QGD/download')[0]
    filepath = '/N/u/anshdixi/Carbonate/Sherlock/sherlock-project-master/QGD/download/'
    x = os.path.join(filepath,filename)
    y = '/N/u/anshdixi/Carbonate/Sherlock/sherlock-project-master/QGD/dataColumn.csv'
    os.replace(x,y)

    #os.remove(x)
    driver.close()
    source = urllib.request.urlopen(str)
    soup = BeautifulSoup(source,'html.parser')
    x = soup.find_all(class_='module-content')
    for para in soup.find("h1"):
        header = para.get_text()

    for para in soup.find("p"):
        paragraph = para.get_text()

    header = header.strip()
    paragraph = paragraph.strip()
    content = header + '\n' +paragraph
    text_file = open("dataDescription.txt", "wt")
    n = text_file.write(content)
    text_file.close()