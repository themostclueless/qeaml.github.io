from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime
from enum import StrEnum
from pathlib import Path
import xml.etree.ElementTree as ET


class ChangeFreq(StrEnum):
    always = "always"
    hourly = "hourly"
    daily = "daily"
    weekly = "weekly"
    monthly = "monthly"
    yearly = "yearly"
    never = "never"


@dataclass
class URL:
    loc: str
    lastmod: Optional[datetime] = None
    changefreq: Optional[ChangeFreq] = None
    priority: Optional[float] = None

    def as_element(self) -> ET.Element:
        parent = ET.Element("url")
        loc = ET.Element("loc")
        loc.text = self.loc
        parent.append(loc)
        if self.lastmod is not None:
            lastmod = ET.Element("lastmod")
            lastmod.text = self.lastmod.isoformat()
            parent.append(lastmod)
        if self.changefreq is not None:
            changefreq = ET.Element("changefreq")
            changefreq.text = str(self.changefreq)
            parent.append(changefreq)
        if self.priority is not None:
            priority = ET.Element("priority")
            priority.text = str(self.priority)
            parent.append(priority)
        return parent


@dataclass
class Sitemap:
    urls: list[URL] = field(default_factory=list)

    def add(self, *args, **kwargs) -> None:
        self.urls.append(URL(*args, **kwargs))

    def as_element(self) -> ET.Element:
        root = ET.Element("urlset")
        root.attrib["xmlns"] = "http://www.sitemaps.org/schemas/sitemap/0.9"
        for url in self.urls:
            root.append(url.as_element())
        return root

    def write(self, path: Path) -> None:
        if path.exists():
            path.unlink()
        with path.open("xb") as f:
            f.write(
                ET.tostring(self.as_element(), encoding="UTF-8", xml_declaration=True)
            )
