import requests
import json

data=requests.get("http://join.navgurukul.org/api/partners")
data_1=data.json()

with open("web_data.json","w") as k:
    json.dump(data_1,k,indent=8)


list1=[]
list2=[]
serial=0
for i in data_1["data"]:
    name=data_1["data"]
    id=data_1["data"]
    print(serial+1,(" -"),i["name"],(" - "),i["id"])
    list1.append(i["name"])
    list2.append(i["id"])
    serial+=1



y={}
for i in range(len(list1)):
    for k in range(len(list2)):
        y[list1[i]]=(list2[i])

print("    ")

topic=input("Which way you want:__Asending or Desending(a/d):")

if topic=="a":
    list4_vlue=[]

    for i2 in y:
        a=y[i2]
        list4_vlue.append(i2)
        list4_vlue.append(a)
    n=1
    while n<len(list4_vlue):
        j=n+2
        while j<len(list4_vlue):
            if list4_vlue[n]>list4_vlue[j]:
                c=list4_vlue[n]
                list4_vlue[n]=list4_vlue[j]
                list4_vlue[j]=c
                i2=a
            j+=2
        n+=2
    i=0
    m=1
    while i<len(list4_vlue):
        print(m," ",list4_vlue[i],list4_vlue[i+1])
        m+=1
        i+=2


elif topic=="d":
        
    list2_key=[]
    list1_vlue=[]

    for i in range(len(y)):
        max = 0
        for x in y:
            if max<y[x]:
                key=x
                max=y[x]
        list1_vlue.append(key)
        list1_vlue.append(max)
        y.pop(key)
    i=0
    s=1
    while i<len(list1_vlue):
        print(s,list1_vlue[i],list1_vlue[i+1])
        s+=1
        i+=2