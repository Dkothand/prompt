# README for Prompt

Requires: Python3 (Developed with Python3.10)  

## Setup
- Clone Repo  
`git clone https://github.com/Dkothand/prompt`  
`cd prompt`  

- Create Python venv and install dependencies  
`python3 -m venv env`  
`source env/bin/activate`  
For Windows: `source /env/Scripts/activate`  
`pip install -r requirements.txt`  

- Load Seed Data  
app/ has a `fixtures` directory which can be used to pre-populate the database  
Database can be populated with:  
`python manage.py loaddata selection/app/fixtures/fixtures.json`

- Run the Server  
`cd selection && python manage.py runserver`


## Relevant Code
A majority of the code is boilerplate provided by Django.  
The logic I have introduced mainly lives in selection/app/models.py and selection/app/views.py.  
These files outline the database table structure, and the GET request logic for the endpoint `/providers`
