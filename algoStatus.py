import http.client

conn = http.client.HTTPSConnection("api-op.streak.tech")
payload = ''
headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9',
  'authorization': 'csrftoken=p2gjGREMoBWX2jHtyM8LDcuHQ8asO98QeosrBqsfstliAsinlkgDuWGSqOmRb2dl;csrfmiddlewaretoken=p2gjGREMoBWX2jHtyM8LDcuHQ8asO98QeosrBqsfstliAsinlkgDuWGSqOmRb2dl;sessionid=y1BgkCH6iZaV3YXMWd4UOVSQ4AiNGrfQ',
  'origin': 'https://www.streak.tech',
  'priority': 'u=1, i',
  'referer': 'https://www.streak.tech/',
  'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
  'Cookie': 'streak_capp=MTcyOTM0ODQ2OXxRd3dBUURveE9tUnFZVzVuYnk1amIyNTBjbWxpTG5ObGMzTnBiMjV6TG1OaFkyaGxaalo2TkhsR2NrTmpSSFpLT1U5NFZWTjRla05KYUVrM2NWbG5hRmMwYnpNPXw7GoW__H0H7J-3MgoLxrqax9mlGRUQo-FO99KvJ4zeAQ=='
}
conn.request("GET", "/fetch_order_log/?deployment_uuid=98c8da14-e34d-4b34-812b-69dbe890dbca", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))