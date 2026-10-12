# FastAPI Issue Tracker

A small REST API for creating and viewing issues. Issue data is stored locally in `data/issues.json`.

## Requirements

- Python 3.9 or newer

## Run locally

From the project root, create and activate a virtual environment, then install FastAPI with its standard extras:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install "fastapi[standard]"
fastapi dev main.py
```

The API is available at `http://127.0.0.1:8000`. Interactive API documentation is at `http://127.0.0.1:8000/docs`.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| `GET` | `/api/v1/issues/` | List all issues |
| `POST` | `/api/v1/issues/` | Create an issue |
| `GET` | `/api/v1/issues/{issue_id}` | Get an issue by ID; returns `404` if it does not exist |

Create an issue with a JSON body like this:

```json
{
  "title": "Login page error",
  "description": "The login page returns an error after submitting valid credentials.",
  "priority": "high"
}
```

`priority` can be `low`, `medium`, or `high`; it defaults to `medium`. New issues start with the `open` status. The API validates titles to 3–100 characters and descriptions to 10–500 characters.

## Data storage

Issues are read from and written to `data/issues.json`, relative to the working directory. Run the development server from the project root so the expected data file is used.