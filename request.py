from os import name
import requests
import json


saral=requests.get("http://saral.navgurukul.org/api/courses")
data=saral.json()
with open("child_Data.json","w") as file:
    json.dump(data,file,indent=4)
serial=0
for i in data["availableCourses"]:
    print(serial+1,i["name"],i["id"])
    serial+=1
print(" ")
couser_no=int(input("what course do you want please Enter of number:"))
name=data["availableCourses"][couser_no-1]["name"]
print(name)

child_Exercise=requests.get("http://saral.navgurukul.org/api/courses/74/exercises")

