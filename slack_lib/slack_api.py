def slack_post(user):
    slack_instance = SlackAPI(user)
    print(f"send_slack_msg will call {slack_instance.post} on {slack_instance}")
    slack_instance.post()


class SlackAPI:
    def __init__(self, user) -> None:
        self._user = user

    def post(self):
        print(f'send from class to user: {self._user}')
