import random
import string


def generate_officer_credentials(
    officer_name,
    case_id
):

    username = (
        officer_name.lower().replace(" ", "")
        + "_"
        + str(case_id)
    )

    password = "".join(

        random.choices(

            string.ascii_letters
            + string.digits,

            k=10

        )

    )

    return {

        "username": username,
        "password": password

    }