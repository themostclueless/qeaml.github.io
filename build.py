from mako.template import Template
from mako.lookup import TemplateLookup
from markdown import markdown
from pathlib import Path
from time import time
from shutil import copytree
import yaml
import traceback

def main(args):
  start = time()

  template = Template(filename="templates/main.html", lookup=TemplateLookup(directories=["."]))

  pages_dir = Path("pages")
  output_dir = Path("out")

  if not output_dir.exists():
    output_dir.mkdir()

  for e in pages_dir.iterdir():
    if e.is_dir() or not e.name.endswith(".md"):
      continue

    doc_name = e.name.removesuffix(".md")
    title = doc_name.title()
    desc = "This page has no description."
    out_path = output_dir.joinpath(doc_name+".html")

    print(f"{e} => {out_path}")

    meta_src = ""
    body_src = ""
    with e.open("rt") as f:
      for ln in f:
        if ln.strip() == "---":
          for ln2 in f:
            if ln2.strip() == "---":
              break
            meta_src += ln2
        body_src += ln

    body = markdown(body_src)
    meta = yaml.load(meta_src, Loader=yaml.Loader)
    if meta is not None and "title" in meta:
      title = meta["title"]
    if meta is not None and "desc" in meta:
      desc = meta["desc"]

    doc = template.render(
      body=body,
      title=title,
      desc=desc,
      fullURL=f"https://qeaml.github.io/{doc_name}")

    mode = "wt"
    if not out_path.exists():
      mode = "xt"
    
    with out_path.open(mode) as f:
      f.write(doc)

  copytree("static", "out/static", dirs_exist_ok=True)

  end = time()
  elapsed = end - start
  print(f"Finished in {elapsed:.2f}s")

  return 0

if __name__ == "__main__":
  from sys import argv
  try:
    exit(main(argv))
  except Exception as e:
    print("Uncaught exception in main:")
    traceback.print_exc()
    exit(100)
