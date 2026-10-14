# Task tracker CLI

Stores tasks in a local JSON file and manages them from the terminal.

## Run

Requires Python 3. Run these commands from this folder:

```sh
python task.py add "Finish the converter"
python task.py list
python task.py update 1 "Document the converter"
python task.py mark done 1
python task.py list done
python task.py delete 1
```

An empty `tasks.json` is included.

## What I practiced

I practiced CRUD operations, JSON files, task IDs, timestamps, status filters, and command-line input.

## Notes

This is a local learning tool with basic error handling, not a multi-user task service.
