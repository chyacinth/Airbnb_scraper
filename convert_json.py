import json
import sys
import pandas as pd
import pprint
from tabulate import tabulate

if __name__ == '__main__':
    input_file = sys.argv[1]
    json_str_list = []
    with open(input_file, 'r') as data_file:

        input_str = data_file.read()
        input_lists = input_str.split('\n][\n')        
        if len(input_lists) > 1:
            for i in range(0,len(input_lists)):
                if (i == 0):
                    input_lists[i]+='\n]'
                elif (i < len(input_lists) - 1):
                    input_lists[i]='[\n'+input_lists[i]+'\n]'
                else:
                    input_lists[i]='[\n'+input_lists[i]
        
                json_str_list += json.loads(input_lists[i])

    print(len(json_str_list))

    for i in range(0,len(json_str_list)):
        json_str_list[i] = json.dumps(json_str_list[i])

    json_str_list = list(set(json_str_list))
    
    final_df = pd.DataFrame()
    
    #for i in range(len(json_str_list)):

    #    json_str_list[i] = json.loads(json_str_list[i])


    #import pickle
    #pickle.dump( json_str_list, open( input_file.split(".")[0]+"_remove_dup.p", "wb" ) )
    
    for js in json_str_list:
        dt={}
        js = json.loads(js)        
        dt["airbnb_id"]=js["data"]["listing"].get("id")
        dt["beds"]=js["data"]["listing"].get("beds")
        dt["is_rebookable"]=js["data"]["listing"].get("is_rebookable")
        dt["is_business"]=js["data"]["listing"].get("is_business_travel_ready")
        dt["is_superhost"]=js["data"]["listing"].get("is_superhost")
        dt["picture_count"]=js["data"]["listing"].get("picture_count")
        dt["lat"]=js["data"]["listing"].get("lat")
        dt["lng"]=js["data"]["listing"].get("lng")
        dt["localized_city"]=js["data"]["listing"].get("localized_city")
        dt["localized_neighborhood"]=js["data"]["listing"].get("localized_neighborhood")
        dt["name"]=js["data"]["listing"].get("name")
        dt["person_capacity"]=js["data"]["listing"].get("person_capacity")
        dt["reviews_count"]=js["data"]["listing"].get("reviews_count")
        dt["room_type"]=js["data"]["listing"].get("room_type")
        dt["space_type"]=js["data"]["listing"].get("space_type")
        dt["star_rating"]=js["data"]["listing"].get("star_rating")
        dt["can_instant_book"]=js["data"]["pricing_quote"].get("can_instant_book")
        dt["monthly_price_factor"]=js["data"]["pricing_quote"].get("monthly_price_factor")
        dt["rate_amount"]=js["data"]["pricing_quote"]["rate_with_service_fee"].get("amount")
        dt["amount_formatted"]=js["data"]["pricing_quote"]["rate_with_service_fee"].get("amount_formatted")
        dt["currency"]=js["data"]["pricing_quote"]["rate_with_service_fee"].get("currency")
        dt["weekly_price_factor"]=js["data"]["pricing_quote"].get("weekly_price_factor")


        '''dt["badges"]=js["data"]["listing"].get("badges")
        dt["bathroom_label"]=js["data"]["listing"].get("bathroom_label")
        dt["bathrooms"]=js["data"]["listing"].get("bathrooms")
        dt["bed_label"]=js["data"]["listing"].get("bed_label")
        dt["bedroom_label"]=js["data"]["listing"].get("bedroom_label")
        dt["bedrooms"]=js["data"]["listing"].get("bedrooms")
        
        dt["city"]=js["data"]["listing"].get("city")
        dt["host_languages"]=js["data"]["listing"].get("host_languages")        
        dt["host_thumbnail_url_small"]=js["data"]["listing"].get("host_thumbnail_url_small")
        dt["host_thumbnail_url"]=js["data"]["listing"].get("host_thumbnail_url")
        
        
        dt["is_fully_refundable"]=js["data"]["listing"].get("is_fully_refundable")
        dt["is_host_highly_rated"]=js["data"]["listing"].get("is_host_highly_rated")
        dt["is_new_listing"]=js["data"]["listing"].get("is_new_listing")

        dt["neighborhood"]=js["data"]["listing"].get("neighborhood")
        
        
        dt["preview_amenities"]=js["data"]["listing"].get("preview_amenities")
        dt["property_type_id"]=js["data"]["listing"].get("property_type_id")
        
        dt["room_and_property_type"]=js["data"]["listing"].get("room_and_property_type")
        dt["room_type_category"]=js["data"]["listing"].get("room_type_category")
        
        dt["scrim_color"]=js["data"]["listing"].get("scrim_color")
        
        
        dt["tier_id"]=js["data"]["listing"].get("tier_id")        
        dt["is_superhost"]=js["data"]["listing"]["user"].get("is_superhost")
        dt["seo_reviews"]=js["data"]["listing"].get("seo_reviews")
        #dt["amenity_ids"]=js["data"]["listing"].get("amenity_ids")
        #dt["preview_amenity_names"]=js["data"]["listing"].get("preview_amenity_names")        
        
        
        dt["price_string"]=js["data"]["pricing_quote"].get("price_string")
        dt["rate_type"]=js["data"]["pricing_quote"].get("rate_type")
        print(dt)        
    {"data": {"listing": {"badges": [], "bathroom_label": "1 shared bath", "bathrooms": 1.0, "bed_label": "1 bed", "bedroom_label": "1 bedroom", "bedrooms": 1, "beds": 1, "city": "Austin", "guest_label": "2 guests", "host_languages": [], "host_thumbnail_url_small": "https://a0.muscache.com/im/pictures/user/9a51864e-2d9c-4808-b16a-d7d6707d1587.jpg?aki_policy=profile_small", "host_thumbnail_url": "https://a0.muscache.com/im/pictures/user/9a51864e-2d9c-4808-b16a-d7d6707d1587.jpg?aki_policy=profile_x_medium", "id": 7702099, "is_business_travel_ready": false, "is_fully_refundable": true, "is_host_highly_rated": true, "is_new_listing": false, "is_rebookable": false, "is_superhost": true, "kicker_content": {"messages": ["Private room", "1 bed"]}, "lat": 30.438772179173153, "lng": -97.75112451255002, "localized_city": "Austin", "localized_neighborhood": "Milwood", "name": "NW Howdy Hotel Bedroom", "neighborhood": "Milwood", "person_capacity": 2, "picture_count": 16, "preview_amenities": "Wifi, Free parking on premises, Hair dryer", "property_type_id": 2, "reviews_count": 132, "room_and_property_type": "Private room in house", "room_type_category": "private_room", "room_type": "Private room", "scrim_color": "#1E1B14", "show_structured_name": false, "space_type": "Private room", "star_rating": 5.0, "tier_id": 0, "user": {"first_name": " ", "has_profile_pic": true, "id": 7404805, "is_superhost": true, "picture_url": "https://a0.muscache.com/im/pictures/user/9a51864e-2d9c-4808-b16a-d7d6707d1587.jpg?aki_policy=profile_x_medium", "smart_name": " ", "thumbnail_url": "https://a0.muscache.com/im/pictures/user/9a51864e-2d9c-4808-b16a-d7d6707d1587.jpg?aki_policy=profile_small"}, "wide_kicker_content": {"messages": ["Private room in house"]}, "public_address": "Austin, TX, United States", "seo_reviews": [], "amenity_ids": [1, 2, 3, 4, 5, 9, 77, 85, 23, 89, 90, 91, 30, 35, 36, 37, 39, 40, 41, 44, 45, 46, 47, 51, 53], "preview_amenity_names": ["Wifi", "Free parking on premises", "Hair dryer"], "reviews": []}, "pricing_quote": {"can_instant_book": false, "monthly_price_factor": 1.0, "price_string": "From $38 per night", "rate": {"amount": 38.0, "amount_formatted": "$38", "currency": "USD", "is_micros_accuracy": false}, "rate_type": "nightly", "rate_with_service_fee": {"amount": 38.0, "amount_formatted": "$38", "currency": "USD", "is_micros_accuracy": false}, "weekly_price_factor": 1.0}, "verified": {"enabled": false, "badge_text": "Plus", "badge_secondary_text": "Verified", "kicker_badge_type": "filled"}, "verified_card": false}}'''
        #print(dt)
        final_df = final_df.append(dt, ignore_index=True)
        #current_df = pd.DataFrame([dt],columns=dt.keys())
        #print(current_df)

        #final_df = pd.concat([final_df,current_df], ignore_index=True)

    #print(final_df.head())
    #for i in range(0,len(json_str_list)):
     #   print(json_str_list[i])
        #for js in jsons:
         #   json_list.append(js)    

                        

        
        #print(final_fm)
        #tabulate(final_fm, headers='keys', tablefmt='psql')    
    final_df.to_csv(input_file + '.csv')
            #pprint.pprint(data[0])
        
        #print(len(input_str.split('][')))
        
        #json_data = data_file.read()

    #data = json.loads(json_data)

    #pprint.pprint(len(data))'''