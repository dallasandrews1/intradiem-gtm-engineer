import asyncio, os
from playwright.async_api import async_playwright

async def main():
    cwd = os.getcwd()
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page()
        for name, margin in [('cover', {'top':'0','bottom':'0','left':'0','right':'0'}),
                             ('body', {'top':'0.35in','bottom':'0.35in','left':'0','right':'0'})]:
            await pg.goto(f'file://{cwd}/{name}.html')
            await pg.wait_for_timeout(2500)  # let Google Fonts settle
            await pg.pdf(path=f'{name}.pdf', format='Letter', margin=margin, print_background=True)
        await b.close()

asyncio.run(main())
print('rendered')
