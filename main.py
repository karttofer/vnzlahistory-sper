# dependencies
from dotenv import load_dotenv
import os
import asyncio  # Import asyncio to run the async function

# ai
from src.model.init import trigger_ai_response
from src.collector.init import data_collector

load_dotenv()

async def process_img(url):
    img_container = await data_collector(url)
    
    model_response = await trigger_ai_response(img_container.images)  
    
    return model_response

async def __main__():
    await process_img("https://elperiodiquito.com/deportes/190189/alemania-continua-por-buen-camino-en-la-liga-de-naciones/")

# Run the async main function
if __name__ == "__main__":
    asyncio.run(__main__())
