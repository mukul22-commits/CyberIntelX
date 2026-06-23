import requests
import ipaddress


def get_ip_info(ip):

    result = {

        "ip": ip,
        "country": "Unknown",
        "region": "Unknown",
        "city": "Unknown",
        "org": "Unknown",
        "asn": "Unknown",
        "latitude": None,
        "longitude": None,
        "risk_level": "Low",
        "lookup_status": "Unknown"

    }

    try:

        ip_obj = ipaddress.ip_address(ip)

        if ip_obj.is_private:

            result["lookup_status"] = (
                "Private Network Address"
            )

            result["risk_level"] = "Low"

            return result

        response = requests.get(
            f"http://ip-api.com/json/{ip}",
            timeout=10
        )

        data = response.json()

        if data.get("status") != "success":

            result["lookup_status"] = (
                data.get(
                    "message",
                    "Lookup Failed"
                )
            )

            return result

        result["country"] = data.get(
            "country",
            "Unknown"
        )

        result["region"] = data.get(
            "regionName",
            "Unknown"
        )

        result["city"] = data.get(
            "city",
            "Unknown"
        )

        result["org"] = data.get(
            "org",
            "Unknown"
        )

        result["asn"] = data.get(
            "as",
            "Unknown"
        )

        result["latitude"] = data.get(
            "lat"
        )

        result["longitude"] = data.get(
            "lon"
        )

        result["lookup_status"] = (
            "Success"
        )

        if result["country"] in [

            "Russia",
            "China",
            "Iran",
            "North Korea"

        ]:

            result["risk_level"] = "High"

        else:

            result["risk_level"] = "Low"

    except Exception as e:

        result["lookup_status"] = str(e)

    return result


def lookup_ip(ip):

    return get_ip_info(ip)

def lookup_geoip(ip):

    return get_ip_info(ip)