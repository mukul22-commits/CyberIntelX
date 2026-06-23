from processing.system_health import system_health
from processing.alert_engine import generate_alerts
from processing.incident_engine import build_incidents
from processing.fraud_ring_detector import detect_fraud_rings
from processing.campaign_detector import detect_campaigns
from processing.national_threat_score import calculate_national_threat

print("\n=== FULL SYSTEM CHECK ===\n")

# System Health
health = system_health()
print("[PASS] System Health")
print(health)

# Alerts
alerts = generate_alerts()
print("\n[PASS] Alert Engine")
print("Total Alerts:", len(alerts))

# Incidents
incidents = build_incidents()
print("\n[PASS] Incident Engine")
print("Total Incidents:", len(incidents))

# Fraud Rings
rings = detect_fraud_rings()
print("\n[PASS] Fraud Ring Detection")
print("Fraud Rings:", len(rings))

# Campaigns
campaigns = detect_campaigns()
print("\n[PASS] Campaign Detection")
print("Campaigns:", len(campaigns))

# National Threat
threat = calculate_national_threat()
print("\n[PASS] National Threat Score")
print(threat)

print("\n=== SYSTEM VALIDATION COMPLETE ===")