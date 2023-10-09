from a_lib.aaa import A_slack_post

def send_slack_msg(user):
    print(f"send_slack_msg will call {A_slack_post}")
    A_slack_post(user)