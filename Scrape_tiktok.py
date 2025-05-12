import requests
import json

# SerpAPI key (you'll need to get a key from SerpAPI)
SERPAPI_API_KEY = "your_serpapi_key"
QUERY = "online business"  # Keyword
LOCATION = "UK"  # Location filter

url = f"https://serpapi.com/search?q=site:tiktok.com+{QUERY}+{LOCATION}&api_key={SERPAPI_API_KEY}"

response = requests.get(url)
data = response.json()

# Process the results and store them in a JSON file
results = []
for result in data.get("organic_results", []):
    if "link" in result:
        video = {
            "title": result.get("title"),
            "link": result.get("link"),
            "comments": result.get("snippet"),
        }
        results.append(video)

# Write the results to a file
with open("result.json", "w") as f:
    json.dump(results, f, indent=4)
