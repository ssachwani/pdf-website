# seo-agent/seo_agent.py
import requests
from bs4 import BeautifulSoup

def analyze_seo(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Check title
    title = soup.find('title')
    if not title or len(title.text) < 30:
        print("SEO Issue: Title is too short/missing")
    else:
        print(f"Title: {title.text}")

    # Check meta description
    meta = soup.find('meta', attrs={'name': 'description'})
    if not meta or len(meta['content']) < 150:
        print("SEO Issue: Meta description missing/too short")

# Test with your website
analyze_seo("https://your-pdf-website.netlify.app")