# Wrapper for the Giphy API

import giphy_client
from random import randint


class Giphy:

    api_instance = giphy_client.DefaultApi()
    api_key = open("giphy_key.txt", "r").read()

    @staticmethod
    def search(keywords):
        api_response = Giphy.api_instance.gifs_search_get(Giphy.api_key, keywords, limit=100)
        return api_response.data

    @staticmethod
    def get_random_gif(gif_list):
        random = randint(0, len(gif_list)-1)
        return gif_list[random]

    @staticmethod
    def get_url(gif):
        return gif.images.original.url
