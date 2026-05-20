---
name: run-python-app
description: Run the Personal Calendar Assistant FastAPI app from the project root.
---

# Run Python App

Use this skill when the user asks to run, start, launch, or test the Personal Calendar Assistant app locally.

## Command

From the project root, run:

```powershell
python run.py
```

The app should start at:

```text
http://127.0.0.1:8000
```

## Before Running

Check that the virtual environment is active.

The terminal prompt should start with:

```text
(.venv)
```

If it is not active, run:

```powershell
.venv\Scripts\Activate.ps1
```

Then run:

```powershell
python run.py
```

## If Port 8000 Is Already In Use

Tell the user that another process is already using port `8000`.

Suggest either stopping that process or changing the port in `run.py`.