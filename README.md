# Repo Tagger

[![Continuous Integration](https://github.com/bruno-fs/repo-tagger/actions/workflows/ci.yml/badge.svg)](https://github.com/bruno-fs/repo-tagger/actions/workflows/ci.yml)

An extremely simple action that will create a tag in your repo pointing to current commit.
If the tag already exists, the action won't fail, but also won't do anything.

By design, this is a very simple and won't do any parsing to guess which tag should be used.
Furthermore, this action won't create any release. Instead, this action can be used alongside
other actions to accomplish the creation of a release.

## Usage

Here's an example of how to use this action in a workflow file:

```yaml
name: Example Workflow

on:
  workflow_dispatch:
    inputs:
      tag:
        description: git tag that should be created
        required: true
        type: string

jobs:
  say-hello:
    name: Tag repo
    runs-on: ubuntu-latest
    permissions:
      contents: write # required to be able to write tags

    steps:
      # Change @main to a specific commit SHA or version tag, e.g.:
      # actions/repo-tagger@e76147da8e5c81eaf017dede5645551d4b94427b
      # actions/repo-tagger@v1.2.3
      - name: Tag repo
        id: tag-repo
        uses: actions/repo-tagger@main
        with:
          tag: "${{ inputs.tag }}"
        env:
          GITHUB_TOKEN: "${{ secrets.GITHUB_TOKEN }}"
```

For example workflow runs, check out the
[Actions tab](https://github.com/actions/repo-tagger/actions)!
:rocket:

## Inputs

| Input | Description                          |
| ----- | ------------------------------------ |
| `tag` | That that shall be added to the repo |

## Outputs

| Output | Description                        |
| ------ | ---------------------------------- |
| `tag`  | If created, tag name.              |
| `sha`  | If created, commit sha of the tag. |
