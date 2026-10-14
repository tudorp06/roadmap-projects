# GitHub activity CLI

Fetches recent public events for a GitHub username and prints them in the terminal.

## Run

Requires Python 3. Run `python script.py <username>`. On Windows, `github-activity.bat <username>` runs the same command. No third-party packages are required.

## What I practiced

I practiced urllib requests, JSON parsing, command-line arguments, mapping event types to messages, and handling HTTP or network errors.

## Notes

Only selected event types have friendly descriptions. It uses the public GitHub API and is subject to its request limits.
