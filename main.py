import os

from github import Github
from github import GithubException


GH_TOKEN_REQUIRED_PERMISSION = (
    "The minimum permission required to write a tag is 'contents: write'."
)
REF_REQUIRED_TOKEN_PERMISSION = "See https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/controlling-permissions-for-github_token"


def main():
    tag = os.environ["INPUT_TAG"]
    try:
        g = Github(os.environ["GITHUB_TOKEN"])
    except KeyError:
        print("secret GITHUB_TOKEN is required.")
        exit(1)
    repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])
    sha = repo.get_commits()[0].sha
    try:
        repo.create_git_ref(f"refs/tags/{tag}", sha)
    except GithubException as err:
        if err.status == 403:
            print(GH_TOKEN_REQUIRED_PERMISSION)
            print(REF_REQUIRED_TOKEN_PERMISSION)
            exit(1)
        elif err.status == 422:
            print("Tag already exists. Won't do anything...")
            exit(0)
        raise err

    with open(os.environ["GITHUB_OUTPUT"], mode="at") as output:
        print(f"tag={tag}", file=output)
        print(f"sha={sha}", file=output)


if __name__ == "__main__":
    main()
