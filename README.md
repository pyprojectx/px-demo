# Pyprojectx demo project

Pyprojectx(https://github.com/houbie/pyprojectx) can turn your [pyproject.toml](./pyproject.toml)
config file into an executable build script.

You only need to download the wrapper scripts into your project directory (or any empty directory)
* osx / linux :
```shell
curl -LO https://github.com/houbie/pyprojectx/releases/latest/download/wrappers.zip && unzip wrappers.zip && rm -f wrappers.zip
```
* windows: unpack the [wrappers zip](https://github.com/houbie/pyprojectx/releases/latest/download/wrappers.zip)

and specify which tool(sets) you want to use in  _pyproject.toml_:
```toml
[tool.pyprojectx]
pdm = "pdm==1.12.6"
black = "black==21.7b0"
https = "httpie"
```

Things you can try out:
* show help: `./pw --help`
* show available tools and commands: `./pw --info`
* run a pdm command: `./pw pdm --help`
* use httpie to execute https commands: `./pw https --help`
* just type the first letters if you don't remember the full command: `./pw c`
* just type enough (camel case) letters to identify an aliased command:
  * `./pw post-json`  
  * `./pw pJ`
  * `./pw p`
