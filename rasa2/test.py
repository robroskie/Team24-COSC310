import json
import requests


# url1 = "https://google-maps-geocoding.p.rapidapi.com/geocode/json"
# querystring = {"address":'Vancouver',"language":"en"}
# headers = {
# 'x-rapidapi-host': "google-maps-geocoding.p.rapidapi.com",
# 'x-rapidapi-key': "90a274727dmsh607a63ae7dd7473p12f953jsn5e3fb6071646"
# }
# response = requests.request("GET", url1, headers=headers, params=querystring)
# data = json.loads(response.text)
# lat = data['results'][0]['geometry']['location']['lat']
# long = data['results'][0]['geometry']['location']['lng']
# print('long is {} lat is {}'.format(long, lat))

# url2 = "https://booking-com.p.rapidapi.com/v1/hotels/search-by-coordinates"
# querystring2 = {"checkin_date":'2022-08-01',"order_by":"popularity","units":"metric","longitude":long,"adults_number":1,"latitude":lat,"room_number":1,"locale":"en-us","filter_by_currency":"USD","checkout_date":'2022-08-10',"children_number":"1","children_ages":"5","page_number":"0","categories_filter_ids":"class::2,class::4,free_cancellation::1","include_adjacency":"true"}
# headers = {
#     'x-rapidapi-host': "booking-com.p.rapidapi.com",
#     'x-rapidapi-key': "90a274727dmsh607a63ae7dd7473p12f953jsn5e3fb6071646"
# }
# response = requests.request("GET", url2, headers=headers, params=querystring2).json()
# # print(response)
# print(json.dumps(response, indent=4, sort_keys=True))
# temp = []

# for list_result in response['result']:
#     # print('{name} : {address}'.format(name = list_result['hotel_name'], address = list_result['address_trans']))
#     temp.append('{name} : {address} {city}'.format(name = list_result['hotel_name'], address = list_result['address_trans'], city = list_result['city_trans']))

# i = 1
# while i < len(temp) and i <= 10:
#     print(i)
#     print( ("hotel_returned_" + str(i)) +str(temp[i]))
#     i += 1



url = "https://google-maps-geocoding.p.rapidapi.com/geocode/json"

querystring = {"address":"8181 Cambie Rd., Richmond, BC V6X 3X9","language":"en"}
headers = {
'x-rapidapi-host': "google-maps-geocoding.p.rapidapi.com",
'x-rapidapi-key': "90a274727dmsh607a63ae7dd7473p12f953jsn5e3fb6071646"
}
response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text)
lat = data['results'][0]['geometry']['location']['lat']
long = data['results'][0]['geometry']['location']['lng']
print('long is {} lat is {}'.format(long, lat))

url = "https://travel-advisor.p.rapidapi.com/restaurants/list-by-latlng"

querystring = {"latitude":lat,"longitude":long,"limit":"15","currency":"CAD","distance":"25","open_now":"false","lunit":"km","lang":"en_US","min_rating":"0"}

headers = {
    "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com",
    "X-RapidAPI-Key": "90a274727dmsh607a63ae7dd7473p12f953jsn5e3fb6071646"
}

response = requests.request("GET", url, headers=headers, params=querystring).json()
# print(response)
# string_builder = ''
for list_results in response['data']:
    toadd = True
    if 'name' not in list_results:
        toadd = False
    if 'address' not in list_results:
        toadd = False
    if 'distance' not in list_results:
        toadd = False
    if 'cuisine' not in list_results:
        toadd = False
    if 'ranking' not in list_results:
        toadd = False
    if toadd == True:
        if len(list_results['cuisine']) == 0:
            toadd = False
    if toadd == True:
        print(list_results['name'])
        print(list_results['address'])
        print(list_results['cuisine'][0]['name'])
        print(str(round(float(list_results['distance'])*100,2))+"km away")
        print(list_results['ranking'] + "\n")



# print(json.dumps(response['data'], indent=4, sort_keys=True))
print(json.dumps(response['data'][2], indent=4, sort_keys=True))
# for lr in response['data']:
#     print(lr['name'])
