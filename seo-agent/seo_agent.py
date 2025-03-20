import requests
from bs4 import BeautifulSoup

def analyze_seo(url):
    # Bypass proxy settings for PythonAnywhere
    response = requests.get(url, proxies={"http": None, "https": None})
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Check title tag
    title = soup.find('title')
    if not title or len(title.text.strip()) < 30:
        print("🚨 SEO Issue: Title tag is missing/too short (min 30 characters)")
    else:
        print(f"✅ Title: {title.text.strip()}")

    # Check meta description
    meta_description = soup.find('meta', attrs={'name': 'description'})
    if not meta_description or len(meta_description['content'].strip()) < 150:
        print("🚨 SEO Issue: Meta description missing/too short (min 150 characters)")
    else:
        print(f"✅ Meta Description: {meta_description['content'].strip()}")

    # Check h1 tags
    h1_tags = soup.find_all('h1')
    if len(h1_tags) != 1:
        print(f"🚨 SEO Issue: Found {len(h1_tags)} H1 tags (should be exactly 1)")

    # Check image alt texts
    images = soup.find_all('img')
    for img in images:
        if not img.get('alt'):
            print(f"🚨 SEO Issue: Missing alt text for image - {img['src']}")

# Analyze your live website
analyze_seo("https://toolsforpdf.netlify.app/")