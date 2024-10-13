import requests
from bs4 import BeautifulSoup
from colorama import init, Fore

init(autoreset=True)

def whois_lookup(domain):
    try:
        print(Fore.YELLOW + f"Looking up WHOIS information for: {domain}\n")

        # Requesting the whois page from whois.com
        url = f"https://www.whois.com/whois/{domain}"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception("Failed to retrieve data from whois.com")

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Check if the div containing WHOIS info exists
        whois_data_div = soup.find("div", {"class": "df-block"})
        
        if whois_data_div is None:
            raise Exception("Domain not found or not registered")

        # Extract and display the WHOIS result
        whois_data = whois_data_div.get_text(separator="\n").strip()

        print(Fore.CYAN + "WHOIS Information:\n")
        print(Fore.GREEN + whois_data)

        print(Fore.GREEN + "\nWHOIS Lookup completed successfully.")
    except Exception as e:
        print(Fore.RED + f"Error performing WHOIS lookup: {e}")

if __name__ == "__main__":
    domain = input("Enter the domain name: ")
    whois_lookup(domain)
