# fetch_pdf.py
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from urllib.parse import urljoin

async def main():
    url = 'https://www.coopenae.fi.cr/ahorro-e-inversion'
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        await page.wait_for_timeout(5000)
        soup = BeautifulSoup(await page.content(), 'html.parser')
        section = soup.select_one('section.first_credito')
        pdf = section.select_one('a[href$=".pdf"]') if section else None
        if pdf:
            print("✅ PDF:", urljoin(url, pdf['href']))
        else:
            print("❌ PDF not found")
        await browser.close()

asyncio.run(main())
