 
import os

# Define the project folder and sub-folders
project_folder = "realtime_data_processing"
api_folder = "api"
app_folder = "app"
data_folder = "data"

# Create the project folder if it doesn't exist
if not os.path.exists(project_folder):
    os.mkdir(project_folder)

# Create the sub-folders if they don't exist
if not os.path.exists(os.path.join(project_folder, api_folder)):
    os.mkdir(os.path.join(project_folder, api_folder))

if not os.path.exists(os.path.join(project_folder, app_folder)):
    os.mkdir(os.path.join(project_folder, app_folder))

if not os.path.exists(os.path.join(project_folder, data_folder)):
    os.mkdir(os.path.join(project_folder, data_folder))

# Create empty files for the API and App
open(os.path.join(project_folder, api_folder, "main.py"), 'w').close()
open(os.path.join(project_folder, app_folder, "main.py"), 'w').close()

# Create the data files
open(os.path.join(project_folder, data_folder, "sensor.csv"), 'w').close()
open(os.path.join(project_folder, data_folder, "twitter.csv"), 'w').close()
