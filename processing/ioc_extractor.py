import re


def extract_iocs(text):

    emails = re.findall(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        text
    )

    urls = re.findall(
        r'https?://[^\s]+',
        text
    )

    ips = re.findall(
        r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
        text
    )

    domains = re.findall(
        r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b',
        text
    )

    return {
        "emails": emails,
        "urls": urls,
        "ips": ips,
        "domains": domains
    }