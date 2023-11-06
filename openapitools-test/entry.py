import os

from openapi_client import (
    Configuration,
    ApiClient,
    PetApi,
    Pet,
    ApiException,
)

config = Configuration(
    host="http://test.com"
)

# config.access_token = os.environ["TOKEN"]
config.access_token = "TOKEN"

with ApiClient(config) as client:
    instance = PetApi(client)
    pet = Pet()

    try:
        api_response = instance.add_pet(pet)
    except ApiException as exc:
        print(exc)
