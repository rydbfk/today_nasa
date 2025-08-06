import requests

api_key = "YOUR_NASA_API_KEY"  # 실제 키는 workflow에서 치환됨
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url)
data = response.json()

title = data.get("title", "")
explanation = data.get("explanation", "")
image_url = data.get("url", "")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(f"# NASA Astronomy Picture of the Day\n\n")
    f.write(f"## {title}\n\n")
    f.write(f"![APOD Image]({image_url})\n\n")
    f.write(f"{explanation}\n")
