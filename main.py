import asyncio
import os
import sys

from contentParser import parseContent
from Scraper import Scraper


async def main():
    # Get the argument (website link)
    WEB_URL = getArgs()
    if WEB_URL:
        print(WEB_URL)

    # Create directory if not exists
    if not os.path.exists("./parsed/"):
        os.mkdir("./parsed")
    if not os.path.exists("./raw/"):
        os.mkdir("./raw")

    # Remove the parsed file if exists
    try:
        os.remove("./parsed/all_div.html")
    except OSError:
        pass

    # Launch the browser
    scr1 = Scraper()
    # Scrape the contents
    await scr1.scrapePage(WEB_URL)

    # Put into HTML file
    htmlStart = """
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Document</title>
   <link rel="stylesheet" href="../style.css">
</head>
<body>
    """
    htmlEnd = """
    <script src="../script.js"></script>
</body>
</html>
    """
    with open(f"./parsed/all_div.html", "a", encoding="utf-8") as htmlFile:
        htmlFile.write(htmlStart)

    for i in range(2, 29):
        with open(f"./raw/div_content-{i}.html", "r", encoding="utf-8") as file:
            html_content = file.read()
            
        with open(f"./parsed/all_div.html", "a", encoding="utf-8") as htmlFile:
            htmlFile.write(f'<section class="page">')
            htmlFile.write(html_content)
            htmlFile.write("<br>")
            htmlFile.write("</section>")

    with open(f"./parsed/all_div.html", "a", encoding="utf-8") as htmlFile:
        htmlFile.write(htmlEnd)

    with open("./parsed/all_div.html", "r", encoding="utf-8") as htmlFile:
        content = htmlFile.read()

    #
    #     parsed = parseContent(html_content)
    #
    #     with open(f'./parsed/div_content-{i}', 'w', encoding='utf-8') as file:
    #         file.write(parsed)
    #
    #     print(f'parsed {i}')


def getArgs():
    if len(sys.argv) > 2 and sys.argv[1].__eq__("--url"):
        return sys.argv[2]
    else:
        print("Please use the correct format: python main.py --url [URLs]")
        return


if __name__ == "__main__":
    asyncio.run(main())
