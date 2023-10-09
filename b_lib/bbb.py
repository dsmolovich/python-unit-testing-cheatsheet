from c_lib.ccc import C_slack_post

def B_slack_post(user):
    print(f"B will call {C_slack_post}")
    C_slack_post(user)