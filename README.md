# Registration of Workshop Maps

### Deployment
  1) Create a Google Cloud Platform account here: https://cloud.google.com/
  
  2) Enable billing: https://cloud.google.com/billing/docs/how-to/manage-billing-account
  
  3) Create a new project that will house the web app.
  
  4) Download Google Cloud SDK: https://cloud.google.com/sdk/
  
  5) Open a terminal.
  
  6) Type in:
   ```
   gcloud auth application-default login
   ```
  7) Verify that your default project is correct:

    gcloud config list
 
   If the project ID listed in the output is not the project that you intended to use, set the project by entering this command:

    gcloud config set project [YOUR_PROJECT_ID]
where [YOUR_PROJECT_ID] is the ID of the project you created.

  8) Clone our repository: 
  ```
  git clone csc431-sp18-t8
  ```
  9) In the terminal, cd into the gcp-code folder in our repository.
  
  10) In the browser, go to: http://console.cloud.google.com
  
  
### Configuration
  
  1) Open gcp folder in our repository:
  ```
  cd gcp-code/
  ```
  
  2) Open config.py for editing.
    
  3) Set the value of PROJECT_ID to your project ID, which is visible in the GCP Console.
  
  4) Set the value of DATA_BACKEND to datastore.
    
  5) Save and close config.py.
  
  Cloud Datastore is a fully managed service that is automatically initialized and connected to your App Engine app. No further configuration is required.
    
  ### Running the app on your local machine
  1) Start a local web server:
  ```
  python main.py
  ```
  2) In web browser, enter this address:
  ```
  http://localhost:8080
  ```
  3) Press Control+C to exit the local web server
    
    
  
  
