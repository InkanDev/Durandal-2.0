# Wrapper for the Giphy API

import giphy_client


class Giphy:

    api_instance = giphy_client.DefaultApi()
    api_key = open("giphy_key.txt", "r").read()
