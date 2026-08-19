# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A deliberately tiny demo project for [pyprojectx](https://github.com/pyprojectx/pyprojectx). The
Python code (`src/px_demo/moo.py` — one function that shells out to `pycowsay`) exists only to give
the build something to build. **The real content is `pyproject.toml` and `README.ipynb`**: this repo
is documentation-by-example, so config changes are usually the point, not incidental.

Sibling branches demonstrate the same project with other dependency managers: `main` (uv), `pdm`,
`poetry`. CI builds all three. A change to the demo story often needs porting across them.

## Commands

Everything runs through the `./pw` wrapper (`pw.bat` on Windows, or `python pw <cmd>` for
OS-agnostic CI). `pw` is a vendored copy of the pyprojectx bootstrap script — it installs tools into
isolated venvs under `.pyprojectx/` on first use, so **never `pip install` anything and never
activate a venv manually**.

| Command | Effect |
|---|---|
| `./pw build` | install + lint + test + `uv build` (what CI runs, as `python pw --clean build`) |
| `./pw check` | lint + test |
| `./pw test` | `uv run pytest` — append args, e.g. `./pw test tests/test_cowsay.py::test_cowsay` |
| `./pw lint` / `./pw format` | ruff check / ruff format + import sort |
| `./pw install` / `./pw update` | `uv sync` / `uv lock --upgrade` |
| `./pw run <cmd>` | run anything inside the project venv |
| `./pw notebook` | JupyterLab with the project installed editable |
| `./pw clean` | remove `dist`, `.venv`, `.ipynb_checkpoints` |
| `./pw -i` | list every available tool and alias (authoritative over this table) |

Aliases resolve on unique prefixes and camel-case initials: `./pw c`, `./pw pJ`. `./pw --clean`
(a wrapper flag, distinct from the `clean` alias) purges cached tool venvs before running.

## How the pyprojectx config is wired

- `[tool.pyprojectx.<name>]` blocks each define an isolated tool context. `main` holds uv/ruff/
  pre-commit/px-utils/httpie; `venv` maps to the uv-managed `.venv`; `jupyter` and `asciinema` are
  kept separate so their heavy deps never leak into the others.
- `scripts_ctx = "venv"` is why scripts in `bin/` can import `px_demo` directly.
- `main.post-install = "pre-commit install"` — hooks get wired up the first time any `./pw` command
  runs. The hooks call `pw format` and `pw lint`, so pre-commit needs `pw` on PATH.
- `pw.lock` pins the exact tool versions per context (separate from `uv.lock`, which pins project
  dependencies). Regenerate it by letting `./pw` reinstall, not by hand.

## Editing the README

`README.md` is **generated** from `README.ipynb` by jupytext (`./pw generate-readme`). Edit the
notebook, then regenerate — direct edits to `README.md` are lost. The notebook's code cells are
executed documentation and must keep working against the project.

## Style

ruff with `select = ["ALL"]`, line length 120, and a curated `ignore` list in `pyproject.toml`;
tests and `bin/` have per-file relaxations. Target is `requires-python = ">=3.8"` and CI tests 3.9
and 3.12 on Ubuntu and Windows, so keep code and aliases cross-platform (note the
`[tool.pyprojectx.os.win.aliases]` override for `clean`).
