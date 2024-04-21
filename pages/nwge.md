---
desc: Story of the nwge engine.
---

# nwge

nwge (for **n**e**w** **g**ame **e**ngine, pronounced *nooj*) is small
game-oriented graphics-and-other-stuff engine.

## What does it do?

The nwge engine has 3 main purposes:

1. State management,
2. data loading,
3. rendering.

### State management

Nwge utilises a class-based approach to state management. Each major state your
game can be in is a separate class derived from one common, abstract `State`
class. As you switch between states the engine will automatically unload all the
data previously used by the state. The state then has various methods to
communicate to the engine what needs to be loaded. Additionally, the engine
provides a sub-state system. Sub-states are essentially smaller states that run
on top of one big main state. Sub-states are not allowed to load data, and as
such all necessary data must be passed from the main state to its sub-states.
Since the sub-states are internally stored on a stack, a sub-state can choose
whether sub-states below it in the stack are updated or rendered. This is useful
for a pause menu, for example: a pause menu sub-state would prevent the main
state from being updated while the user interacts with the menu.

### Data loading

Since nwge is not currently publically available, I cannot link to the lengthy
data system documentation here.

In short: the data system is based around queues, which allow the engine to only
load data while not in the middle of game playe -- most often during state
changes. The data system also provides access to bundle files for storing game
data and stores for persistent game data storage (game files, settings etc.).

### Rendering

Nwge has a simplistic renderer. It is effectively a kind-of-sort-of-lightweight
wrapper over plain OpenGL. It's mostly useful due to its built-in shaders and
textures making it easy to get a couple textured rectangles on screen alongside
some ASCII text.

### Other

Keep in mind that nwge is just a shared library. You can use just about any
system or 3rd-party libraries your heart desires. Nwge tries to be as flexible
to your needs as possible.

## Why does it exist?

Engineless gamedev is fun *apparently...* I decided to give it a shot,
developing a small game using SDL2. I realized pretty quickly that making the
engine at the same time as making the game caused a lot of non-reusable code in
the engine's part of the code. Eventually, I gave up on continuing development
of the game and utilised what little code I could to start a *new game engine*.
(updoot if you get the reference :3). By focusing on code reusability, I have a
pretty powerful solution I can freely reuse between as many game projects as I
wish! *(kind of the whole point of a game engine, no?)*. Due to it's bare-bones
nature, it supports any kind of game you could imagine. As of right now, the
best you'll be getting is basic 2D graphics, but if you're insane enough to
write your own shaders and everything in between -- anything is possible.
