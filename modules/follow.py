from github import Github, GithubException
import datetime
import time

from misc.util import success_prefix, error_prefix


def follow(access_token: str, who_follow: str):
    g = Github(access_token)

    user = g.get_user(who_follow)
    followers = user.get_followers()
    counter = 0

    for user in followers:
        try:
            g.get_user().add_to_following(user)
            counter += 1
            print(success_prefix(f"The user {user.name} has been successfully followed (+{counter})."))
        except GithubException as e:
            if e.status == 403:
                print(error_prefix("Waiting for the end of rate limit."))
                reset_time = g.get_rate_limit().core.reset
                time_to_wait = reset_time - datetime.datetime.now(datetime.timezone.utc)
                time.sleep(time_to_wait.total_seconds())
