from playwright.async_api import async_playwright


class Scraper:
    async def scrapePage(self, WEB_URL):
        async with async_playwright() as pw:

            # Launch the browser
            browser = await pw.chromium.launch(headless=False)
            context = await browser.new_context(viewport={"width": 1920, "height": 1080})

            # Go to new page, the page we will be working on
            page = await context.new_page()
            await page.goto(WEB_URL)

            for i in range(2, 29):

                # Choose a page
                element = await page.query_selector(f'#page{i}')

                # scroll to that page 
                await element.scroll_into_view_if_needed()
                await page.wait_for_timeout(100)

                if element:

                    div_element = await page.query_selector(f'#page{i}')
        
                    if div_element:
                        # Get the innerHTML of the div element
                        div_content = await div_element.inner_html()
        
                        # Write the content to a file
                        with open(f'./raw/div_content-{i}.html', mode="w", encoding='utf-8') as file:
                            file.write(div_content)
                            print(f'Content written to \'./raw/div_content{i}.html\'')
                    else:
                        print("Div not found")


            page_content = await page.content()

            # await browser.close()
            return page_content
