from bs4 import BeautifulSoup


def parseContent(page_content):
    soup = BeautifulSoup(page_content, "html.parser")
    # Extract data using Beautiful soup

    # Clean html tags, remove invalid character
    parsed = ""

    parsed = soup.get_text()

    images = soup.find_all("img")
    
    if images:
        parsed = parsed + "\nImage Links in this page: \n"
        for img in images:
            if img.has_attr('src'):
                parsed = parsed + img['src'] + "\n"

    print("file parsed")
    return parsed
