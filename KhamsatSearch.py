from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
Path = "C:\\Users\\ASUS\\Downloads\\chromedriver.exe"
driver = webdriver.Chrome(Path)
driver.get("https://khamsat.com/community/requests")
r = 10
toSearchFor = ["بايثون", "أندرويد","باركود","سكريبت", "اندرويد"]
def getAllRequests():
    return driver.find_elements_by_class_name("ajaxbtn")
def getRequests():
    requests = []
    allRequests = getAllRequests()
    for request in allRequests:
        if any(word in request.text for word in toSearchFor):
           requests.append(request)
    return requests
    
for i in range(r):
    while len(getAllRequests()) < r*25:

        try:    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "community_loadmore_btn"))).click()
        except: pass
a = getRequests()
links = [elem.get_attribute('href') for elem in a]

for i in range(len(a)):
    print(a[i].text)
    print(links[i])

driver.quit()
