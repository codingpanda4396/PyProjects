import requests
import json
def get_poins(url,jsonObj):
    response=requests.post(url,json=jsonObj)
    if response.status_code == 200:
        result=response.json()
        return result
    else:
        return []



if __name__=='__main__':
    url="https://apinew.juejin.im/recommend_api/v1/short_msg/ho t"
    payload = {"cursor": 0, "id_type": 4, "sort_type": 200, "limit": 200}
  
    res=get_poins(url,payload)
    print(res)