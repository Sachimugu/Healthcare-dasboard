### Importing all relevant libraries
# import urllib3 take urllib #o mins more than request

import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm.notebook import tqdm_notebook

#function to load a url and parse it content
def browse(url): #browse function
    page= requests.get(url) #to load a url
    soup= BeautifulSoup(page.content, 'html.parser') # parse it content
    return soup

# def browse(url):
#     http = urllib3.connection_from_url(url)
#     r = http.urlopen('GET', url)
#     page=r.data.decode('utf-8')
#     soup= BeautifulSoup(page, 'html.parser') # parse it content
#     return soup

url="https://hfr.health.gov.ng/facilities/hospitals-list" #link
soup = browse(url)
total=int(soup.findAll('a', class_="page-link")[-2].text)


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
print(f'total: {total}')
for num in tqdm_notebook(range(total), desc= 'Loading....'):
    url=f"https://hfr.health.gov.ng/facilities/hospitals-list?page={num}"
    soup=browse(url)
    facilities= soup.findAll('button', class_='btn btn-success btn-sm')
    for facility in facilities:
        Id.append(facility['data-id'])
        State.append(facility['data-state'])
        Facility_Name.append(facility['data-facility_name'])
        Ward.append(facility['data-ward'])
        LGA.append(facility['data-lga'])
        Ownership.append(facility['data-ownership'])
        Ownership_Type.append(facility['data-ownership_type'])
        Facility_Level.append(facility['data-facility_level'])
        Facility_Level_Option.append(facility['data-facility_level_option'])
        Physical_Location.append(facility['data-physical_location'])
        Postal_Address.append(facility['data-postal_address'])
        Longitude.append(facility['data-longitude'])
        Latitude.append(facility['data-latitude'])
        Phone_Number.append(facility['data-phone_number'])
        Email_Address.append(facility['data-email_address'])
        Website.append(facility['data-website'])
        Operational_Status.append(facility['data-operation_status'])
        Total_number_of_Beds.append(facility['data-beds'])
        Onsite_Laboratory.append(facility['data-onsite_laboratory'])
        Mortuary_Services.append(facility['data-mortuary_services'])
        Ambulance_Services.append(facility['data-ambulance_services'])
        Number_of_Doctors.append(facility['data-doctors'])
        Number_of_Dentists.append(facility['data-dentist'])
        Number_of_Nurses.append(facility['data-nurses'])
        Number_of_Midwifes.append(facility['data-midwifes'])
        Number_of_him_officers.append(facility['data-him_officers'])
        Number_of_Nurses_Midwifes.append(facility['data-nurse_midwife'])
        Number_of_community_health_officer.append(facility['data-community_health_officer'])
        Number_of_community_extension_workers.append(facility['data-community_extension_workers'])
        Number_of_jun_community_extension_worker.append(facility['data-jun_community_extension_worker'])
        Number_of_dental_technicians.append(facility['data-dental_technicians'])
        Number_of_env_health_officers.append(facility['data-env_health_officers'])
        Inpatient_care.append(facility['data-inpatient'])
        Outpatient_care.append(facility['data-outpatient'])

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
df.to_csv('health2.csv', index=False)