# Python Service

A minimal FastAPI HTTP service used to exercise the shared composite GitHub Action in this organization.

## Endpoints

| Method | Path      | Response                 |
|--------|-----------|--------------------------|
| GET    | `/`       | `"Hello, World!"`        |
| GET    | `/health` | `{ "status": "ok" }`    |

FastAPI also auto-generates interactive API docs at `/docs` (Swagger UI) and `/redoc`.

## Running locally

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt

python main.py                  # serves on :8000
# or
uvicorn app.main:app --reload   # dev mode with auto-reload
```

## Tests & linting

```bash
pytest                  # 3 tests
ruff check .            # lint
ruff format --check .   # format check
```

## GitHub Actions

The workflow at `.github/workflows/ci.yml` calls your organization's shared composite action.
Update the `uses:` line with your action's path and ref:

```yaml
- uses: my-org/actions/.github/actions/<your-action-name>@main
  with:
    python-version: "3.11"   # if your action takes this input
```
