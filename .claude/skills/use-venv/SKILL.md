---
name: use-venv
description: Activate the project's Python virtual environment in PowerShell.
---

# Use Venv

Use this skill when the user asks to activate the virtual environment for this project.

## Command

From the project root, run:

```powershell
.venv\Scripts\Activate.ps1
```

After activation, the terminal prompt should start with:

```text
(.venv)
```

## If Activation Fails

If PowerShell blocks activation scripts, tell the user to run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try again:

```powershell
.venv\Scripts\Activate.ps1
```

## Notes

This skill is for the user's interactive terminal workflow.

For one-off Claude Code shell commands, prefer calling the virtual environment's Python executable directly:

```powershell
.venv\Scripts\python.exe
```