from pprint import pprint
import requests

class YaUploader:
  def __init__(self, token: str):
    self.token = token

  def upload(self, file_path: str):
    params = {
      'path' : name_file
    }
    headers = {
      'content-type' : 'application/json',
      'accept': 'application/json','authorization': f'OAuth {uploader.token}'
    }
    req = requests.get(API_BASE_URL + "/v1/disk/resources/upload", params=params, headers=headers)
    print(req)
    upload_url = req.json()["href"]
    print(upload_url)
    requests.put(upload_url, headers=headers, files={'file': path_to_file})
    print("ГОТОВО")

if __name__ == '__main__':

  token = 'Тут токен'
  API_BASE_URL = "https://cloud-api.yandex.net:443"
  name_file = 'Maksim.jpg'
  path_to_file = "C://Users/smelk/Desktop/Maksim.jpg"
  uploader = YaUploader(token)
  result = uploader.upload(path_to_file)

