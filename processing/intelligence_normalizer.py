def classify_article(title):

    title = str(title).lower()

    category = "General"
    severity = "Low"
    confidence = 50
    mitre = "Unknown"
    threat_type = "Unknown"

    if any(x in title for x in [
        "ransomware",
        "lockbit",
        "encryptor"
    ]):

        category = "Ransomware"
        severity = "Critical"
        confidence = 95
        mitre = "T1486"
        threat_type = "Malware"

    elif any(x in title for x in [
        "phishing",
        "credential",
        "login",
        "spoof"
    ]):

        category = "Phishing"
        severity = "High"
        confidence = 88
        mitre = "T1566"
        threat_type = "Social Engineering"

    elif any(x in title for x in [
        "cve",
        "vulnerability",
        "exploit"
    ]):

        category = "Vulnerability"
        severity = "Critical"
        confidence = 92
        mitre = "T1190"
        threat_type = "Exploitation"

    elif any(x in title for x in [
        "malware",
        "trojan",
        "botnet"
    ]):

        category = "Malware"
        severity = "High"
        confidence = 85
        mitre = "T1204"
        threat_type = "Malware"

    elif any(x in title for x in [
        "breach",
        "leak",
        "stolen"
    ]):

        category = "Data Breach"
        severity = "High"
        confidence = 90
        mitre = "T1537"
        threat_type = "Data Theft"

    return {

        "category": category,
        "severity": severity,
        "confidence": confidence,
        "mitre": mitre,
        "threat_type": threat_type

    }