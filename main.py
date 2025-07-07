import re
import requests
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
api_key = os.getenv("HUBSPOT_API_KEY")

if not api_key:
    raise ValueError("API key not found. Make sure .env file has HUBSPOT_API_KEY set.")

# Simulate receiving an email subject
email_subject = "Please review quote Q#0001 for approval"

# Extract quote number using regex
match = re.search(r'Q#\d{4}', email_subject)
if match:
    quote_number = match.group()
    print(f"Extracted Quote Number: {quote_number}")
else:
    print("No quote number found in the subject.")
    quote_number = None

# If quote number found, call HubSpot API to get deals
if quote_number:
    url = "https://api.hubapi.com/crm/v3/objects/deals"
    headers = {"Authorization": f"Bearer {api_key}"}
    params = {
        "properties": "dealname,hubspot_owner_id,dealstage,closedate",
        "limit": 100
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        deals = response.json().get("results", [])

        # Search for quote number in deal names
        found = False
        for deal in deals:
            deal_name = deal.get("properties", {}).get("dealname", "")
            if quote_number in deal_name:
                found = True
                print("\n✅ Match found!")
                print(f"Quote Number: {quote_number}")
                print(f"Deal Name: {deal_name}")
                print(f"Deal ID: {deal.get('id')}")
                print(f"Owner ID: {deal['properties'].get('hubspot_owner_id')}")
                print(f"Stage: {deal['properties'].get('dealstage')}")
                print(f"Close Date: {deal['properties'].get('closedate')}")
                break
        if not found:
            print("\n❌ No matching deal found with the extracted quote number.")
    except requests.exceptions.RequestException as e:
        print(f"\n🚨 Error calling HubSpot API: {e}")
