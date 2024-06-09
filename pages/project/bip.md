---
title: Bip
desc:
    An overview and history of the design of qeaml's custom build system, bip.
keywords: [Bip, Build System, C++, Python]
---

**Bip**, for **b**uild **i**t **p**lease, is an extensible build system written
in Python. Although it is mostly focused on C/C++ projects, it can integrate
with other languages through its **plugin system**.

This is a general overview of the build system, take a peek at the [bip
documentation] for detailed information.

## Design

Bip was designed to simplify getting a C/C++ project up and running. It revolves
entirely around one **recipe file**. This recipe file defines the basic build
directories and language configuration as well as **components**. A component
may be an **executable**, **shared library** or a **plugin**. Each component
also specified what language it is written in. Bip will then invoke the correct
compiler for that language to build and link the component. For an example of
how such a recipe file work, see the [recipe file][nwge-template recipe] from
the nwge template repository.

Thanks to plugins, bip is very extensible. Plugins provide **lifetime
functions**, which help with a seamless integration with the build. Plugins may
be used for:

* Generating source code
* Packaging resources
* Updating build numbers
* and more!

Bip is also cross-platform by design. It supports multiple C++ compilers (uses
Clang whenever possible, defaulting to GCC or MSVC otherwise). It is able to
build projects on Linux and Windows from the same recipe file. Additionally,
components may define a **platform restriction**, where they will only be built
for certain platforms. This allows for easy separation of Linux-specific and
Windows-specific code in cases where no cross-platform solution exists.

## Origin

Bip begun as [qcbs], **q**eaml's **C**/C++ **b**uild **s**ystem. It was less
advanced, only being able to compile a single executable or shared library. As
such, I quickly begun work on bip instead to address that limitation. Bip then
gained support for many more compilers and many more compiler options, allowing
for more granular control of the build process.

My main reason for creating a build system was dissatisfaction from existing
solutions. While programs like CMake and Visual Studio are incredibly powerful,
I wanted something more dumbed-down. I also wanted something that was easy to
extend and modify.

While there are plenty of other choices out there (GNU Make, XMake, PreMake,
Meson, just to name a few!), none of them seem to fit my particular taste.
I like bip's component-oriented design. It's simple, easy to understand and
flexible. This may limit bip's ability to compile a more complex codebase, but
that's a sacrifice I'm willing to make.

## Future

Bip currently only supports C and C++ natively and plugins written in Python. I
do intend on expanding it beyond just these languages. Particularly, [Zig] has
caught my attention.

I am also seriously thinking about implementing **compatibility modes**, which
would allow bip to parse build files written for other build systems and then
emulate their behavior. This would ultimately allow for:

1. An easier transition to bip for existing projects
2. For bip to become a sort-of build orchestrator between multiple projects
   using different supported build systems
3. For bip to become a sort-of Swiss army knife of build systems.

Particularly, I'm thinking of implementing compatibility modes for
MSBuild/Visual Studio solutions, CMake and GNU Make.

[bip documentation]:
    https://github.com/qeaml/bip/tree/main/doc
[nwge-template recipe]:
    https://github.com/qeaml/nwge-template/blob/main/recipe.toml
[qcbs]: https://github.com/qeaml/bs
[Zig]: https://ziglang.org
