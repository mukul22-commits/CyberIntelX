from ioc_extractor import extract_iocs

text = """
Received email from fraud@fakebank.com

Visit:
https://fakebank-login.com

IP:
192.168.1.55
"""

print(
    extract_iocs(text)
)