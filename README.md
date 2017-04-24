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

That should run a local server on port 8000. Publishing to Github is similarly a matter of

    make clean && make publish
