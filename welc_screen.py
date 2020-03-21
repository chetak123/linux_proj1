import os
os.system("tput setaf 3")
print("\t\t\tWELCOME TO MY PROJEC")
os.system("tput setaf 7")
print("\t\t\t...........................................")


print("""press 1 te see date")
press 2 to conf web server
press 3 to create new user
""")

print("ENTER your choice : " , end="")
ch=int(input())

print(ch)

if (ch==1):
    os.system("date")
elif (ch==2):
    os.system("yum install https")
elif (ch==3):
    create_user=input("please enter user name: ")
    os.system("useradd {}".format(create_user))
else:
    print("option out of range")






