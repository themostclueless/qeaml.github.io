---
desc: The story of the Skol programming language.
---

# Skol

## About

Skol (for **S**yz**k**rash **O**rdinary **L**anguage) is a programming language
I've developed for [a pretty long time][first-commit]. While it
doesn't have one specific purpose, it was a great learning experience to
develop. I do not work on the language anymore, but if you wish to continue its
legacy, the repository is public. One of the things that'll definitely catch you
off-guard is it's syntax, which actually has a pretty long history.

## Quick Overview

Skol was written in Go. The source code can be found [on GitHub][github].
If you want to learn the language, visit the [Skol Documentation][docs].

One of the ways I'd describe Skol is *minimalistic*. Mostly because I don't
want to spend the rest of my life working on it. Another reason is because I
wanted to create a language completely free of keywords. The goal was to be
able to name your variable, function or structure anything you'd like.

While Skol *does* mostly achieve this goal, a problem arises with functions.
Expressions do not exist in Skol, being replaced by calls to built-in functions.
Due to this the general recommendation is to use PascalCase for user-defined
functions and snake_case for built-in functions. A problem may also arise
when defining structures, as the primitive types' names are not case-sensitive.
This would cause confusion between a structure `B` and the boolean type (which
has multiple names: `b`, `bool` and `boolean`)

## Backstory

### Major influences

If you don't want to know the *entire* story of how Skol came to be and just
want to know what was the biggest influence on its syntax the below paragraph
is all you need to read.

The biggest influences are from 3 languages I've designed long before Skol.
When it comes to regular programming languages, influences include (but are not
limited to) Go, C, and Rust. [Code golf][codegolf] was also an influence toward
a more concise syntax.

### String interpolation

Skol's syntax stemmed off a concept for a string interpolation language I've
come up with extremely long ago. Back then, I was merely dreaming of what
could be. I can't recall exactly, but the basic syntax looked like this:

```
Hello %name!
```

While this seems pretty simple, the language offered more than just referring
to predefined name. Namely, function calls:

```
Hello $capitalize:%name
```

Quite an odd decision, but that lead me down a rabbit hole: What if there was
a syntax to *define* a function?

```
$?capitalize[name]
  ...
$
Hello $!capitalize:%!name
```

At this point this was becoming less and less string interpolation, but just
straight up programming.

### Datasets

Another language that ended up playing a big influence on Skol's syntax is a
dataset language.

Two flavors of the language existed. One for un-keyed data (array data):

```
somebody
once
told
me
```

And one for keyed data (dictionary data):

```
somebody -> once
told -> me
```

Of course, it took inspiration from that string interpolation language, and
included references:

```
@ comments are denoted with the at sign (@)
somebody
once
told
me
@ produces "somebody once told me"
^$0 ^$1 ^$2 ^$0
```

The syntax for dictionary data was slightly different:

```
somebody -> once
told -> me
sentence -> somebody ^:somebody told ^:told
```

But I didn't stop there. You could cross-reference values between files.

If we assume "dataset1" contains:

```
somebody
me
```

Then:

```
sentence -> ^!dataset1$0 once told ^!dataset1$1
```

***But wait!*** *There's more:* **Random chance!**

```
@ 50% of the time:
@  "somebody once told me"
@ the other 50%:
@  "somebody once told"
sentence -> somebody once told ^?50!dataset1$1
```

Why would you need random chance in a dataset language? *I have no idea!*

I never got around to implementing either of these languages. I'm pretty sure
the reason is obvious. But the inspiration Skol took from these concepts is
pretty clear.

### Exk

However, before I implemented Skol, I wanted to implement a language called
*Exk*. It is a direct predecessor of Skol. Here's what a piece of Exk code
(would) look like:

```exk
?$add_and_print a int; b int {
  ?%val = !$math::add a; b
  !$std::println !$std::to_str !%val
}
```

Personally, I'd take Skol's syntax over Exk's any day of the week.

### Rough timeline of events

<table>
<tr>
<th>Time span</th><th>Event</th>
</tr>
<tr>
<td>~2020</td><td>Creation of the string interpolation language.</tr>
<td>~Late 2020</td><td>Creation of the dataset language.</tr>
<td>April 2021</td><td>Finalization of the dataset language.</tr>
<td>February 2022</td><td>Creation of Exk.</tr>
<td>May 2022</td><td>Creation of Skol.</tr>
</tr>
</table>

[first-commit]: https://github.com/syzkrash/skol/commit/70acb244b2ba74344e5ed1c0717b4606975e9fa0
[github]: https://github.com/syzkrash/skol
[docs]: https://syzkrash.github.io/skol
[codegolf]: https://en.wikipedia.org/wiki/Code_golf
