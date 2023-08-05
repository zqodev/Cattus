from github import Github, GithubException
import datetime
import time

from misc.util import success_prefix, error_prefix


def unfollow(access_token: str):
    g = Github(access_token)

    user = g.get_user()
    following = user.get_following()
    counter = 0

    for user in following:
        try:
            g.get_user().remove_from_following(user)
            counter += 1
            print(success_prefix(f"The user {user.name} has been successfully unfollowed (-{counter})."))
        except GithubException as e:
            if e.status == 403:
                print(error_prefix("Waiting for the end of rate limit."))
                reset_time = g.get_rate_limit().core.reset
                time_to_wait = reset_time - datetime.datetime.now(datetime.timezone.utc)
                time.sleep(time_to_wait.total_seconds())
