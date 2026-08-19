<!--

---
jupyter:
  jupytext:
    hide_notebook_metadata: true
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.19.5
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

-->

Open [README.ipynb](README.ipynb) to view the full README (unfortunately github does not render notebook readme's)

# Pyprojectx demo project

> Clone the repo, run one command, everything works.

Onboarding on a Python project usually starts with a wall of instructions: install the right Python,
create a virtualenv, activate it (differently on Windows), install the dependencies, and then install
the linter, the formatter, the test runner and the build tool that CI happens to use.

[Pyprojectx](https://github.com/pyprojectx/pyprojectx) replaces all of that with a small `pw` script
that you commit next to your [pyproject.toml](./pyproject.toml). It bootstraps every tool your project
needs, on demand, in isolated environments inside the project directory.

If you have python 3.9+ and git, you're ready to go. There is nothing else to install: no jupyter,
no poetry, no ruff, not even pyprojectx itself.

```shell
git clone --branch poetry https://github.com/houbie/px-demo.git
cd px-demo
./pw notebook
```

That one command installed JupyterLab, installed this project in editable mode and opened the notebook
you are reading right now.

### Things to try

| Command | What happens |
|---|---|
| `./pw -i` | list every tool and alias, straight from `pyproject.toml` |
| `./pw build` | install dependencies, lint, test and build a wheel |
| `./pw poetry --help` or `./pw https --help` | run Poetry or HTTPie without ever installing them |
| `./pw post-json` | POST some json to pie.dev with HTTPie |
| `./pw c` | aliases resolve on a unique prefix (here: `check`) |
| `./pw pJ` | ... and on camel case initials (here: `post-json`) |
| `./pw --add mypy` | add a tool to the main context (writes it to `pyproject.toml`) |
| `./pw --clean build` | throw away all cached tools and prove it still works from scratch |

### Tired of typing `./pw`?

`./pw --install-px` installs the tiny `px` script in your home directory and adds it to your
PATH. After that:

* `px build` runs the project's aliases from any subdirectory, without the `./` prefix (and without
  the Windows/linux difference between `pw` and `./pw`)


## Your pyproject.toml *is* the build script

No Makefile, no `scripts/` directory full of shell scripts that only work on one OS:

```toml
[tool.pyprojectx.main]
requirements = ["poetry", "ruff", "prek", "px-utils", "httpie"]
post-install = "prek install"

[tool.pyprojectx.aliases]
install = "poetry install"
test = "poetry run pytest"
lint = ["ruff check"]
check = ["@lint", "@test"]
build = ["@install", "@check", "poetry build"]
```

* **Tools are declared, not documented.** Everything in `requirements` is installed on first use and
  pinned in [pw.lock](./pw.lock), so you, your colleagues and CI all run the exact same ruff.
* **Aliases compose.** `@lint` refers to another alias, which turns `./pw build` into a readable
  pipeline instead of a paragraph of setup instructions.
* **Contexts are isolated.** `[tool.pyprojectx.jupyter]` keeps JupyterLab's dependencies away from the
  `main` context, so Poetry never has to share an environment with JupyterLab.
* **Nobody forgets the git hooks.** `post-install = "prek install"` installs them the first time
  anyone runs `./pw`.


## Your project is already installed

Experimenting with your own code in a notebook takes exactly one command: `./pw notebook`. The project
is installed in editable mode, together with its dependencies.

**NOTE:** restart the notebook kernel to activate changes to the project's dependencies.

```python
import os
import shutil
import sys

# nothing was installed globally: this kernel and everything it can import
# live in a throw-away environment inside the project directory
print("python  :", os.path.relpath(sys.executable))
print("pycowsay:", os.path.relpath(shutil.which("pycowsay")))
```

```python
# the project and all its dependencies are automatically available here
from px_demo import moo

moo.say_moo()
```

## Nothing leaks onto your machine

The `pw` script installs every tool context in its own virtual environment under `.pyprojectx/`, much
like npm keeps everything in `node_modules`. Your system Python stays clean, two projects can happily
use two different ruff versions, and `./pw clean` undoes it all.

Commands and their arguments are forwarded to the right environment by typing `./pw` in front of them.


## Simplified CI/CD pipelines

Because the tools install themselves, there is no toolchain to set up in CI. The entire build step is:

```yaml
      - name: Test and build
        run: python pw --clean build
```

See it in action in this project's [github action workflow](.github/workflows/build.yml) or in the
[pyprojectx workflow](https://github.com/houbie/pyprojectx/tree/main/.github/workflows) for a bigger
example.

> **_NOTE:_**  If your CI/CD server runs on both linux and windows, you can merge the linux style
> `./pw build` and the windows style `pw build` into a single command: `python pw build`


## Use it in your own project

Copy `pw` and `pw.bat` into your repository, add a `[tool.pyprojectx]` section to your
_pyproject.toml_ and commit them. Later on, `./pw --upgrade` fetches the latest wrapper scripts.
See the [documentation](https://pyprojectx.github.io/) for all the details.

This branch uses [Poetry](https://python-poetry.org/), but pyprojectx doesn't care which dependency
manager you prefer: the same demo is available with [uv](https://github.com/houbie/px-demo/tree/main)
and [PDM](https://github.com/houbie/px-demo/tree/pdm) on sibling branches.
