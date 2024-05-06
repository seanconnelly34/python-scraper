from selenium import webdriver 
from selenium.webdriver.common.by import By
from numpy import column_stack 
import numpy as lead_row
import csv
import time

def getList():
    name = []
    services = []
    phone_numbers = []
    addresses = []
  
    def url(page_number):
        print(page_number)
        url = f"www.example.com&page={page_number}&sort=Distance"
        print(url)
        return url


    driver = webdriver.Chrome() 
    count = 16
    page_num = 1

    while (page_num < count):
        time.sleep(10) 
        print("\n")
        driver.get(url(str(page_num))) 
        page_num = page_num + 1
        
         

        #make a list of all containers
        containers = driver.find_elements(By.CLASS_NAME, "result-item-ab")    
        for container in containers:
            #grab business name from each container 
            bizNames = container.find_elements(By.CLASS_NAME, "bds-h4")
            for biz in bizNames:
                name.append([biz.text])

            #find first element in container for service due to same class for dif info
            service = container.find_element(By.CLASS_NAME, "bds-body")
            services.append([service.text])

            phone = container.find_elements(By.CLASS_NAME, "css-1u1ibea")
            phone_container = container.find_elements(By.CLASS_NAME, "stack")
            if not phone:
                phone_numbers.append(['N/A'])
            for p in phone:
                phone_numbers.append([p.text])

            address = container.find_elements(By.CLASS_NAME, "bds-body")
            if not address:
                addresses.append(['N/A'])
            addresses.append([address[-1].text])
            
        fields = ["Business Name", 'Services', 'Phone', "Address"]
        leads_stacked = lead_row.column_stack((name, services, phone_numbers, addresses))
        with open('name_here.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(fields)
            writer.writerows(leads_stacked)
 
    print(leads_stacked)

    driver.quit() 

getList()