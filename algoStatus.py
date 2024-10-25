import http.client

conn = http.client.HTTPSConnection("api-op.streak.tech")
payload = ''
headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9',
  'authorization': 'csrftoken=gDBp1Ez90Cra7zrR7Wxrw0cFmdhuMSy0lzhAm64DZE5OpW8rteDW6NZXFPCAlX67;csrfmiddlewaretoken=gDBp1Ez90Cra7zrR7Wxrw0cFmdhuMSy0lzhAm64DZE5OpW8rteDW6NZXFPCAlX67;sessionid=G6Ogzl5uXyeWPojYSrTjRgQKbmOPjjrx',
  'origin': 'https://www.streak.tech',
  'priority': 'u=1, i',
  'referer': 'https://www.streak.tech/',
  'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
  'Cookie': 'streak_capp=MTcyOTM0ODQ2OXxRd3dBUURveE9tUnFZVzVuYnk1amIyNTBjbWxpTG5ObGMzTnBiMjV6TG1OaFkyaGxaalo2TkhsR2NrTmpSSFpLT1U5NFZWTjRla05KYUVrM2NWbG5hRmMwYnpNPXw7GoW__H0H7J-3MgoLxrqax9mlGRUQo-FO99KvJ4zeAQ=='
}
conn.request("GET", "/fetch_order_log/?deployment_uuid=c2d0656b-bb7d-4d10-b443-abcd56f9c113", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))