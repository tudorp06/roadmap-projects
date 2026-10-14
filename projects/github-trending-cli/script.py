import argparse
import sys
from datetime import date, timedelta
import requests


parser = argparse.ArgumentParser(description="Github Trending CLI")
parser.add_argument("--duration", default="week", choices=("day", "week", "month", "year"))
parser.add_argument("--limit", type=int, default=10)

def days_ago(duration):
    curr_date = date.today()
    day_dict = {
        "day": 1,
        "week": 7,
        "month": 30,
        "year": 365
    }
    result = curr_date - timedelta(days=day_dict[duration])
    return result

def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    args = parser.parse_args()
    if not 1 <= args.limit <= 100:
        parser.error("--limit must be between 1 and 100")

    base_url = "https://api.github.com/search/repositories"
    params = {"q": f"created:>{str(days_ago(args.duration))}", "sort": "stars", "order": "desc", "per_page": args.limit}
    headers = {
        "User-Agent": "github-trendingcli (tudorxjh)"
    }

    try:
        resp = requests.get(base_url, params=params, headers=headers, timeout=10)
        resp.raise_for_status()
        repo_list = resp.json()
    except requests.RequestException as error:
        print(f"GitHub request failed: {error}", file=sys.stderr)
        return 1
    except ValueError:
        print("GitHub returned invalid JSON", file=sys.stderr)
        return 1

    parse_list = repo_list.get("items")
    if not isinstance(parse_list, list):
        print("GitHub response has no repository list", file=sys.stderr)
        return 1

    count = 0
    for repo in parse_list[:args.limit]:
        count += 1
        stars = repo["stargazers_count"]
        repo_name = repo.get("full_name") or ""
        language = repo.get("language") or ""
        description = repo.get("description") or ""
        url = repo.get("html_url") or ""
        str_answer = f"#{count}  ★{stars}  {repo_name}  {language}     {description}     {url}"
        print(str_answer)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
