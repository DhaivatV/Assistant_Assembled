import requests

def query_api(Question):

    reqUrl = f'''https://hardware.aaruush.org/predict?question={Question}'''
    payload = {"question" : {Question} }
    print(payload)
    response = requests.request("POST", reqUrl, data=payload,  )

    return (response)

