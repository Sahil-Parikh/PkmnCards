from camera_recognition.card_recognition import identify_card_from_camera
from scraping.tcg_scraper import fetch_sales_data
import pandas as pd

EXCEL_FILE = "data/pokemon_data.xlsx"

def update_excel(card_info, sales, dates, avg_sales):
    """Update the Excel file with card data and sales information."""
    df = pd.read_excel(EXCEL_FILE)
    new_row = {
        "Pokemon Name": card_info["name"],
        "Pokemon Number": card_info["number"],
        "Set": card_info["set"],
        "5 Recent Sales & Dates": ', '.join([f"${s} ({d})" for s, d in zip(sales, dates)]),
        "Avg Sales": avg_sales,
        "Quantity": 1
    }
    df = df.append(new_row, ignore_index=True)
    df.to_excel(EXCEL_FILE, index=False)
    print("Data updated in Excel.")

def main():
    print("Recognizing card from camera...")
    card_info = identify_card_from_camera()
    
    if not card_info["name"]:
        print("Failed to recognize the card.")
        return
    
    print(f"Fetching sales data for {card_info['name']} ({card_info['set']})...")
    sales, dates, avg_sales = fetch_sales_data(card_info["name"], card_info["set"])
    
    if sales:
        print(f"Updating Excel with data for {card_info['name']}...")
        update_excel(card_info, sales, dates, avg_sales)
    else:
        print("Failed to fetch sales data.")

if __name__ == "__main__":
    main()
