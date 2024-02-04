#install Python 3.12.1
https://www.python.org/downloads/

#install Pulumi
https://www.pulumi.com/docs/clouds/aws/get-started/begin/

#install pip for installing Python dependencies
https://packaging.python.org/guides/installing-using-linux-tools/

#install AWS CLI
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

#create an iam user with administor role
#create a access key for that user
https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user_manage_add-key.html

# AWS configure. Run below commands to configure AWS CLI
# Use link https://www.pulumi.com/registry/packages/aws/installation-configuration/#create-a-shared-credentials-file
aws configure
AWS Access Key ID [None]: <YOUR_ACCESS_KEY_ID>
AWS Secret Access Key [None]: <YOUR_SECRET_ACCESS_KEY>
Default region name [None]:
Default output format [None]:

#install 7z
https://www.7-zip.org/
# Add the path to 7z.exe to your PATH environment variable. 
# See this QA: How to set the path and environment variables in Windows

#Setup google cloud account
# create a google cloud project in google console
https://console.cloud.google.com/
# Enable Google Cloud Translation API
# With the new translation project selected, go to the hamburger menu to the left and visit API & Services
# From here you need to enable Google Translate API by clicking the + Enable APIs and Services button in your dashboard.
# This will open the API Library where you will have to search for the Cloud Translation API in the search bar
# Once you’ve identified it, select it and click Enable. You will have to setup a billing account to enable it

# Create service account accesskeys from Google account project
# download the file and place it under src\lambda\translate\resource folder

# once the file is placed. Open Git Bash console
# run the below command
./deploy.sh

# If everything is properly setup then this will download python dependencies
# create a zip with lmabda code and dependencies
# Run Pulumi commands to install the lambda and APIGateway in your aws account

# console will show the APIGateway URL
# Append /dev/v1/translate to it
e.g. https://bot8l3bjye.execute-api.ap-south-1.amazonaws.com/dev/v1/translate
Set action as POST
post a raw json message e.g.
{"text": "hello Martha, how are you doing \n in this beautiful world"}

