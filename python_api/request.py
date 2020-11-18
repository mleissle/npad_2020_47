import requests

url = "http://192.168.181.23/restconf/data/ietf-restconf-monitoring:restconf-state/capabilities"

payload={}
headers = {
  'Accept': 'application/yang.data+xml',
  'Authorization': 'Basic YWRtaW46Y2lzY28=',
  'Cookie': 'APIC-cookie=2NxK65DVTAhMUL3pquKEACeirOkRdj4oNaUaR7LMkBYWlYJFdJn1Xad3SvB7pleGTnFq2WNv0JUxnZITMaPmF2MTdlgjBz+BbXC/z7UDbqSniJ/oxB1DYzb88enzPhkifwLPb+pdEqqYUAKwZqFY9HX61QkWK7NlMvPBDnhp6dc='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
