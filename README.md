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

  8) Go to console.cloud.google.com
  
  9) Navigate to App Engine
  
  10) click on select language
  
  11) Select python
  
  12) follow prompts on screen
  
  13) Wait for App Engine to finish loading
  
  14) Select cancel tutorial
  
  15) Set the bucket's default ACL to public-read, which enables users to see their uploaded images:
  
     gsutil defacl set public-read gs://[YOUR-BUCKET-NAME]

  16) Clone our repository: 
  
    git clone csc431-sp18-t8
  
  
  
### Configuration
  
  1) Open gcp folder in our repository:
  ```
  cd gcp-code/wkshp-maps-sp18
  ```
  
  2) Open config.py for editing.
    
  3) Set the value of PROJECT_ID to your project ID, which is visible in the GCP Console.
  
  4) Set the value of DATA_BACKEND to datastore
  
  5) Set the value of CLOUD_STORAGE_BUCKET to your Cloud Storage bucket name.
    
  5) Save and close config.py.
  
  Cloud Datastore is a fully managed service that is automatically initialized and connected to your App Engine app. No further configuration is required.
  
  
### Deploying the app
  1) Deploy the sample app.
    
    gcloud app deploy
  2) In your web browser, enter this address. Replace [YOUR_PROJECT_ID] with your project ID:
  
    https://[YOUR_PROJECT_ID].appspot.com
