import pandas as pd


def verify_ioc(ioc):

    sources = []

    if "paytm-security.xyz" in ioc:
        sources.append("Domain Intelligence")

    if "fakebank.com" in ioc:
        sources.append("Email Intelligence")

    if "185.220.101.1" in ioc:
        sources.append("IOC Enrichment")

    if "44d88612fea8a8f36de82e1278abb02f" in ioc:
        sources.append("Hash Intelligence")

    source_count = len(sources)

    if source_count >= 3:

        confidence = 95
        verdict = "Verified Malicious"

    elif source_count == 2:

        confidence = 80
        verdict = "Likely Malicious"

    elif source_count == 1:

        confidence = 60
        verdict = "Suspicious"

    else:

        confidence = 10
        verdict = "Unknown"

    return pd.DataFrame([{

        "ioc": ioc,
        "sources": ", ".join(sources),
        "matches": source_count,
        "confidence": confidence,
        "verdict": verdict

    }])