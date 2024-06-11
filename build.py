from dataclasses import dataclass
from mako.template import Template
from mako.lookup import TemplateLookup
from markdown import markdown
from pathlib import Path
from shutil import copytree
from typing import Optional
import yaml


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
class Page:
    config: Config
    path: str
    title: str
    section: str # which section of the website does this fall under
    desc: str
    keywords: list[str]
    content: str
    dst: Path

    @classmethod
    def parse(cls, config: Config, src: Path, dst: Path) -> "Page":
        raw_content = ""
        raw_meta = ""
        in_meta = False

        with src.open("rt") as f:
            for line in f:
                if in_meta:
                    if line.strip() == "---":
                        in_meta = False
                        continue
                    raw_meta += line
                    continue
                elif line.strip() == "---":
                    in_meta = True
                    continue
                raw_content += line

        path = src.relative_to(config.src).with_suffix("").as_posix()
        title_in_meta = False
        title = src.with_suffix("").name.capitalize()
        section = ""
        desc = "This page has no description."
        keywords = []
        keywords.extend(config.base_keywords)

        meta = yaml.load(raw_meta, Loader=yaml.Loader)
        if meta is not None:
            if "title" in meta:
                title = meta["title"]
                title_in_meta = True
            if "in" in meta:
                section = meta["in"]
            if "desc" in meta:
                desc = meta["desc"]
            if "keywords" in meta:
                keywords.extend(meta["keywords"])

        if title_in_meta:
            raw_content = f"# {title}\n\n{raw_content}"

        return cls(config, path, title, section, desc, keywords, raw_content, dst)

    def render(self):
        self.dst.parent.mkdir(parents=True, exist_ok=True)
        content = markdown(self.content)
        with self.dst.open("wt") as f:
            real_title = self.title
            if self.section != "":
                real_title += " :: " + self.section
            f.write(
                g_template.render(
                    body=content,
                    title=real_title,
                    desc=self.desc,
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
    pairs = find_all_pages(config, config.src)
    for pair in pairs:
        page = Page.parse(config, pair.src, pair.dst)
        page.render()

    copytree(config.static, config.out / "static", dirs_exist_ok=True)
    return 0


if __name__ == "__main__":
    from sys import argv

    exit(main(argv))
