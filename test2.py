import requests

# url = "https://skyscanner44.p.rapidapi.com/search-extended"

# querystring = {"adults":"1","origin":"YYZ","destination":"YVR","departureDate":"2022-06-28","returnDate":"2022-07-28","currency":"CAD"}

# headers = {
# 	"X-RapidAPI-Host": "skyscanner44.p.rapidapi.com",
# 	"X-RapidAPI-Key": "90a274727dmsh607a63ae7dd7473p12f953jsn5e3fb6071646"
# }

# response = requests.request("GET", url, headers=headers, params=querystring).json()



# # data =json.loads(response.text)

# # print(json.dumps(data, indent=4, sort_keys=True))

# # print(response.text['destination'])

# # print(response['itineraries']['results'])

# string_builder = ''
# temp_airlines_added = []
# i = 1

# # print(response['itineraries']['results'][0])
# # print(json.dumps(response['itineraries']['results'][0], indent=4, sort_keys=True))
# for e in response['itineraries']['results']:
# 	price = e['pricing_options'][0]['price']['amount']
# 	for ee in e['legs']:

# 		if(ee['origin']['displayCode'] == 'YYZ' and ee['segments'][0]['operatingCarrier']['name'] not in temp_airlines_added):
# 			# print('-' * 10)
# 			temp_airlines_added.append(ee['segments'][0]['operatingCarrier']['name'])

# 			if(i == 1):
# 				flight_num = 'Flight #{}'.format(i)
# 			else:
# 				flight_num = '\nFlight #{}'.format(i)
# 			# print(flight_num)

# 			flight_with = 'Flying with {}'.format(ee['segments'][0]['operatingCarrier']['name'])
# 			depart_on = 'Departing on {}'.format(ee['departure'][0:10] + ' @ ' + ee['departure'][-8:])
# 			arriv_on = 'Arriving on {}'.format(ee['arrival'][0:10] + ' @ ' + ee['arrival'][-8:])
# 			price_send = 'Which will cost you aboot: ${}'.format(price)
			
# 			string_builder += flight_num + '\n'
# 			string_builder += flight_with + '\n'
# 			string_builder += depart_on + '\n'
# 			string_builder += arriv_on + '\n'
# 			string_builder += price_send 


# 			# print(flight_with)
# 			# print(depart_on)
# 			# print(arriv_on)
# 			# print(price_send)

# 			i += 1
# 			# print('-' * 10)

# 		if(i >= 10):
# 			break

# print(string_builder)


url = "https://google-maps-search1.p.rapidapi.com/search"

payload = {
	"language": "en",
	"region": "us",
	"coordinates": "37.381315,-122.046148",
	"limit": 5,
	"reviews_limit": 2,
	"reviews_sort": "newest",
	"reviews_offset": 0,
	"reviews_query": "best",
	"photos_limit": 3,
	"queries": ["Bars in Manhattan, NY, US", "Accountants near San Francisco, CA, US", "0x8862666e9691f54d:0xf91133af6a396d08", "Lawyers in Sunnyvale, CA, US"],
	"fields": ["google_id", "name", "phone_number", "subtypes", "full_address", "country", "state", "city", "zipcode", "address", "latitude", "longitude", "status", "verified", "rating", "review_count", "cid", "google_place_id", "owner_id", "owner_name", "owner_link", "place_link", "website", "photos_sample"],
	"review_fields": ["place_google_id", "review_id", "author_id", "author_link", "author_name", "author_photo_url", "author_review_count", "review_text", "rating", "datetime_utc", "review_link", "review_photo_url", "review_language", "like_count", "owner_response_datetime_utc", "owner_response_text", "owner_response_language"],
	"photo_fields": ["place_google_id", "photo_id", "photo_url", "latitude", "longitude", "owner_id", "owner_link"],
	"fields_filters": [
		{
			"type": "not_empty",
			"field": "phone_number"
		},
		{
			"type": "not_empty",
			"field": "full_address"
		},
		{
			"type": "equals",
			"field": "verified",
			"value": True
		}
	],
	"review_fields_filters": [],
	"photo_fields_filters": []
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Host": "google-maps-search1.p.rapidapi.com",
	"X-RapidAPI-Key": "90a274727dmsh607a63ae7dd7473p12f953jsn5e3fb6071646"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)