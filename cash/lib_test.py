import json
import requests
import amazonlib
from datetime import datetime

WEBHOOK_FILE = 'amazon.txt'

def save_webhook(webhook_url):
    with open(WEBHOOK_FILE, 'w') as f:
        f.write(webhook_url)

def load_webhook():
    try:
        with open(WEBHOOK_FILE, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def send_to_discord(webhook_url, payload):
    response = requests.post(webhook_url, json=payload, headers={'Content-Type': 'application/json'})
    if response.status_code != 204:
        print('failed to send webhook payload', response.status_code)
    else:
        print('sent/.')

def add_or_update_webhook():
    webhook_url = input("enter your webhook url: ")
    save_webhook(webhook_url)
    print("sent/.")

def run_script():
    webhook_url = load_webhook()
    if webhook_url is None:
        print("Error: Url not set")
        return

    amz = amazonlib.Amazon(dbg=False)
    search = input("Enter item/product: ")
    maxpages = amz.getMaxPagesBySearchText(search)
    
    for x in range(maxpages):
        searchresult = amz.getSearchResultFromText(search, page=x)
        
        for item in searchresult:
            try:
                iteminfo = amz.getItemResult(item['link'])
                timestamp = datetime.utcnow().isoformat()  
                
                embed = {
                    "title": item['itemname'],
                    'description': f'Price: {item["price"]}\nRating: {iteminfo["rating"]}\nOld Price: {iteminfo["wasprice"]}\nYou Save: {iteminfo["saveprice"]}',
                    "url": item['link'],
                    "color": 0x800080, 
                    "footer": {
                        "text": f"Amazon Scrap • {timestamp}"
                    },
                    "author": {
                        "name": "Amazon Scraper",
                        "icon_url": "https://imgs.search.brave.com/HgJvzrak9qJbUerSw1_Oe8zQgTaAEZqKOrQ6FyBlifQ/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9zdGF0/aWMtMDAuaWNvbmR1/Y2suY29tL2Fzc2V0/cy4wMC9hbWF6b24t/aWNvbi0yNTZ4MjU2/LWloemk1ZWJyLnBu/Zw"  
                    },
                    "thumbnail": {
                        "url": "https://cdn.discordapp.com/attachments/1202429230873448450/1205609018513428580/7200271a3ed5491093ca7d5a57b74c21.png?ex=65d8fde5&is=65c688e5&hm=0c726cca8cddced252b75d68ef10693a1cf3b01f83d5cec2dbc1ace2655305a9&"  
                    }
                }
                
                payload = {
                    'embeds': [embed]
                }
                
                send_to_discord(webhook_url, payload)
                
            except Exception as e:
                print(f'Error: {e}')

def main_menu():
    print("Main Menu:")
    print("1. Add/Update Discord webhook URL")
    print("2. Run the script")
    print("3. Exit")

    choice = input("Enter your choice: ")
    return choice

if __name__ == '__main__':
    while True:
        choice = main_menu()

        if choice == '1':
            add_or_update_webhook()
        elif choice == '2':
            run_script()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose again.")

