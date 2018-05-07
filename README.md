# Registration of Workshop Maps
## Connecting to AWS Server
To access your instance:

Open an SSH client. (find out how to connect using PuTTY for windows)

Locate and cd to your private key file (serveraccess.pem). The wizard automatically detects the key you used to launch the instance.

Your key must not be publicly viewable for SSH to work. Use this command if needed:
```
chmod 400 serveraccess.pem
```
Connect to your instance using its Public DNS:
```
ec2-18-217-202-156.us-east-2.compute.amazonaws.com
```
Example:
```
ssh -i "serveraccess.pem" ec2-user@ec2-18-217-202-156.us-east-2.compute.amazonaws.com
```

Please note that in most cases the username above will be correct, however please ensure that you read your AMI usage instructions to ensure that the AMI owner has not changed the default AMI username.

## Setting Up the Amazon server

After SSH connection to server follow the following instructions

### Installing GDAL
  ```
  cd ~
  ```
  ```
  sudo yum -y update
  ```
  ```
  sudo yum-config-manager --enable epel
  ```
  ```
  sudo yum -y install make automake gcc gcc-c++ libcurl-devel proj-devel geos-devel
  ```
  ```
  cd /tmp
  ```
  ```
  curl -L http://download.osgeo.org/gdal/2.2.4/gdal-2.2.4.tar.gz | tar zxf -
  ```
  ```
  cd gdal-2.2.4/
  ```
  ```
  ./configure --prefix=/usr/local --without-python
  ```
  ```
  make
  ```
  ```
  sudo make install
  ```
  ```
  cd /usr/local
  ```
  ```
  tar zcvf ~/gdal-2.2.4-amz1.tar.gz *
  ```
### Installing Node.js
  1) Install the current version of node version manager (nvm) by typing the following at the command line to install version 33.8.
  ```
  curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash
  ```
  We will use nvm to install Node.js because nvm can install multiple versions of Node.js and allow you to switch between them. See the nvm repo on GitHub for the current version to install.
  
  2) Activate nvm by typing the following at the command line.
  ```
  . ~/.nvm/nvm.sh
  ```
  
  3) Use nvm to install the version of Node.js you intend to use by typing the following at the command line.
  ```
  nvm install 6.11.5
  ```
  To install the latest LTS (long-term-support) release of Node.js, type the following at the command line.
  ```
  nvm install --lts
  ```
  Installing Node.js also installs the Node Package Manager (npm) so you can install additional modules as needed.
  
  4) Test that Node.js is installed and running correctly by typing the following at the command line.
  ```
  node -e "console.log('Running Node.js ' + process.version)"
  ```
  This should display the following message that confirms the installed version of Node.js running.
  ex. "Running Node.js v6.11.5"

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
 
   If the project ID listed in the output is not the project that you intended to use for this tutorial, set the project by entering this command:

    gcloud config set project [YOUR_PROJECT_ID]
where [YOUR_PROJECT_ID] is the ID of the project you created.

  8) Clone our repository: 
  ```
  git clone csc431-sp18-t8
  ```
  9) In the terminal, cd into the gcp-code folder in our repository.
  
  10) In the browser, go to: http://console.cloud.google.com
  
  
