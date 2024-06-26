#!/usr/bin/env python3

import subprocess
import os
import sys

github_api_token = (
    os.getenv("CHANGELOG_GITHUB_TOKEN") if os.getenv("CHANGELOG_GITHUB_TOKEN") else input("Enter Github API token: ")
)

if len(sys.argv) < 2:
    raise Exception("Provide a version number as parameter (--future-release argument)")

version = sys.argv[1]

cmd = [
    "github_changelog_generator",
    "-t",
    github_api_token,
    "-u",
    "locustio",
    "-p",
    "locust",
    "--exclude-labels",
    "duplicate,question,invalid,wontfix,cantfix,stale",
    "--header-label",
    "# Changelog\nNote that the latest version is usually missing here, check [github](https://github.com/locustio/locust/releases) for the latest info.",
    "--since-tag",
    "1.0.1",
    # "--since-commit", # these cause issues
    # "2020-07-01 00:00:00",
    "--future-release",
    version,
]

print(f"Running command: {' '.join(cmd)}\n")
subprocess.run(cmd)
