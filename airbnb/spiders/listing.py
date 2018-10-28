# -*- coding: utf-8 -*-
import scrapy
from ..items import AirbnbItem
from urllib.parse import urlencode
import json
import logging
QUERY_URL = 'https://www.airbnb.com/api/v2/explore_tabs?'
PARAMS = {
    'version': "1.3.9",
    'satori_version': "1.1.0",
    '_format': "for_explore_search_web",
    'experiences_per_grid': "20",
    'items_per_grid': 30,
    'gbuidebooks_per_grid': 20,
    'auto_ib': True,
    'fetch_filters': True,
    'has_zero_guest_treatment': False,
    'is_guided_search': True,
    'is_new_cards_experiment': True,
    'luxury_pre_launch': True,
    'query_understanding_enabled': True,
    'show_groupings': True,
    'supports_for_you_v3': True,
    'timezone_offset': -300,
    'client_session_id': "21f0f9b8-ffb0-4474-8a9e-e4cbde7795e1",
    'metadata_only': False,
    'is_standard_search': True,
    'tab_id': "home_tab",
    # 'section_offset': 5,
    # 'items_offset': 18,
    'recommendation_item_cursor': "",
    'refinement_paths[]': "/homes",
    'allow_override[]': "",
    # 'price_max': 687,
    # 'price_min': 687,
    'last_search_session_id': "73a686e7-9dcc-4364-8b3f-4f87b8c04f83",
    'federated_search_session_id': "301dafce-2a37-4182-b47f-396c006b7ad5",
    'screen_size': "large",
    'query': "Austin",  # query string, put address / zipcode / placename here
    '_intents': "p1",
    'key': "d306zoyjsyarp7ifhu67rjxn52tv0t20",
    'currency': "USD",
    'locale': "en",
}


def url(**kwargs):
    # generate a url with specified arguments
    params_copy = PARAMS.copy()
    params_copy.update(kwargs)
    return QUERY_URL + urlencode(params_copy)


class ListingSpider(scrapy.Spider):
    name = 'listing'
    allowed_domains = ['airbnb.com']

    def __init__(self, query='Austin', **kwargs):
        PARAMS["query"] = query
        super().__init__(**kwargs)

    def start_requests(self):
        lowest = dict(price_max=20)
        # price_range passed in meta to be retrived from response
        yield scrapy.Request(url(**lowest), meta={"args": lowest})
        for price in range(20, 990, 10):
            price_range = dict(price_min=price, price_max=price + 10)
            yield scrapy.Request(
                url(**price_range), meta={"args": price_range})
        highest = dict(price_min=1000)
        yield scrapy.Request(url(**highest), meta={"args": highest})

    def parse(self, response):
        # see test.json for example json response
        data = json.loads(response.body)
        price_range = response.meta["args"]
        if "explore_tabs" not in data:
            logging.error(f"No tabs in page {response.url}")
        for tab in data["explore_tabs"]:
            pagination = tab["pagination_metadata"]
            if pagination["has_next_page"]:
                yield scrapy.Request(
                    url(items_offset=pagination["items_offset"],
                        section_offset=pagination["section_offset"],
                        **price_range),
                    meta={"args": price_range})
            for section in tab.get("sections", []):
                for item in section.get("listings", []):
                    yield AirbnbItem(data=item)
