# Welcome !
# 33

We'll follow the tutorial from [this 
link](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-getting-started.html)

## Details
- Choose a region
- Your VPC:
  - 1 private subnets in different AZ
  - 2 public subnet in the same AZ as the private subnets
  - public route table with a route to an IGW
  - private route table
  - Create a single security group that opens HTTP to hosts from the VPC, and SSH to anybody.
  - Make sure your private subnets CAN reach the public internet, because you'll have to install a web server on your 
private servers.
- Your hosts:
  - One on each private subnet (you'll install a web server on those) 
  - One in the public network to connect to the private ones.


In CloudFormation
