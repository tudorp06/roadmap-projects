# My roadmap.sh projects

Small projects I build to practice specific concepts. Some are command-line tools, some have a web interface. I keep them here so the implementations and what I learned are in one place.

These are learning projects, separate from the products I ship. They are my implementations of project ideas from [roadmap.sh](https://roadmap.sh/projects), not official roadmap.sh projects.

## Implemented

| Project | What it does | What I practiced |
| --- | --- | --- |
| [Unit converter](projects/unit-converter) | Converts length, weight, and temperature with a pencil-style interface | DOM events, input handling, conversion formulas, and CSS |
| [GitHub activity CLI](projects/github-activity-cli) | Prints a user's public GitHub activity | HTTP requests, JSON, CLI arguments, and API errors |
| [GitHub trending CLI](projects/github-trending-cli) | Finds recently created repositories with the most stars | Query parameters, date ranges, argparse, and API limits |
| [Task tracker CLI](projects/task-tracker-cli) | Adds, updates, lists, and marks tasks stored in JSON | CRUD, file persistence, identifiers, and timestamps |
| [URL shortener](projects/url-shortener) | Stores a URL behind a short code and redirects visitors | Flask routes, SQL, persistence, request validation, and redirects |

## Structure

```text
projects/
  unit-converter/
  github-activity-cli/
  github-trending-cli/
  task-tracker-cli/
  url-shortener/
assets/
```

Each project has its own setup instructions and a short learning note. Existing standalone GitHub repositories stay available; this repository collects the implementations without removing them.

## Adding the next project

Create a folder under `projects/`, include the implementation and dependencies, and add a README covering what it does, how to run it, what I practiced, and what remains rough. Add it to the table above.

Project logos can live under `assets/<project-name>/` when I make them. No placeholder logos are included for now.
