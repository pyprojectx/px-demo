# Python Wraptor examples

The [Python Wraptor](https://github.com/houbie/python-wraptor) scripts bootstrap the installation of tools used by a
Python project.

Just add the *pw* and *pw.bat* scripts to your projects and configure the (Python based) tools
in your [pyproject.toml](./pyproject.toml)

## Zero effort tool installation
* Tutorials and open source projects: make sure that your audience can execute all your examples
  without making any assumptions about prerequisite tools
* Software projects: make sure that all team members use the correct (version of) tools and speed-up onboarding
  of new team members

```shell
# only prerequisite: make sure that python 3.7+ is on your path and cd into the project dir

# build the project and run unit tests
./pw poetry install
./pw test

# use common tools without the need to install them
# not everyone has curl installed; httpie to the rescue!
./pw http http://pie.dev/get
# do you regularly make the same http request? just create an alias
./pw postjson

# is your project running on AWS? Use the AWS CLI...
./pw aws --version
```

## Jupyter notebooks
Jupyter notebooks make it easy to experiment with your project's code and it can improve documentation.

I would not recommend adding Jupyter as dependency, as it can lead to version conflicts.

Here's how you can create a project specific kernel for your notebooks:

```shell
# install a kernel named wrapped-pi
./pw installkernel
# start the Jupyter notebook server
./pw nb
```

Now you can do the usual notebook things...

```python
# project dependencies are available in the custom kernel
import matplotlib.pyplot as plt
import numpy as np

%matplotlib inline

x = np.arange(0,4*np.pi,0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()

# same for your project's modules
from wrapped_pi.plot import simple_plot
simple_plot()
```
