# GitHub trending CLI

Finds the most-starred public repositories created within a selected time range. It uses repository search, not the ranking on GitHub’s Trending page.

## Run

Install with `python -m pip install -r requirements.txt`, then run `python script.py --duration week --limit 10`. Duration accepts day, week, month, or year; limit accepts 1 to 100.

## What I practiced

I practiced argparse, date calculations, request parameters, sorting search results, and reporting API failures.

## Notes

Anonymous GitHub API requests can be rate-limited. [Original standalone repository](https://github.com/tudorp06/github-trending-cli).
