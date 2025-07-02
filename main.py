import re

# === MOCK EMAIL DATA ===
mock_email_response = {
    "results": [
        {
            "id": "123456789",
            "properties": {
                "hs_email_direction": "INCOMING",
                "hs_email_status": "SENT",
                "subject": "Re: QUOTE#56789 - Demo request",
                "createdAt": "2025-06-15T15:20:00Z",
                "hs_email_text": "Hi, please send the revised quote.",
                "hs_email_from_email": "client@company.com"
            }
        }
    ]
}

# === MOCK DEAL DATA ===
mock_deals = [
    {
        "id": "deal_001",
        "properties": {
            "dealname": "Client Expansion Deal",
            "quote_number": "56789",
            "amount": "$15,000",
            "dealstage": "Scheduled"
        }
    },
    {
        "id": "deal_002",
        "properties": {
            "dealname": "Backup Deal",
            "quote_number": "11111",
            "amount": "$5,000",
            "dealstage": "Prospecting"
        }
    }
]

# === PROCESS EMAILS ===
for email in mock_email_response["results"]:
    subject = email["properties"].get("subject", "")
    match = re.search(r"QUOTE#(\d+)", subject)
    
    if match:
        quote_number = match.group(1)
        print(f"✅ Quote number found: {quote_number}")
        matched_deal = None
        
        # === MATCH WITH DEAL ===
        for deal in mock_deals:
            if deal["properties"]["quote_number"] == quote_number:
                matched_deal = deal
                break
        
        if matched_deal:
            print("🎯 Matching deal found:")
            print(f"Deal ID: {matched_deal['id']}")
            print(f"Deal Name: {matched_deal['properties']['dealname']}")
            print(f"Amount: {matched_deal['properties']['amount']}")
            print(f"Stage: {matched_deal['properties']['dealstage']}")
        else:
            print("❌ No matching deal found for this quote number.")
    else:
        print("❌ No quote number found in email subject.")

    print("-" * 40)
