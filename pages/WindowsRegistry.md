---
desc: Registry tweaks to make Windows more usable.
---

# Windows Registry Tweaks

## `FastExplorer`

This registry tweak stops Explorer from opening every file in a folder to detect
the type of folder it is. For example, a folder with lots of images would
automatically be "optimized for Pictures". This requires that Explorer look
through every file in the folder, which can take a long time even on fast SSDs
if the folder has many files in it.

Make sure to inspect the registry file you download before applying it.

Download: [`FastExplorer.reg`][FastExplorer]

## `NoWebSearch`

This registry tweak disables Bing search from within the Windows search bar.
This not only improves the search speed but also prevents Windows from opening
Edge for no apparent reason other than to shill Bing.

Make sure to inspect the registry file you download before applying it.

Download: [`NoWebSearch.reg`][NoWebSearch]

## `UTC`

This registry makes Windows interpret the hardware clock time as UTC rather than
local time. This is useful if you have a dual-boot setup with Linux, as Linux
interprets the hardware clock time as UTC by default.

Make sure to inspect the registry file you download before applying it.

Download: [`UTC.reg`][UTC]

[FastExplorer]: /static/Windows/FastExplorer.reg
[NoWebSearch]: /static/Windows/NoWebSearch.reg
[UTC]: /static/Windows/UTC.reg
