from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import time
import warnings
warnings.filterwarnings('ignore')
from tqdm.notebook import tqdm


#Headless
from selenium.webdriver.firefox.options import Options as FirefoxOptions
options = webdriver.FirefoxOptions()
options.headless = True

path = './geckodriver' #firefox driver
driver = webdriver.Firefox(executable_path=path, options=options)

driver.get("https://hfr.health.gov.ng/facilities/hospitals-list") #url


#initialise empty list
Id=[]
Facility_Code=[]
State = []
Facility_Name = []
Ward = []
LGA = []
Facility_Name = []
Ownership = []
Ownership_Type = []
Facility_Level = []
Facility_Level_Option = []
Physical_Location = []
Postal_Address = []
Longitude = []
Latitude = []
Phone_Number = []
Alternate_Number = []
Email_Address = []
Website = []
Operational_Status = []
Total_number_of_Beds = []
Onsite_Laboratory = []
Mortuary_Services = []
Ambulance_Services = []
Number_of_Doctors = []
Number_of_Dentists = []
Number_of_Nurses = []
Number_of_Midwifes = []
Number_of_Nurses_Midwifes = []
Number_of_him_officers = []
Number_of_community_health_officer = []
Number_of_community_extension_workers = []
Number_of_jun_community_extension_worker = []
Number_of_dental_technicians = []
Number_of_env_health_officers = []       
Inpatient_care=[]
Outpatient_care = []

#get all info and append to list
nums =int(driver.find_elements(By.CLASS_NAME, 'page-link')[-2].text)
for num in tqdm(range(nums), desc='Loading'):
    driver.get(f"https://hfr.health.gov.ng/facilities/hospitals-list?page={num}")
    x =driver.find_elements(By.XPATH, '//button[contains(@class, "btn-sm")]')
    for i in x[2:]:
        Id.append(i.get_attribute('data-id'))
        State.append(i.get_attribute('data-state'))
        Facility_Name.append(i.get_attribute('data-facility_name'))
        Ward.append(i.get_attribute('data-ward'))
        LGA.append(i.get_attribute('data-lga'))
        Ownership.append(i.get_attribute('data-ownership'))
        Ownership_Type.append(i.get_attribute('data-ownership_type'))
        Facility_Level.append(i.get_attribute('data-facility_level'))
        Facility_Level_Option.append(i.get_attribute('data-facility_level_option'))
        Physical_Location.append(i.get_attribute('data-physical_location'))
        Postal_Address.append(i.get_attribute('data-postal_address'))
        Longitude.append(i.get_attribute('data-longitude'))
        Latitude.append(i.get_attribute('data-latitude'))
        Phone_Number.append(i.get_attribute('data-phone_number'))
        Email_Address.append(i.get_attribute('data-email_address'))
        Website.append(i.get_attribute('data-website'))
        Operational_Status.append(i.get_attribute('data-operation_status'))
        Total_number_of_Beds.append(i.get_attribute('data-beds'))
        Onsite_Laboratory.append(i.get_attribute('data-onsite_laboratory'))
        Mortuary_Services.append(i.get_attribute('data-mortuary_services'))
        Ambulance_Services.append(i.get_attribute('data-ambulance_services'))
        Number_of_Doctors.append(i.get_attribute('data-doctors'))
        Number_of_Dentists.append(i.get_attribute('data-dentist'))
        Number_of_Nurses.append(i.get_attribute('data-nurses'))
        Number_of_Midwifes.append(i.get_attribute('data-midwifes'))
        Number_of_him_officers.append(i.get_attribute('data-him_officers'))
        Number_of_Nurses_Midwifes.append(i.get_attribute('data-nurse_midwife'))
        Number_of_community_health_officer.append(i.get_attribute('data-community_health_officer'))
        Number_of_community_extension_workers.append(i.get_attribute('data-community_extension_workers'))
        Number_of_jun_community_extension_worker.append(i.get_attribute('data-jun_community_extension_worker'))
        Number_of_dental_technicians.append(i.get_attribute('data-dental_technicians'))
        Number_of_env_health_officers.append(i.get_attribute('data-env_health_officers'))
        Inpatient_care.append(i.get_attribute('data-inpatient'))
        Outpatient_care.append(i.get_attribute('data-outpatient'))

#Create a dataframe from list
df = pd.DataFrame({
    'ID':Id,
    'State':State,
    'Facility_Name':Facility_Name,
    'Ward':Ward,
    'LGA':LGA,
    'Ownership':Ownership,
    'Ownership_Type':Ownership_Type,
    'Facility_Level':Facility_Level,
    'Facility_Level_Option':Facility_Level_Option,
    'Physical_Location':Physical_Location,
    'Postal_Address':Postal_Address,
    'Longitude':Longitude,
    'Latitude':Latitude,
    'Phone_Number':Phone_Number,
    'Email_Address':Email_Address,
    'Website':Website,
    'Operational_Status':Operational_Status,
    'Total_number_of_Beds':Total_number_of_Beds,
    'Onsite_Laboratory':Onsite_Laboratory,
    'Mortuary_Services':Mortuary_Services,
    'Ambulance_Services':Ambulance_Services,
    'Number_of_Doctors':Number_of_Doctors,
    'Number_of_Dentists':Number_of_Dentists,
    'Number_of_Nurses':Number_of_Nurses,
    'Number_of_Midwifes':Number_of_Midwifes,
    'Number_of_Nurses_Midwifes':Number_of_Nurses,
    'Number_of_him_officers':Number_of_him_officers,
    'Number_of_community_health_officer':Number_of_community_health_officer,
    'Number_of_community_extension_workers':Number_of_community_extension_workers,
    'Number_of_jun_community_extension_worker':Number_of_jun_community_extension_worker,
    'Number_of_dental_technicians ':Number_of_dental_technicians,
    'Number_of_env_health_officers':Number_of_env_health_officers,       
    'Inpatient_care':Inpatient_care,
    'Outpatient_care':Outpatient_care,

})


#save to csv
df.to_csv('health1.csv', index=False)