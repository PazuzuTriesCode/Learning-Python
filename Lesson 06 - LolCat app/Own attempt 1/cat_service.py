import requests
import shutil
import os


def get_cats(folder, name):
    url = "http://consuming-python-services-api.azurewebsites.net/cats/random"
    data = get_data_from_web(url)
    save_image(folder, name, data)


def get_data_from_web(url):
    response = requests.get(url, stream=True)
    return response.raw


def save_image(folder, name, data):
    file_name = os.path.join(folder, name + ".jpg")

    with open(file_name, "wb") as fout:
        shutil.copyfileobj(data, fout)