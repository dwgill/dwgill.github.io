Personal site of Daniel Gill.

Process for setting it up:

    # clone the project
    # cd into the project dir
    git submodule update --init themes/flex
    python3.6 -m venv .venv 
    source .venv/bin/activate # different cmd for windows cmd prompt
    pip install -r requirements.pip

Then, in development, one can preview changes to the site with

    make clean && make html && make serve

That should run a local server on port 8000.

`make html` Should produce the "dev" codebase, `make publish` should produce
the "production" codebase. The primary difference between the two is that the
"dev" output just follows the configuration specified in `pelicanconf.py`,
whereas the "production" build follows the `publishconf.py` configuration,
which mimics the `pelicanconf.py` configuration and only specifies where it
differs.

Anyhow, publishing to github is then a matter of

    make clean && make github
