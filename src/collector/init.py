import csv
import requests
from bs4 import BeautifulSoup

def scrape_images(soup, images):
    selectors = ['img', 'figure > img', 'div > img', 'a > img', 'a > div > img']
    
    for selector in selectors:
        img_elements = soup.select(selector)
        
        for img in img_elements:
            img_src = img.get('src')
            if img_src and img_src not in [image['src'] for image in images]:
                images.append({'src': img_src})
def get_scraped_img(base_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }

    page = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    images = []

    scrape_images(soup, images)

    return images