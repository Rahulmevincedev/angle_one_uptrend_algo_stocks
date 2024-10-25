import http.client

conn = http.client.HTTPSConnection("api-op.streak.tech")
payload = ''
headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9',
  'authorization': 'csrftoken=isKIO0LzgCRbLEjxDwmLXqOgi5gUx0L2n9Z3heTQNOTb4gjm0F18E2oi3Tr2MM16;csrfmiddlewaretoken=isKIO0LzgCRbLEjxDwmLXqOgi5gUx0L2n9Z3heTQNOTb4gjm0F18E2oi3Tr2MM16;sessionid=TGnxUWU2fGqKaaaqEcYtbPdHE2G9YJbQ',
  'cache-control': 'no-cache',
  'origin': 'https://www.streak.tech',
  'pragma': 'no-cache',
  'priority': 'u=1, i',
  'referer': 'https://www.streak.tech/',
  'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
  'Cookie': 'streak_capp=MTcyODg4NDE0NHxRd3dBUURveE9tUnFZVzVuYnk1amIyNTBjbWxpTG5ObGMzTnBiMjV6TG1OaFkyaGxiVzl5Tm1abloxUmpjM1J6YjFZMGFqRjZjekpMZGpGTE5uVnRORUZpUmpnPXzWQE76Ald2ciRFFIPsizNsPae-sPzDFHux6DMmGDBVUw=='
}
conn.request("GET", "/fetch_order_log/?deployment_uuid=c2d0656b-bb7d-4d10-b443-abcd56f9c113", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))