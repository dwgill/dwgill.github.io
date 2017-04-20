title: This Blog Runs on Pelican
Date: 2017-04-20 12:00
Modified: 2017-04-20 12:00
Category: code
Tags: code, python, pelican, projects
Slug: this-blog-runs-on-pelican
Authors: Daniel Gill
Summary: A detailed breakdown of how this blog is coded & built

This blog is built using the [Pelican][pelican] static site generator,
written in [Python][python], and utilizes the [Flex][flex] pelican theme.
I'm actually writing this post as I set up the site for the first time,
partially so that I can document everything for myself, and hopefully
because it will be of some use for anyone else who finds him-or-herself
dealing with this in the future.

Pelican is a static site generator, which means basically that allows me
to write content for this blog in simple [Markdown][markdown] files,
and uses those files to generate the individual pages of this website.
It takes my markdown files as input, and outputs the entire body of
html files that comprise this website. I can then take those html
files and host them anywhere I like—on my own server, or on 
[Github Pages][ghpages], etc.

Pelican has a pretty simple quickstart process, which can be found
[here][pelican-quickstart]. Altogether my first steps looked like the
following:


    cd <project_dir>
    virtualenv .venv
    source .venv/bin/activate
    pip install pelican markdown
    pelican-quickstart


That was straightforward enough (the living hell of trying to figure)
out a name for this blog notwithstanding), but the next step was
bettering the look of the site. The default look of Pelican is not the
greatest. For example, [here][pelican-site] is the official Pelican
website at the time of this writing:

![getpelican.com circa 2017]({filename}/images/code/getpelican-site-2017-04-20.png)

Not my style, and not responsive besides. I looked through the themes
available on [pelicanthemes.com][] and found [Flex][flex] to my taste
while not complicating things too much up front. Pelican seems to
half-expect you to install themes via the `pelican-themes` program
which is installed alongside Pelican, but that seems to operate by
installing themes on a system wide basis and I preferred to have the
project self-contained in my Git repo as much as possible. I ended up
going with putting the Flex's git repo in a git [submodule][git-submodule]
of my project repository. An introduction to Git is beyond the purview
of this article (I got myself familiar with it with the
[Code School course][git], personally), but
[Git submodules][git-submodule] aren't all that common, and as that's
what I ended up going with I figured I might detail what I did. At the
very least, it will be useful when I come back in a while wondering how
the devil you're supposed to handle a Git submodule.

I added the flex repo to my project like so:

    mkdir themes
    git submodule add https://github.com/alexandrevicenzi/Flex themes/flex

I'm unsure if this did both the work of the formally adding the
submodule to the project (i.e. creating/modifying the `.gitmodules`
file) _and_ checking out the contents the submodule, but it may be the
case when a new submodule is added that you still need to initiate the
process of cloning/checking out the repo. You can do this with the
following:

    git submodule update themes/flex

With that command the entire contents of the [Flex][flex] repo should
be in the local directory `themes/flex`, which means I can now add the
theme to my Pelican configuration:

    THEME = 'themes/flex'

[pelican]: https://blog.getpelican.com/
[python]: https://en.wikipedia.org/wiki/Python_(programming_language)
[flex]: https://github.com/alexandrevicenzi/Flex
[markdown]: https://en.wikipedia.org/wiki/Markdown
[ghpages]: https://pages.github.com/
[pelican-quickstart]: http://docs.getpelican.com/en/stable/install.html
[pelican-site]: https://blog.getpelican.com/
[pelicanthemes.com]: http://www.pelicanthemes.com/
[git]: https://www.codeschool.com/courses/git-real
[git-submodule]: https://git-scm.com/docs/git-submodule