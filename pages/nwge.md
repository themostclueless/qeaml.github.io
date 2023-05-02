---
desc: Story of the nwge game development framework.

---

# nwge

nwge (for **n**e**w** **g**ame **e**ngine, pronounced *nooj*) is a lightweight game development framework, whose main purpose is to ease the most basic steps of creating a game.

## Selling points

### It is small

Fits in a single DLL providing all of the functionality within.

### It is very light

nwge is based around states. Every state the game could be in is contained insids its own unique class. The engine automatically calls the methods of the state object, handling all of the failures along the way. Using classes allows us to release resources once they are no longer needed. Utilities for passing data between states are also provided.

### Abstractions for modern programmmers

nwge's render system is a RAII-based wrapper of OpenGL. Provides you with `VertexBuffer`s, `Texture`s, `Shader`s & `ShaderProgram`s. Notably, the engine will ensure all `ShaderProgram`s have a vertex shader and a fragment shader attatched. If not, it will attach some built-in shaders for you. Another note is that nwge uses a different coordinate system to OpenGL. In the engine `(0, 0)` is the top left of the screen. In OpenGL, it is the center of the screen.

### Engineless feel

nwge is *not* an actual game engine. It is more of a *game development framework*, simply doing the most basic parts for you. It also provides options to customize its behavior to your liking.

## But why?

As I was developing a game without an engine, there were some bits of code that were built to be reused. The project I was working on was a rather large one. I eventually decided to put it on the back burner while I work on something smaller to "warm up". It was at this point I decided to split the most basic elements to a reusable library, so I can use it when I return to the big project.

## Is it not open source?

It will be. If I ever do release nwge, it will be after a game using it is released.
