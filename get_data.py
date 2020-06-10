# get_data.py

#print("REQUESTING SOME DATA FROM THE INTERNET...")

import json
import requests
import statistics

#part 1
#request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"
#response = requests.get(request_url)
#response_data = json.loads(response.text)
#print(response_data['name'])
#print('****************\n\n')
#
##part 2
#request2_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
#resp = requests.get(request2_url)
#resp_data = json.loads(resp.text)
#
#i = 0
#while i != len(resp_data):
#    print('Name:' , resp_data[i]['name'],'', 'ID:', resp_data[i]['id'])
#    i=i+1
#    print('****************\n\n')
#
##Alternative:
#
##prod2_path = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
##prod2 = requests.get(prod2_path)
##prod2_data = json.loads(prod2.text)
##
##for x in prod2_data:
#    #print(f"{x['name']} (ProductID: {x['id']}")
#
##part 3
#request3_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
#response3 = requests.get(request3_url)
#response_data3 = json.loads(response3.text)
#
#grades=[]
#students = response_data3["students"]
#for x in students:
#    grades.append(x["finalGrade"])
#
#print(max(grades))
#
#---------------------------------------------------


print("----------")
print("PART 1")
product_response = requests.get("https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json")
product = json.loads(product_response.text)
print(product["name"])
print("----------")


print("PART 2")
products_response = requests.get("https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json")
products = json.loads(products_response.text)
for p in products:
    print(p["name"])
print("----------")


print("PART 3")
gradebook_response = requests.get("https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json")
gradebook = json.loads(gradebook_response.text)
#print(gradebook)
#breakpoint()
grades = [s["finalGrade"] for s in gradebook["students"]]
print("MIN:", min(grades))
print("MAX:", min(grades))
print("AVG:", statistics.mean(grades))






