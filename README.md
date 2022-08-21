# HEALTH CARE DASHBOARD
### https://hcdashborad.herokuapp.com/

![dashboard](assets/db.png)

## Data Source
Dataset used in building the dashboard was scaraped from the <a href = "https://hfr.health.gov.ng/facilities/hospitals-list">NIGERIA Health Facility Registry (HFR)</a> with Selenium. Explore scraping scripts <a href = 'https://github.com/Sachimugu/Health-care-dasboard/tree/master/Data%20collection'>here</a>

### Run Locally
![](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

1. Create a folder dashboard. 
2. Open terminal and cd in dashboard.

```bash
# clone the repo
git clone https://github.com/Sachimugu/Health-care-dasboard.git
```
```bash
# Create a conda virtual environment called healthCaerDashboard and install all the packages
conda create --name healthCaerDashboard pandas plotly plotly dash==2.5.1 dash-bootstrap-components
```
```bash
# Activate the conda environment
conda activate healthCaerDashboard
```
```bash
#run app
python dashboard.py
```
Go to http://127.0.0.1:8081/ on browser

### Contact
<a href="mailto:sachimugu@outlook.com"> ![](https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white) </a>
<a href="https://www.linkedin.com/in/achimugu-a-79aa8a18a/"> ![](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white) </a>
<a href="https://twitter.com/achimugu_a"> ![](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white) </a>
<a href="https://medium.com/@sachimugu"> ![](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white) </a>
