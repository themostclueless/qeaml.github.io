from dataclasses import dataclass
from mako.template import Template
from mako.lookup import TemplateLookup
from markdown import markdown
from pathlib import Path
from shutil import copytree
from typing import Optional
import yaml

g_template = Template(filename="templates/main.html", lookup=TemplateLookup(directories=["."]))

@dataclass
class Page:
  path: str
  title: str
  desc: str
  keywords: list[str]
  content: str
  dst: Path

  @classmethod
  def parse(cls, root: Path, src: Path, dst: Path) -> "Page":
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

    path = src.relative_to(root).with_suffix("").as_posix()
    title_in_meta = False
    title = src.with_suffix("").name.capitalize()
    desc = "This page has no description."
    keywords = []

    meta = yaml.load(raw_meta, Loader=yaml.Loader)
    if meta is not None:
      if "title" in meta:
        title = meta["title"]
        title_in_meta = True
      if "desc" in meta:
        desc = meta["desc"]
      if "keywords" in meta:
        keywords = meta["keywords"]

    if title_in_meta:
      raw_content = f"# {title}\n\n{raw_content}"

    return cls(path, title, desc, keywords, raw_content, dst)

  def render(self):
    self.dst.parent.mkdir(parents=True, exist_ok=True)
    content = markdown(self.content)
    with self.dst.open("wt") as f:
      f.write(g_template.render(
        body=content,
        title=self.title,
        desc=self.desc,
        keywords=self.keywords,
        fullURL=f"https://qeaml.github.io/{self.path}"
      ))

@dataclass
class PathPair:
  src: Path
  dst: Path

def find_all_pages(out: Path, root: Path, dir: Path) -> list[PathPair]:
  pairs = []

  for src in dir.iterdir():
    if src.is_dir():
      pairs.extend(find_all_pages(out, root, src))
      continue

    if not src.name.lower().endswith(".md"):
      continue

    dst = out.joinpath(src.relative_to(root)).with_suffix(".html")
    pairs.append(PathPair(src, dst))

  return pairs

def main(args: list[str]) -> int:
  out = Path("out/")
  root = Path("pages/")

  pairs = find_all_pages(out, root, root)
  for pair in pairs:
    page = Page.parse(root, pair.src, pair.dst)
    page.render()

  static = Path("static/")
  copytree(static, out / "static", dirs_exist_ok=True)
  return 0

if __name__ == '__main__':
  from sys import argv
  exit(main(argv))
