from b_lib.bbb import B_slack_post

def A_slack_post(user):
    print(f"A will call {B_slack_post}")
    B_slack_post(user)