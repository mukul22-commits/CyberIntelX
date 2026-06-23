import pandas as pd


def correlate(ioc):

    findings = []

    if "185.220.101.1" in ioc:

        findings.append(
            "Known Tor Exit Node"
        )

    if "fakebank.com" in ioc:

        findings.append(
            "Associated With Fraud Emails"
        )

    if "paytm-security.xyz" in ioc:

        findings.append(
            "Known Phishing Domain"
        )

    return pd.DataFrame([{

        "ioc": ioc,
        "correlations":
        ", ".join(findings),
        "count": len(findings)

    }])