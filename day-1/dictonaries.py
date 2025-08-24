my_dict={
    "key1":"value1",
    "key2":"value2",
    "key1":"value3",#if we give the same key it will take the most recent one and 
    # will be only two unique keys and last value of that key will be returned.
}
print(my_dict)

office_details={
    "Company_name":"Cognizant",
    "id":2413637,
    "name":"Devendar Reddy Lomada",
    "email id":"devendarreddylomada@cognizant.com",
    "Designation":"Engineer Trainee",
    "Skills":["Vmware","windowsserver2022","ITIL","Networking","Storages","Monitoring"],
    "mobileno":7674920534,
    "is_graduated":True,
    "Assigned_to_project":{
        "SO_id":23123,
        "Project_id":48992,
        "Project_name":"DBA Managed Services",
    },
    "Location":("SIRUSERI","CHENNAI","INDIA")

}
print(office_details)

#Accessing dictonaries
print(office_details.get("Assigned_to_project"))
print(office_details.get("Skills"))

#ADD or Update Elements
office_details["Martial_Status"]="Single" #ADDing Elements

office_details["name"]="Lomada Devendar Reddy" #UPDATING Elements
print(office_details)