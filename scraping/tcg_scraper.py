import requests
from bs4 import BeautifulSoup

def fetch_sales_data(card_name, set_name):
    url = f"https://www.tcgplayer.com/search?productName={card_name}&set={set_name}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to fetch data for {card_name} ({set_name})")
        return None, None, 0

    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Update selectors based on the actual HTML structure
    sales = []
    dates = []
    for sale in soup.select('.sales-class'):  # Replace with correct class
        sales.append(float(sale.text.strip('$')))
    for date in soup.select('.date-class'):  # Replace with correct class
        dates.append(date.text.strip())
    
    # Only keep the 5 most recent sales
    if len(sales) > 5:
        sales = sales[:5]
        dates = dates[:5]
    
    avg_sales = sum(sales) / len(sales) if sales else 0
    return sales, dates, avg_sales

if __name__ == "__main__":
    card_name = input("Enter card name: ")
    set_name = input("Enter set name: ")
    sales, dates, avg_sales = fetch_sales_data(card_name, set_name)
    print(f"Sales: {sales}")
    print(f"Dates: {dates}")
    print(f"Average: ${avg_sales:.2f}")
