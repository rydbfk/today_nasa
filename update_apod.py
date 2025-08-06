import requests
import datetime

API_KEY = "YOUR_NASA_API_KEY"
URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

response = requests.get(URL)
data = response.json()

today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(f"# 🌌 NASA Astronomy Picture of the Day\n")
    f.write(f"## 📅 {today}\n\n")  # 시간까지 포함
    f.write(f"**{data.get('title', 'No Title')}**\n\n")
    f.write(f"{data.get('explanation', 'No Description')}\n\n")
    f.write(f"![APOD]({data.get('url', '')})\n")
