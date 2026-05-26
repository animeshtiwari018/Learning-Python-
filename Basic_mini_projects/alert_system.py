device_status = "active"
temperature = int(input("Enter the temprature:"))

if device_status == "active":
    if temperature > 35:
        print("High Temperature")
    else:
        print("Temperature is low")
        
else:
    print("Device is offline")
        