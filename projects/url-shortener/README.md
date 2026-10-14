# URL shortener

A Flask app that saves a URL under a six-character code and redirects that code to the original URL.

## Run

Install with `python -m pip install -r requirements.txt`, then run `python app.py`. Open http://localhost:3000. SQLite is used by default. `DATABASE_URL` enables the PostgreSQL connection path.

## What I practiced

I practiced Flask endpoints, JSON requests and responses, validation, parameterized SQL, unique short codes, and HTTP redirects.

## Notes

This personal implementation has basic validation and no abuse-prevention system. [Original standalone repository](https://github.com/tudorp06/Personal-URL-shortener).
