import pandas as pd
import re

from processing.virustotal_lookup import (
    lookup_ip,
    lookup_domain
)


def is_ip(value):

    return re.match(
        r"^\d{1,3}(\.\d{1,3}){3}$",
        value
    )


def is_url(value):

    return value.startswith(
        ("http://", "https://")
    )


def enrich_ioc(ioc):

    try:

        # ------------------
        # IP ADDRESS
        # ------------------

        if is_ip(ioc):

            vt = lookup_ip(ioc)

            if "data" in vt:

                attr = vt["data"]["attributes"]

                stats = attr[
                    "last_analysis_stats"
                ]

                return pd.DataFrame([{

                    "ioc": ioc,
                    "type": "IP",

                    "country":
                    attr.get(
                        "country",
                        "Unknown"
                    ),

                    "asn":
                    attr.get(
                        "asn",
                        "Unknown"
                    ),

                    "malicious":
                    stats.get(
                        "malicious",
                        0
                    ),

                    "suspicious":
                    stats.get(
                        "suspicious",
                        0
                    ),

                    "reputation":
                    attr.get(
                        "reputation",
                        0
                    )

                }])

        # ------------------
        # URL
        # ------------------

        if is_url(ioc):

            return pd.DataFrame([{

                "ioc": ioc,
                "type": "URL",
                "status": "URL Lookup Ready"

            }])

        # ------------------
        # DOMAIN
        # ------------------

        vt = lookup_domain(ioc)

        if "data" in vt:

            attr = vt["data"]["attributes"]

            stats = attr[
                "last_analysis_stats"
            ]

            return pd.DataFrame([{

                "ioc": ioc,
                "type": "Domain",

                "reputation":
                attr.get(
                    "reputation",
                    0
                ),

                "malicious":
                stats.get(
                    "malicious",
                    0
                ),

                "suspicious":
                stats.get(
                    "suspicious",
                    0
                ),

                "harmless":
                stats.get(
                    "harmless",
                    0
                )

            }])

        return pd.DataFrame([{

            "ioc": ioc,
            "type": "Unknown"

        }])

    except Exception as e:

        return pd.DataFrame([{

            "ioc": ioc,
            "error": str(e)

        }])