import requests
import json
saral=requests.get("http://saral.navgurukul.org/api/courses")
data1=saral.json()
with open ("data1.json","w") as f:
    json.dump(data1,f,indent=2)


serial_no=1
for index1 in data1["availableCourses"]:                  
    print(serial_no,index1["name"],index1["id"])
    serial_no+=1
topic=int(input("WHICH TOPIC DO YOU WANT?? "))
print(data1["availableCourses"][topic-1]["name"]) 

parents_data=requests.get("http://saral.navgurukul.org/api/courses/"+data1["availableCourses"][topic-1]["id"]+" "+"/exercises")
data=parents_data.json()
## dump parents data in json file XXXX
with open("parents_data.json","w") as fl:
    json.dump(data,fl,indent=2)
course=input("DO YOU WANT TO GO NEXT(n)/PREVIOUS(p)") 
if course=="n"   :    

    index_1=1
    data1=data["data"]
    for index_2 in data1:
        print(index_1,index_2["name"])
        index_1+=1
        i=1
        if index_2["childExercises"]==[]:
            print(" ",i,index_2["slug"])
            i=i+1
        else:
            s_num2=1 
            Child=index_2["childExercises"]
            for index_3 in Child:
                print(" ",s_num2,index_3["name"])
                s_num2+=1
    same_course=input("DO YOU WANT TO GO NEXT(n)/PREVIOUS(p)")
    if same_course=="n":
        course_name=int(input("Enter in which question you wants to go:"))
        Data=data["data"][course_name-1]["childExercises"]
        indexa=1
        questionlist1=[]
        for index_4 in Data:
            questionlist1.append(index_4)
            print("  ",indexa,index_4["name"])
            # print(questionlist)
            indexa+=1

        for i in range (len(questionlist1)) :
            a=input("DO YOU WANT TO GO NEXT(n)/PREVIOUS(p)")
            if a=="n":
                slug=int(input("WHICH QUESTION DO YOU WANT?? ......."))
                slugid=Child[slug]["id"]
                ChildSlugName=Child[slug]["slug"]
                slugdata=requests.get("http://saral.navgurukul.org/api/courses/"+slugid+"/exercise/getBySlug?slug="+str(ChildSlugName))
                data8=slugdata.json()
                with open("slugdata","w") as file:
                    json.dump(data8,file,indent=8)
                    print(data8["content"])   
            elif a=="p":
                slug=int(input("WHICH QUESTION DO YOU WANT?? ......."))
                slugid=Child[slug]["id"]
                ChildSlugName=Child[slug-1]["slug"]
                slugdata=requests.get("http://saral.navgurukul.org/api/courses/"+slugid+"/exercise/getBySlug?slug="+str(ChildSlugName))
                data8=slugdata.json()
                with open("slugdata","w") as file:
                    json.dump(data8,file,indent=8)
                    print(data8["content"])     
        
        
    elif same_course=="p":
            saral=requests.get("http://saral.navgurukul.org/api/courses")
            data1=saral.json()
            with open ("data1.json","w") as f:
                json.dump(data1,f,indent=2)
            serial_no=1
            for index2 in data1["availableCourses"]:
                print(serial_no,index2["name"],index2["id"])
                serial_no+=1
            topic2=int(input("WHICH TOPIC DO YOU WANT?? "))
            print(data1["availableCourses"][topic2-1]["name"]) 

            parents_data=requests.get("http://saral.navgurukul.org/api/courses/"+data1["availableCourses"][topic2-1]["id"]+" "+"/exercises")
            data2=parents_data.json()
            with open("parents_data.json","w") as fl:
                json.dump(data2,fl,indent=2)
            s_num=1
            data3=data2["data"]
            l=1                  
            for index_2 in data:
                print(s_num,index_2["name"])
                s_num+=1
                if index_2["childExercises"]==[]:
                    print(" ",l,index_2["slug"])
                    l+=1
                else:
                    s_num2=1 
                    Child=index_2["childExercises"]
                    for index_3 in Child:
                        print(" ",s_num2,index_3["name"])
                        s_num2+=1           


