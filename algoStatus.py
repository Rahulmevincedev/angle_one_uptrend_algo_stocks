import http.client

conn = http.client.HTTPSConnection("api-op.streak.tech")
payload = ''
headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9',
  'authorization': 'csrftoken=Fz71IHv1mJEOxGtFe4a6AX77XjThDRv4bbZuc4lXVRpa4VtbUtUojI9sqCZcRB9Z;csrfmiddlewaretoken=Fz71IHv1mJEOxGtFe4a6AX77XjThDRv4bbZuc4lXVRpa4VtbUtUojI9sqCZcRB9Z;sessionid=ABq9fXCY0qEKumJ05nkVQl9etoGvfACU',
  'origin': 'https://www.streak.tech',
  'priority': 'u=1, i',
  'referer': 'https://www.streak.tech/',
  'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}
conn.request("GET", "/fetch_order_log/?deployment_uuid=cf19a1ec-81c9-4e40-b157-eb16b1e9efa4", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))