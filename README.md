# Pokémon Card Recognition and Sales Data Scraper

## Overview
This program identifies Pokémon cards using a camera, fetches recent sales data from TCGplayer, and updates the data in an Excel file.

## Folder Structure
- `camera_recognition/`: Handles image recognition.
- `data/`: Stores card data and Excel sheet.
- `scraping/`: Scrapes sales data from TCGplayer.
- `main.py`: Integrates all components.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Place `pokemon_data.xlsx` in the `data/` folder.
3. Run the program: `python main.py`

## Usage
1. Use a camera to recognize a card.
2. Input the set name when prompted.
3. Sales data is fetched and saved to `pokemon_data.xlsx`.
