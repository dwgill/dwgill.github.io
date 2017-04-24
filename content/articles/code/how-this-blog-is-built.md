title: This Blog Runs on Pelican
Date: 2017-04-21 13:53
Modified: 2017-04-24 10:51
Category: code
Tags: code, python, personal projects
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

    :::shell
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
available on [pelicanthemes.com][] and found [Flex][flex] to be to my
taste while not complicating things too much up front. Pelican seems to
half-expect you to install themes via the `pelican-themes` program
which is installed alongside Pelican, but that seems to operate by
installing themes on a system wide basis and I preferred to have the
project self-contained in my Git repo as much as possible. I ended up
going with putting the Flex's git repo in a git
[submodule][git-submodule] of my project repository. An introduction to 
Git is beyond the purview of this article (I got myself familiar with it 
with the [Code School course][git], personally), but
[Git submodules][git-submodule] aren't all that common, and as that's
what I ended up going with I figured I might detail what I did. At the
very least, it will be useful when I come back in a while wondering how
the devil you're supposed to handle a Git submodule.

I added the flex repo to my project like so:

    :::shell
    mkdir themes
    git submodule add https://github.com/alexandrevicenzi/Flex themes/flex

I'm unsure if this did both the work of formally adding the
submodule to the project (i.e. creating/modifying the `.gitmodules`
file) _and_ checking out the contents the submodule, but it may be the
case when a new submodule is added that you still need to initiate the
process of cloning/checking out the repo. You can do this with the
following:

    :::shell
    git submodule update --init themes/flex

With that command the entire contents of the [Flex][flex] repo should
be in the local directory `themes/flex`, which means I can now add the
theme to my Pelican configuration `pelicanconf.py`:

    :::python
    THEME = 'themes/flex'

The theme is straightforward enough, but not as documented as it could
be, and I'm having to figure out some details by looking at the
[test configuration][pelican-test]. For example, it turns out you need
to explicitly enable & configure the menu menu at the top of the page;
it doesn't just list whatever 'pages' you have on your site:

    :::python
    MAIN_MENU = True
    MENUITEMS = (
        ('Archives', '/archives.html'),
        ('Categories', '/categories.html'),
        ('Tags', '/tags.html'),
    )

Additionally—and I'm not sure if this is specific to the Flex theme or
how you configure it for Pelican sites in general—I found that the
Favicon could be configured by setting the `FAVICON` variable in my
configuration, like so:

    :::python
    PATH = 'content'
    STATIC_PATHS = ['images']
    FAVICON = '/images/favicon-red.ico'

In this case `images/` is a subdirectory of my `content/` folder, which
is where I put all of my site content, and futhermore I specify that
`images` is one of my `STATIC_PATHS`, which I believe means the contents
of `images` will be included in the generated site output irrespective of
whether Pelican finds any markdown posts in it to generate into articles.

I'm now going to try and get this site up on my Github pages, which means
if you're reading this you can expect an update shortly on how I did
that.

**UPDATE:**

So, getting it up on github pages had some snags. The biggest one I
learned—and I believe this is particular to the configuration of the
Flex theme—is that it is crucial that the `SITEURL` variable accurately
reflex whatever URL the reader's browser is using to access the page.
I had an initial goof where I set my `SITEURL` to `dwgill.github.com`
and it broke all the CSS, as the webpage was requesting all of its
assets at the wrong domain. The maddening thing was is that Github will
try to gracefully redirect you to the corresponding page on
`*.github.io`, but that is still enough to break assets, even if the
link ends up looking perfectly valid when I visit it in my browser.

The other tricky thing was setting up the CNAME, but the [Pelican
documentation lays that out][pelican-tips] pretty neatly (once you find
the corner of the documentation it's hidden in).

So, all told my configuration for github pages amounts to these lines in
my publish config file.

    :::python
    _use_custom_domain = True
    if _use_custom_domain:
        SITEURL = 'http://dwgill.com'
        try:
            STATIC_PATHS += ['extra/CNAME']
        except NameError: # STATIC_PATHS wasn't defined
            STATIC_PATHS = ['extra/CNAME']

        EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}
    else:
        SITEURL = 'https://dwgill.github.io'

This both sets the value of `SITEURL` and insures the `CNAME` file in
`/content/extra` will be output on the top level of the project as
`/CNAME`. The content of `CNAME` is just the following.

    dwgill.com

This basically means that Github will look at the content of that CNAME,
and any requests it receives at its ip addresses of `192.30.252.153` and
`192.30.252.154` addressed to `dwgill.com` will be served the files in
my project repo. All I had to do next was point my domain of
`dwgill.com` at those ip addresses. The documentation for this can be
found [here][ghpages-custom-domain].

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
[pelican-test]: https://github.com/alexandrevicenzi/Flex/blob/master/tests/pelicanconf.py
[pelican-tips]: http://docs.getpelican.com/en/stable/tips.html#extra-tips
[ghpages-custom-domain]: https://help.github.com/articles/setting-up-an-apex-domain/
