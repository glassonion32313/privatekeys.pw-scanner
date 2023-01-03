import requests
from bs4 import BeautifulSoup

def check_value():
    # Fetch the webpage
    response = requests.get('https://privatekeys.pw/keys/bitcoin/733168433274609637251439399157822078321036075022847522777729385446028817554')
    html = response.text

    # Parse the HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Find the element containing the value you want to check
    value_element = soup.find('span', {'class': 'badge'})
    if value_element is not None:
        value_text = value_element.text

        # Extract the value from the element's text
        value = int(value_text.replace('<i class="cf cf-btc" aria-hidden="true" title="" data-bs-toggle="tooltip" data-bs-original-title="BTC" aria-label="BTC"></i> ', ''))

        # Check the value and take action
        if value > 0:
            # Get the current URL
            url = response.url
            # Print the URL
            print(url)
        else:
            # Find the element with the random URL
            url_element = soup.find('a', {'class': 'page-link text-center'})
            # Extract the URL from the element
            url = url_element['href']
            # Fetch the webpage at the random URL
            response = requests.get(url)
            html = response.text
            # Do something with the HTML

# Initialize the counter
counter = 0

# Run the check continuously
while True:
    check_value()
    # Increment the counter
    counter += 1
    # Print the counter
    print(f'Checked {counter} pages')
