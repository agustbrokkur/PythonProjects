import sys
from bs4 import BeautifulSoup
import requests

def main(args):
    # Only run program if there is an argument
    if len(args) == 0:
        return

    # Retreive the data
    data = requests.get(str(args[0]))

    # Load the data into soup
    soup = BeautifulSoup(data.text, "html.parser")

    # Get data from tr in the html
    for tr in soup.find_all("tr"):
        for td in tr.find_all("td"):
            for a in td.find_all("a"):
                print(a.text)

    # Find data from class
    for td in soup.find_all("td", { "class", "content" }):
        print(td.text)


# Same as static void main
if __name__ == "__main__":
    main(sys.argv[1:])
