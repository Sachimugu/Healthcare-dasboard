# HEALTH CARE DASHBOARD
![dashboard](assets/db.png)

##

### Run Locally
![](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

1. Create a folder. 
2. Open terminal in the created folder and run the following code one by one.

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
python app.py
```
Go to http://127.0.0.1:8081/ on browser