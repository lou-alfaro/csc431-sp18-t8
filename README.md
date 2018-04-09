# Registration of Workshop Maps
# Connecting to AWS Server
To access your instance:

Open an SSH client. (find out how to connect using PuTTY for windows)

Locate your private key file (server access.pem). The wizard automatically detects the key you used to launch the instance.

Your key must not be publicly viewable for SSH to work. Use this command if needed:

chmod 400 serveraccess.pem

Connect to your instance using its Public DNS:
ec2-18-217-202-156.us-east-2.compute.amazonaws.com

Example:

ssh -i "serveraccess.pem" ec2-user@ec2-18-217-202-156.us-east-2.compute.amazonaws.com


Please note that in most cases the username above will be correct, however please ensure that you read your AMI usage instructions to ensure that the AMI owner has not changed the default AMI username.

# csc431-sp18-t8
