import requests
import json
from requests.structures import CaseInsensitiveDict

def req(message):
	url = "https://dialogflow.googleapis.com/v2/projects/ed-doll-lrcv/agent/sessions/a22dcbb5-f989-d9ed-befa-159527752e86:detectIntent"
	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/json; charset=utf-8"
	headers["Authorization"] = "Bearer ya29.A0AVA9y1v1cBFhlTFxWaCAWVrojJ3fIxNq4M8WQbfyDthM2YpUkwGzN0Ihkm412IumTG7RD-8tv_wOJshP__-zTftjZMSmFiTGM0ZdEFh2VCIGmg-28XqnVYXJmAtT9RfA_DfW20xQnVJ-qIBermbveR6OguXzRsteDYdmDhAl9NIfujjk3dgO6aioufZPOSaRoHLcU28qo7UoyNSNeHy6p6FbwXl5TpqHLlCAX7ZPGxtJeyIaCgYKATASATASFQE65dr8rXWM9h2hdYgW5QrfK_w4xA0246"
	data0= '{"queryInput":{"text":{"text":"'
	data1='","languageCode":"en"}},"queryParams":{"source":"DIALOGFLOW_CONSOLE","timeZone":"Asia/Kolkata","sentimentAnalysisRequestConfig":{"analyzeQueryTextSentiment":true}}}'
	data=data0+message+data1

	resp = requests.post(url, headers=headers, data=data)
	result=json.loads(resp.text)

	return result["queryResult"]["fulfillmentText"]