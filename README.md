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
  
  
