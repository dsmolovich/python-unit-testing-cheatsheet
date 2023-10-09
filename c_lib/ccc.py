from slack_lib.slack_api import slack_post


def C_slack_post(user):
    print(f"C will call {slack_post}")
    slack_post(user)