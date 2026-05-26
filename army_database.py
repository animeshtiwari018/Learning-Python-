army = [
    {
    "name" : "Saurabh Singh Shekhawat",
    "age": 55, 
    "unit" : "21 Para SF",
    "rank" : "Brigadier",
    "awards" : ["SM", "SC", "KC", "VSM"],
    "service_number" : "IC-12345A",
    "served" : 30
    },
    
    {
        "name" : "Hemonto Panging",
        "age" : 55,
        "unit" : "9 Para SF",
        "rank" : "Colonel",
        "awards" :  ["SM"],
        "service_number" : "IC-23456B",
        "served" : 26
    },
    {
        "name" : "Sudhir Walia",
        "age" : 30,
        "unit" : "9 Para SF",
        "rank" : "Major",
        "awards" :  ["AC"],
        "service_number" : " IC-47623P",
        "served" : 11
    }
    
]



print(f"one of the most decorated army officers: {army[0]['name']}")
print(f"Service Number is : {army[0]['service_number']}")

highest = army[0]

for soldier in army:

    if soldier["served"] > highest["served"]:
        highest = soldier

print("Officer with highest service years:")
print(highest["name"])
print(f"Served: {highest['served']} years")