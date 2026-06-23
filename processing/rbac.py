def has_access(
    role,
    feature
):

    permissions = {

        "Admin": [

            "all"

        ],

        "Officer": [

            "cases",
            "evidence",
            "timeline"

        ],

        "Analyst": [

            "intelligence",
            "reports",
            "ioc"

        ],

        "Viewer": [

            "reports"

        ]

    }

    if role == "Admin":

        return True

    return (
        feature
        in permissions.get(
            role,
            []
        )
    )