import boto3
from create_user import cr_user as c_u
from create_policy import createPolicy as c_p
from attach_policy import attachRoleUser as a_r_u

def main():
    
    #username = input("Enter name of the new user: ")
    #c_u(username)
    #print("\n\n")
    print("Creating new policy :\n")
    c_p()
    print("\n\n")
    print("Attaching the policy to exist user :\n")
    a_r_u()

main()