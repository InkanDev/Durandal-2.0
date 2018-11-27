# Wrapper for the Giphy API

import giphy_client


class Giphy:

    api_instance = giphy_client.DefaultApi()
    api_key = open("giphy_key.txt", "r").read()

    @staticmethod
    def search(keywords):
        api_response = Giphy.api_instance.gifs_search_get(Giphy.api_key, keywords)
        return api_response.data
