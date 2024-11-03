# dependencies
from dotenv import load_dotenv
import os
import asyncio

# ai
from src.model.init import trigger_ai_response
from src.collector.init import get_scraped_img

load_dotenv()

async def process_img(url):
    img_container =  get_scraped_img(url)
    
    model_response = await trigger_ai_response(img_container)  
    print(model_response)

async def __main__():
    await process_img("https://eltiempove.com/un-grand-slam-de-thomas-y-el-juego-de-clase-ponen-a-cleveland-a-pelear-liga-americana/")

if __name__ == "__main__":
    asyncio.run(__main__())