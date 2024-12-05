#!/usr/bin/env python3

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from shutil import copyfile, copytree

import yaml
from mako.lookup import TemplateLookup
from mako.template import Template
from markdown import Markdown

from sitemap import Sitemap


@dataclass
class Config:
    src: Path
    out: Path
    base_keywords: list[str]
    static: Path
    base_url: str


g_template = Template(
    filename="templates/main.html", lookup=TemplateLookup(directories=["."])
)


@dataclass
class PageBlock:
    is_text: bool  # if true, this is a regular markdown block of text
    raw: str  # if is_text, raw markdown text, raw YAML of meta block otherwise
    metadata: dict  # if is_text, empty dict, otherwise YAML metadata
    start_line: int
    end_line: int

    def render(self, markdown: Markdown) -> str:
        if self.is_text:
            return markdown.convert(self.raw)
        else:
            return self._render_meta(markdown)

    def _render_meta(self, markdown: Markdown) -> str:
        if "template" in self.metadata:
            template = self.metadata.pop("template")
            return Template(
                filename=f"templates/{template}.html",
                lookup=TemplateLookup(directories=["."]),
            ).render(**self.metadata)
        return f"<strong>Invalid meta block at lines {self.start_line}-{self.end_line}</strong>"


@dataclass
class Page:
    config: Config
    path: str
    title: str
    section: str  # which section of the website does this fall under
    desc: str
    thumb: str
    keywords: list[str]
    content: str
    dst: Path

    @staticmethod
    def _read_meta_block(line_iter, start_line: int) -> PageBlock:
        lines = []
        for line in line_iter:
            if line.strip() == "---":
                break
            lines.append(line)
        raw = "\n".join(lines)
        data = yaml.safe_load(raw)
        return PageBlock(False, raw, data, start_line, start_line + len(lines))

    @classmethod
    def parse(cls, config: Config, src: Path, dst: Path) -> "Page":
        blocks = []
        text_lines = []
        text_start_line = 1
        with src.open("rt") as f:
            line_iter = iter(f)
            line_no = 0
            for line in line_iter:
                line_no += 1
                if line.strip() == "---":
                    if len(text_lines) > 0:
                        blocks.append(
                            PageBlock(
                                True,
                                "".join(text_lines),
                                {},
                                text_start_line,
                                line_no,
                            )
                        )
                        text_lines = []
                    blocks.append(Page._read_meta_block(line_iter, line_no))
                    text_start_line = line_no + 1
                    continue
                text_lines.append(line)
        if len(text_lines) > 0:
            blocks.append(
                PageBlock(True, "".join(text_lines), {}, text_start_line, line_no)
            )

        path = src.relative_to(config.src).with_suffix("").as_posix()
        title_in_meta = False
        title = src.with_suffix("").name.capitalize()
        section = ""
        desc = "This page has no description."
        thumb = "/static/logo-small.png"
        keywords = []
        keywords.extend(config.base_keywords)

        meta_block = None
        if (not blocks[0].is_text) and blocks[0].metadata is not None:
            meta_block = blocks[0]
            meta = blocks[0].metadata
            if "title" in meta:
                title = meta["title"]
                title_in_meta = True
            if "in" in meta:
                section = meta["in"]
            if "desc" in meta:
                desc = meta["desc"]
            if "thumb" in meta:
                thumb = meta["thumb"]
            if "keywords" in meta:
                keywords.extend(meta["keywords"])

        if meta_block is not None:
            title_block = PageBlock(
                True, f"# {title}", {}, meta_block.start_line, meta_block.end_line
            )
            blocks = [title_block, *blocks[1:]]

        markdown = Markdown()
        raw_content = ""
        for block in blocks:
            if block.is_text:
                raw_content += block.raw
                raw_content += "\n"
            else:
                raw_content += block.render(markdown)
            continue
        content = markdown.convert(raw_content)
        # with dst.with_suffix(".tmp.md").open("wt") as f:
        #     f.write(raw_content)
        return cls(config, path, title, section, desc, thumb, keywords, content, dst)

    def render(self):
        self.dst.parent.mkdir(parents=True, exist_ok=True)
        with self.dst.open("wt") as f:
            real_title = self.title
            if self.section != "":
                real_title += " :: " + self.section
            f.write(
                g_template.render(
                    body=self.content,
                    title=real_title,
                    desc=self.desc,
                    thumb=self.thumb,
                    keywords=self.keywords,
                    fullURL=f"{self.config.base_url}/{self.path}",
                )
            )


@dataclass
class PathPair:
    src: Path
    dst: Path


def find_all_pages(config: Config, dir: Path) -> list[PathPair]:
    pairs = []

    for src in dir.iterdir():
        if src.is_dir():
            pairs.extend(find_all_pages(config, src))
            continue

        if not src.name.lower().endswith(".md"):
            continue

        dst = config.out.joinpath(src.relative_to(config.src)).with_suffix(".html")
        pairs.append(PathPair(src, dst))

    return pairs


def main(args: list[str]) -> int:
    config = Config(
        Path("pages"), Path("out"), [], Path("static"), "https://qeaml.github.io"
    )
    sitemap = Sitemap()
    pairs = find_all_pages(config, config.src)
    for pair in pairs:
        page = Page.parse(config, pair.src, pair.dst)
        page.render()
        stat = pair.src.stat()
        lastmod = datetime.fromtimestamp(stat.st_mtime)
        sitemap.add(config.base_url + "/" + page.path, lastmod=lastmod)

    sitemap.write(config.out / "sitemap.xml")
    copyfile("robots.txt", config.out / "robots.txt")
    copytree(config.static, config.out / "static", dirs_exist_ok=True)
    return 0


if __name__ == "__main__":
    from sys import argv

    exit(main(argv))