elif course=="p":    
    saral=requests.get("http://saral.navgurukul.org/api/courses")
    data1=saral.json()
    with open ("data1.json","w") as f:
        json.dump(data1,f,indent=2)


    serial_no=1
    for index1 in data1["availableCourses"]:
        print(serial_no,index1["name"],index1["id"])
        serial_no+=1
    topic=int(input("WHICH TOPIC DO YOU WANT?? "))
    print(data1["availableCourses"][topic-1]["name"]) 

    parents_data=requests.get("http://saral.navgurukul.org/api/courses/"+data1["availableCourses"][topic-1]["id"]+" "+"/exercises")
    data=parents_data.json()
    with open("parents_data.json","w") as fl:
        json.dump(data,fl,indent=2)         
    course=input("DO YOU WANT TO GO NEXT(n)/PREVIOUS(p)") 
    if course=="n"   :    

        index_1=1
        data1=data["data"]
        for index_2 in data1:
            print(index_1,index_2["name"])
            index_1+=1
            i=1
            if index_2["childExercises"]==[]:
                print(" ",i,index_2["slug"])
                i=i+1
            else:
                s_num2=1 
                Child=index_2["childExercises"]
                for index_3 in Child:
                    print(" ",s_num2,index_3["name"])
                    s_num2+=1
        same_course=input("DO YOU WANT TO GO NEXT(n)/PREVIOUS(p)")
        if same_course=="n":
            course_name=int(input("Enter in which topic you wants to go:"))
            Data=data["data"][course_name-1]["childExercises"]
            indexa=1
            for index_4 in Data:
                print("  ",indexa,index_4["name"])
                indexa+=1
            
            slug=int(input("WHICH QUESTION DO YOU WANT?? ......."))
            slugid=Child[slug]["id"]
            ChildSlugName=Child[slug]["slug"]
            slugdata=requests.get("http://saral.navgurukul.org/api/courses/"+slugid+"/exercise/getBySlug?slug="+str(ChildSlugName-2))
            data8=slugdata.json()
            with open("slugdata","w") as file:
                json.dump(data8,file,indent=8)
                print(data8["content"])    
        elif same_course=="p":
            saral=requests.get("http://saral.navgurukul.org/api/courses")
            data1=saral.json()
            with open ("data1.json","w") as f:
                json.dump(data1,f,indent=2)
            serial_no=1
            for index2 in data1["availableCourses"]:
                print(serial_no,index2["name"],index2["id"])
                serial_no+=1
            topic2=int(input("WHICH TOPIC DO YOU WANT?? "))
            print(data1["availableCourses"][topic2-1]["name"]) 

            parents_data=requests.get("http://saral.navgurukul.org/api/courses/"+data1["availableCourses"][topic2-1]["id"]+" "+"/exercises")
            data2=parents_data.json()
            with open("parents_data.json","w") as fl:
                json.dump(data2,fl,indent=2)
            s_num=1
            data3=data2["data"]
            l=1
            for index_2 in data:
                print(s_num,index_2["name"])
                s_num+=1
                if index_2["childExercises"]==[]:
                    print(" ",l,index_2["slug"])
                    l+=1
                else:
                    s_num2=1 
                    Child=index_2["childExercises"]
                    for index_3 in Child:
                        print(" ",s_num2,index_3["name"])
                        s_num2+=1   
            same_course=input("DO YOU WANT TO GO NEXT(n)/PREVIOUS(p)")
            if same_course=="n":
                course_name=int(input("Enter in which topic you wants to go:"))
                Data=data["data"][course_name-1]["childExercises"]
                indexa=1
                questionlist=[]
                for index_4 in Data:
                    questionlist.append(index_4)
                    print("  ",indexa,index_4["name"])
                    indexa+=1
                  
                for i in range(questionlist) :
                    a=input("DO YOU WANT TO GO NEXT(n)/PREVIOUS(p)")
                    if a=="n":
                        slug=int(input("WHICH QUESTION DO YOU WANT?? ......."))
                        slugid=Child[slug]["id"]
                        ChildSlugName=Child[slug]["slug"]
                        slugdata=requests.get("http://saral.navgurukul.org/api/courses/"+slugid+"/exercise/getBySlug?slug="+(ChildSlugName-2))
                        data8=slugdata.json()
                        with open("slugdata","w") as file:
                            json.dump(data8,file,indent=8)
                            print(data8["content"])
                    else:
                        print("no more")