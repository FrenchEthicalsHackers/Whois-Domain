
# WHOIS Domain Lookup Tool

This is a simple Python script that allows you to perform WHOIS lookups on domain names. It retrieves and displays registration information such as the domain's registrar, creation date, expiration date, and more. This tool does not require any API key and fetches data directly from **whois.com**.

## Features
- No API key required.
- Provides WHOIS details for any domain.
- Informs you if the domain is not found or unregistered.
- Clean and color-coded output for easy readability.

## Requirements
- Python 3.x
- The following Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `colorama`

You can install these libraries using pip:
```bash
pip install requests beautifulsoup4 colorama
```

## How to Use
1. Clone or download this repository.
2. Install the required libraries listed above.
3. Run the script and enter a domain name when prompted:
   ```bash
   python WhoisTool.py
   ```
4. Enter the domain name you wish to look up (e.g., `google.com`).
5. The script will retrieve and display the WHOIS information, or let you know if the domain is unregistered.

### Example
```bash
$ python WhoisTool.py
Enter the domain name: google.com

Looking up WHOIS information for: google.com

WHOIS Information:
Domain Name: GOOGLE.COM
Registry Domain ID: 2138514_DOMAIN_COM-VRSN
Registrar WHOIS Server: whois.markmonitor.com
Registrar URL: http://www.markmonitor.com
...
```

If the domain is not found or unregistered:
```bash
$ python WhoisTool.py.py
Enter the domain name: nonexistingdomain.xyz

Error performing WHOIS lookup: Domain not found or not registered
```

## License
This project is open-source and available under the MIT License.
