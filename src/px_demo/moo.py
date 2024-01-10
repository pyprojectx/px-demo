import subprocess


def say_moo():
    subprocess.run(["pycowsay", "px moo!"], check=True)
