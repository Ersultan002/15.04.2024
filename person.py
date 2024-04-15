#person_data={}
#person_data=dict
#person_data["name"]="Askar"
#last_name="Erlanov"
#person_data["last_name"]=last_name
#a={"name":"Askar", "lastname":"Erlanov"}
#for k,v in a.items():
#    print("Key", k)
#    print("Value", v)
#

list_1=[ {
    "name":"Kanat",
    "last_name":"Erbolov",
    "Age":20},
    {"name":"Askar",
     "last_name":"Erzhanov",
     "Age":15},
    {"name":"Kairat",
     "last_name":"Zhandosov",
     "Age":45}
]

total_age = 0
for person in list_1:
    total_age += person["Age"]
    
count = len(list_1)


average_age = total_age / count

print("Average age:", average_age)
