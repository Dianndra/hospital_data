
#import packages
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#install drivers to access the website
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver = webdriver.Chrome(ChromeDriverManager().install())

#create an empty table to insert the data
hospital = []

#using for loop to automate the extraction of data
for link in range(1, 221):
    #get into url of each page
    url = 'https://hfr.health.gov.ng/facilities/hospitals-search?_token=4HUDEwfUVTJHCcQMzfMpNhWjVNRx9O30G75zS3PW&state_id=124&ward_id=0&facility_level_id=0&ownership_id=0&operational_status_id=1&registration_status_id=0&license_status_id=0&geo_codes=0&service_type=0&service_category_id=0&entries_per_page=10&page=' + str(link)
    driver.get(url)
    #get into the button tag to extract the data
    elements = driver.find_elements(By.CLASS_NAME, 'btn.btn-success.btn-sm')
    
    #using the get attribute to access inside the button tag, because thats where all the informations are 
    for hosp in elements:
        facility_uid = hosp.get_attribute('data-id')
        facility_code = hosp.get_attribute('data-unique_id')
        state_unique_id = hosp.get_attribute('data-state_unique_id')
        registration_no = hosp.get_attribute('data-registration_no')
        start_date = hosp.get_attribute('data-start_date')
        facility_name = hosp.get_attribute('data-facility_name')
        state = hosp.get_attribute('data-state')
        lga = hosp.get_attribute('data-lga')
        ownership = hosp.get_attribute('data-ownership')
        ownership_type = hosp.get_attribute('data-ownership_type')
        facility_level = hosp.get_attribute('data-facility_level')
        facility_level_option = hosp.get_attribute('data-facility_level_option')
        physical_location = hosp.get_attribute('data-physical_location')
        longitude = hosp.get_attribute('data-longitude')
        latitude = hosp.get_attribute('data-latitude')
        phone_number = hosp.get_attribute('data-phone_number')
        email_address = hosp.get_attribute('data-email_address')
        website = hosp.get_attribute('data-website')
        operational_days = hosp.get_attribute('data-operational_days')
        operational_hours = hosp.get_attribute('data-operational_hours')
        operation_status = hosp.get_attribute('data-operation_status')
        registration_status = hosp.get_attribute('data-registration_status')
        license_status = hosp.get_attribute('data-license_status')
        doctors = hosp.get_attribute('data-doctors')
        nurses = hosp.get_attribute('data-nurses')
        midwives = hosp.get_attribute('data-midwifes')
        beds = hosp.get_attribute('data-beds')
        hospital.append({'facility_uid': facility_uid, 'facility_code': facility_code, 'state_unique_id': state_unique_id,
                        'registration_no': registration_no, 'start_date': start_date, 'facility_name': facility_name, 'state': state,
                        'lga': lga, 'ownership': ownership, 'ownership_type': ownership_type, 'facility_level': facility_level,
                        'facility_level_option': facility_level_option, 'physical_location': physical_location, 'longitude': longitude,
                        'latitude': latitude, 'phone_number': phone_number, 'email_address': email_address, 'website': website,
                        'ooperational_days': operational_days, 'operational_hours': operational_hours, 'operation_status': operation_status,
                        'registration_status': registration_status, 'license_status': license_status, 'doctors': doctors,
                        'nurses': nurses, 'midwives': midwives, 'beds': beds})
        
#save imported data into a dataframe
df = pd.DataFrame(hospital)

#export data
df.to_csv('../data/hospital_data.csv', encoding='utf-8', index=False)






