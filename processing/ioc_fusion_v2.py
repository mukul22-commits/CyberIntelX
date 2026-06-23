from processing.ioc_reputation import (
    evaluate_ioc
)

from processing.virustotal_lookup import (
    lookup_domain
)

from processing.whois_lookup import (
    get_whois
)

from processing.geoip_lookup import (
    lookup_ip
)


def investigate_ioc(ioc):

    result = {
        "ioc": ioc
    }

    try:

        result["reputation"] = (
            evaluate_ioc(ioc)
        )

    except Exception as e:

        result["reputation"] = {
            "error": str(e)
        }

    try:

        result["virustotal"] = (
            lookup_domain(ioc)
        )

    except Exception as e:

        result["virustotal"] = {
            "error": str(e)
        }

    try:

        result["whois"] = (
            get_whois(ioc)
        )

    except Exception as e:

        result["whois"] = {
            "error": str(e)
        }

    return result