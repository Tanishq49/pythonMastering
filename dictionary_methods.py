#Dictionary methods in python
country_capitals = {
    "India": "New Delhi",
    "USA": "Washington, D.C.",
    "Japan": "Tokyo",
    "Germany": "Berlin",
    "Brazil": "Brasília",
}

#Adding another dictionary in the country_capitals
countryCapitals2 = {
    "Afghanistan": "Kabul",
    "Albania": "Tirana",
    "Algeria": "Algiers",
    "Andorra": "Andorra la Vella",
    "Angola": "Luanda",
}

country_capitals.update(countryCapitals2)

print(f"The final dictionary is:{country_capitals}")

countryName = input("Enter the country name to get its capital:")
if country_capitals[countryName]:
    print(f"The capital of the country {countryName} is {country_capitals[countryName]}")
else:
    print("Country not found in the list")
    
#Deleting all the contents of the dictionary
#! country_capitals.clear()

#Deleting an key and value from the dictionary by giving the key
#If we have to delete the country Japan from the dictionary
country_capitals.pop("Japan") #.pop is used to delete the value from the dictionary
print(f"Deleted Japan from the dictionary The resultant dictionary is:{country_capitals}")

#Deleting the last value of the dictionary using the popitem
country_capitals.popitem()
print(f"Deleted the last item from the dictionary:{country_capitals}")

#Deleting the whole dictionary completely including if its empty
#! del country_capitals

#Deleting the item using the del
# del country_capitals["Germany"] #?This will delete the Germany from the dictionary 