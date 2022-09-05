from mako.template import Template
from mako.lookup import TemplateLookup
from markdown import markdown
from pathlib import Path
from time import time
from shutil import copytree
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
    out_path = output_dir.joinpath(doc_name+".html")

    print(f"{e} => {out_path}")

    src = ""
    with e.open("rt") as f:
      src = f.read()

    body = markdown(src)
    title = doc_name.title()

    doc = template.render(body=body, title=title)

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
