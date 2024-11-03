from pyppeteer import launch

class ImagesContainer:
    def __init__(self, images):
        self.images = images

async def data_collector(url):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)

    image_elements = await page.querySelectorAll('img')
    images = []

    for img in image_elements:
        img_src = await page.evaluate('(img) => img.src', img)
        images.append(img_src)

    await browser.close()

    return ImagesContainer(images=images)
