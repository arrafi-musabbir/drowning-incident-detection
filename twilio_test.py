from twilio.rest import Client
import glob, os
import requests

directory = "runs/detect/predict"
img_path = glob.glob(os.path.join(directory, "*.jpg"))[0]

api_key = 'your-imgbb-api'
image_path = img_path

with open(image_path, 'rb') as image_file:
    response = requests.post(
        'https://api.imgbb.com/1/upload',
        params={'key': api_key},
        files={'image': image_file}
    )

if response.status_code == 200:
    media_path = response.json()['data']['url']
    try:
      account_sid = ''
      auth_token = ''
      client = Client(account_sid, auth_token)
      message = client.messages.create(
        media_url=media_path,
        from_='',
        body='"Drowning Alerts!!! Someone is drowning!!! 🛟🌊🛟🌊🛟"',
        to=''
      )
      print(message.sid)
    except Exception as e:
      print(f"error with Twilio {e}")
else:
    print("Failed to upload image")



