# qeaml.github.io

My personal website. This is effectively a static site generator written in
Python with all the content seen on [qeaml.github.io](https://qeaml.github.io).

## Adding, modifying, and removing content

All of the pages are written in Markdown and stored in the [`pages`](pages)
directory. The structure of the `pages` directory corresponds to the layout
of the website. For example, `pages/about.md` will become `/about`, and
`pages/blog/2024/01/01/hello-world.md` will become
`/blog/2024/01/01/hello-world`.

All files in the `static` directory will be copied to the `/static` directory
of the website.

Templates used to render pages are stored in the [`templates`](templates)
directory. The website uses the [Mako] template engine.

Additionally, the `build.py` script supports extra syntax for adding
additional content to pages. This is done through so-called "meta" blocks.
These are blocks of text that are placed between two pairs of `---`, just like
the front matter. These meta blocks will be expanded to some HTML content
during rendering.

For example, to insert the `ChEn/portrait` template:

```
---
template: "ChEn/portrait"
char: "Gar28"
file: "Mirror.jpg"
charName: "Gar"
---
```

The keys other than `template` are passed as arguments to the template. The
`ChEn/portrait` template is located at `templates/ChEn/portrait.html`.

## Building & running

To build the website, activate the virtual environment and run the
`build.py` script. The convenience [`build`](build) script will do this for
you. To see the rendered output, simply run the
[`local_server.py`](local_server.py) script in another terminal and navigate to
[`localhost:9060`](http://localhost:9060). Whenever you re-run the `build.py`
script, the content shown by the local server will be updated. You will have to
refresh your browser to see the changes.

> [!IMPORTANT]
> The `local_server.py` script is not intended to be used in production. Only
> use it to preview changes.

## License

This project is licensed under the [BSD 3-Clause License](LICENSE).

[Mako]: https://www.makotemplates.org/
