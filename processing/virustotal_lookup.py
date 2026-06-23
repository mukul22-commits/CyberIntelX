import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("VT_API_KEY")


def lookup_ip(ip):

    url = (
        f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    )

    headers = {
        "x-apikey": API_KEY
    }

    response = requests.get(
        url,
        headers=headers
    )

    if response.status_code != 200:

        return {
            "error":
            f"VirusTotal returned {response.status_code}"
        }

    return response.json()


def lookup_domain(domain):

    url = (
        f"https://www.virustotal.com/api/v3/domains/{domain}"
    )

    headers = {
        "x-apikey": API_KEY
    }

    response = requests.get(
        url,
        headers=headers
    )

    if response.status_code != 200:

        return {
            "error":
            f"VirusTotal returned {response.status_code}"
        }

    return response.json()


def lookup_url(url_value):

    url = "https://www.virustotal.com/api/v3/urls"

    headers = {
        "x-apikey": API_KEY
    }

    response = requests.post(
        url,
        headers=headers,
        data={
            "url": url_value
        }
    )

    if response.status_code not in [200, 202]:

        return {
            "error":
            f"VirusTotal returned {response.status_code}"
        }

    return response.json()