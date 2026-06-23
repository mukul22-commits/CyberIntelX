import whois
from datetime import datetime


def get_domain_info(domain):

    try:

        w = whois.whois(domain)

        creation = w.creation_date
        expiry = w.expiration_date

        if isinstance(creation, list):
            creation = creation[0]

        if isinstance(expiry, list):
            expiry = expiry[0]

        age_days = 0

        if creation:

            age_days = (
                datetime.now()
                - creation.replace(
                    tzinfo=None
                )
            ).days

        risk_score = 20
        risk_level = "Low"
        category = "Established Domain"

        if age_days < 30:

            risk_score = 95
            risk_level = "Critical"
            category = (
                "Newly Registered Domain"
            )

        elif age_days < 90:

            risk_score = 80
            risk_level = "High"
            category = (
                "Recent Registration"
            )

        elif age_days < 365:

            risk_score = 60
            risk_level = "Medium"
            category = (
                "Young Domain"
            )

        return {

            "domain": domain,
            "registrar": str(
                w.registrar
            ),
            "creation_date": str(
                creation
            ),
            "expiry_date": str(
                expiry
            ),
            "domain_age_days":
            age_days,
            "risk_score":
            risk_score,
            "risk_level":
            risk_level,
            "category":
            category

        }

    except Exception as e:

        return {

            "domain": domain,
            "registrar": "Unknown",
            "creation_date": "Unknown",
            "expiry_date": "Unknown",
            "domain_age_days": 0,
            "risk_score": 0,
            "risk_level": "Unknown",
            "category": f"Error: {e}"

        }


def get_whois(domain):

    return get_domain_info(domain)

def lookup_whois(domain):

    return get_domain_info(domain)