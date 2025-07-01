import re

# Mock dataset simulating HubSpot email response
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

# Script to extract quote numbers
for email in mock_email_response["results"]:
    subject = email["properties"].get("subject", "")
    match = re.search(r"QUOTE#(\d+)", subject)
    if match:
        quote_number = match.group(1)
        print(f"Email ID: {email['id']}")
        print(f"Quote number found: {quote_number}")
        print(f"From: {email['properties']['hs_email_from_email']}")
        print(f"Created At: {email['properties']['createdAt']}")
        print("-" * 40)
    else:
        print(f"No quote number found in email ID {email['id']}")