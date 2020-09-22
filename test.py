import http.client
import mimetypes
conn = http.client.HTTPSConnection("api.ciscospark.com")
payload = "{\r\n  \"text\": \"testing this test\",\r\n  \"toPersonEmail\": \"mike.wiegering@gmail.com\"\r\n}"
headers = {
  '': '',
  'Authorization': 'Bearer Y2Q1ODI1NzItNDM5Zi00OTY3LWE4Y2ItN2I2OGJjNTM4MTAyMDFiYWM2M2EtYmU0_PF84_f88c9535-c5ce-4eb5-b166-be95180e4c32',
  'Content-Type': 'application/json'
}
conn.request("POST", "/v1/messages", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))