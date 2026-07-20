import os
import pandas as pd

def run_data_scraper():
    print("[+] Запуск скрапера даних...")
    
    # Імітація зібраних даних з веб-сайту
    market_data = [
        {"ID": 101, "Title": "E-commerce Automation Script", "Category": "Python", "Price_USD": 150, "Status": "Completed"},
        {"ID": 102, "Title": "Telegram Customer Bot", "Category": "Bots", "Price_USD": 300, "Status": "Active"},
        {"ID": 103, "Title": "Real-time Crypto Alert System", "Category": "Analytics", "Price_USD": 250, "Status": "Active"},
        {"ID": 104, "Title": "Web Parsing & Data Extraction", "Category": "Scraping", "Price_USD": 180, "Status": "Completed"},
        {"ID": 105, "Title": "Automated Lead Generation Tool", "Category": "Marketing", "Price_USD": 220, "Status": "Active"},
    ]
    
    # Створення структурованого Dataframe
    df = pd.DataFrame(market_data)
    
    # Шлях до вихідного файлу
    output_filename = "extracted_market_data.xlsx"
    
    # Збереження у формат Excel
    df.to_excel(output_filename, index=False, engine='openpyxl')
    
    print(f"[УСПІХ] Зібрано {len(df)} записів.")
    print(f"[ЗБЕРЕЖЕНО] Файл створено: {os.path.abspath(output_filename)}")

if __name__ == "__main__":
    run_data_scraper()