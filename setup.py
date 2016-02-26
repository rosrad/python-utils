PACKAGE = "utils"
NAME = "utils"
DESCRIPTION = "utils files for python"
AUTHOR = "Bo Ren"
AUTHOR_EMAIL = "justnow.ren@gmail.com"
URL = "https://github.com/rosrad/python-utils"
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
)
