import os
import requests
import datetime

API_KEY = os.getenv("NASA_API_KEY")  # 환경변수에서 가져옴
URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

response = requests.get(URL)
data = response.json()

print(data)

today = datetime.date.today().isoformat()

with open("README.md", "w", encoding="utf-8") as f:
    f.write(f"# 🌌 NASA Astronomy Picture of the Day\n")
    f.write(f"## 📅 {today}\n\n")
    f.write(f"**{data.get('title', 'No Title')}**\n\n")
    f.write(f"{data.get('explanation', 'No Description')}\n\n")
    f.write(f"![APOD]({data.get('url', '')})\n\n")
    f.write(f"_Last updated: {datetime.datetime.now()}_\n")
