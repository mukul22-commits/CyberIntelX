from processing.session_manager import (
    end_session
)


def logout_user(
    username
):

    end_session(
        username
    )

    return True