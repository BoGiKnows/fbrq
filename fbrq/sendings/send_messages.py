import jwt
import requests
import json
import numpy as np


token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDE1MjI5MDAsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IkJvR2lLbm93cyJ9.YjAMiP-VkWgrKMtwZQ6ns0Si81rgQeiAW6gRm9_4NWk'
head = {'Authorization': f'Bearer {token}'}

data = {
  "id": 11,
  "phone": 79628555166,
  "text": "string"
}
url = 'https://probe.fbrq.cloud/v1/send/11'
res = requests.post(url=url, json=data, headers=head)
print(res.json())


