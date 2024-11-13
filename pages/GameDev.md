---
title: "Old Game Dev"
desc: "A collection of old screenshots documenting my game development adventures."
keywords: [GameDev]
---

A collection of old screenshots documenting my game development adventures.

Names in quotes are placeholders or codenames.

## The Ave Archipelago

Codenamed "Island Game" or "IG".

This is a game that begun development in January 2023 and was abandoned in April
2023, when I started work on [nwge] instead. The premise of the game was simple,
you would travel between various islands, each with a different purpose. Most
islands would have some sort of settlement for you to complete quests in. Some
quests advanced one of a few different storylines. The idea was that the choices
you make in these storylines would affect future games in the series. There were
also islands with specific purposes, such as a fishing island or an ave breeding
island.

Aves were in-universe dragon-like creatures that only lived in the archipelago.
There were two kinds of ave, each with slight anatomical differences and being
utilized by humans for different purposes.

The game was developed in C++ using SDL2. All rendering was performed in
software, which brought some limitations to the game. Additionally, starting
with no engine on such a complex project was frankly a stupid idea.

Due to my frustration with the project, I decided to abandon it and lift some of
the ideas into a new game engine project (nwge).

### Gallery

---
template: "gallery"
base: "GameDev/IG"
images:
  - file: "Console.png"
    caption: "Debugging the map system."
  - file: "Map.png"
    caption: "Last in-game screenshot."
  - file: "Isledit.png"
    caption: "<code>isledit</code> tool for editing maps."
---

## "Ooey"

ca. October 2022

This is a game for the [WASM-4] fantasy console. I never had any specific plans
for the game, it was just a fun project to work on.

The only real features implemented was a map system and a simple map editor.

### Gallery

---
template: "gallery"
base: "GameDev/Ooey"
images:
  - file: "Map.png"
    caption: "Fully implemented map system."
  - file: "Mapedit.png"
    caption: "Map editor."
---

## "Aeon"

ca. June 2022

This is another game for the [WASM-4] fantasy console. This was building up to
be a little Pokémon clone. Although I never got very far with it, I still look
upon it very firmly.

I particularly remember tearing my hair out over map rendering. I tried to
achieve a Generator 1 Pokémon-style map system, but ultimately failed.

Some of the monsters were originally designed by my sister and then turned into
in-game sprites based on her designs. This is by far the old game dev project
that has the most artwork.

### Gallery

---
template: "gallery"
base: "GameDev/Aeon"
images:
  - file: "Bestiary.png"
    caption: "Bestiary screen."
  - file: "BestiaryMonster.png"
    caption: "Viewing a monster in the Bestiary."
  - file: "Pause.png"
    caption: "Pause screen with placeholder text."
  - file: "Party.png"
    caption: "Party screen."
  - file: "PartyMonster.png"
    caption: "Viewing a monster in the party."
  - file: "Credits1.png"
    caption: "First page of the credits screen."
  - file: "Credits2.png"
    caption: "Second page of the credits screen."
  - file: "tbh.png"
    caption: "The 'Dummy' monster."
  - file: "Decimatu.png"
    caption: "The 'Decimatu' monster."
  - file: "Imus.png"
    caption: "The 'Imus' monster."
  - file: "ImusL.png"
    caption: "A larger sprite of Imus."
  - file: "ImusConcept.jpg"
    caption: "Concept art of Imus."
  - file: "Iontus.png"
    caption: "The 'Iontus' monster."
  - file: "IontusL.png"
    caption: "A larger sprite of Iontus."
  - file: "Xelus.png"
    caption: "The 'Xelus' monster."
  - file: "Xalia.png"
    caption: "The 'Xalia' monster."
---

## "Lidar"

Inspired by the [LIDAR Garry's Mod addon]. This is just a simple experiment to
try and replicate the effect in [Godot].

### Gallery

---
template: "gallery"
base: "GameDev/Lidar"
images:
  - file: "Cube.png"
    caption: "Dots on a cube."
  - file: "Entity1.png"
    caption: "Entity."
  - file: "Entity2.png"
    caption: "Entity."
---

## "BTPM"

ca. May 2022

BTPM, or **B**etter **T**hird **P**erson **M**ovement, is a small experiment to
try and implement a third person movement system in [Godot]. The game originally
started as just that, but I ended up adding a lot of abstract geometry for the
player to explore, as well as objects to interact with. The player is a skeleton
that makes Half-Life 1 footstep noises when walking around.

### Gallery

---
template: "gallery"
base: "GameDev/BTPM"
images:
  - file: "First.png"
    caption: "First ever screenshot."
  - file: "Atmo.png"
    caption: "Atmosphere."
  - file: "Map1.png"
    caption: "First map geometry."
  - file: "Map2.png"
    caption: "More intricate map geometry."
  - file: "Skeleton.png"
    caption: "The skeleton representing the player."
  - file: "Interaction.png"
    caption: "Interacting with an object - kicking a ball."
---

## "Thing Of Flash"

ca. December 2021

The entire gimmick of this [Godot] game is that you are given a flash beacon to
explore an abandoned facility at night. The gameplay is simple. Flash to see
what's in front of you, pick up batteries for more flashes, read notes to get
some of the lore, find keys to open doors, and find the exit. This is yet
another project that was too ambitious for me to finish.

### Gallery

---
template: "gallery"
base: "GameDev/TOF"
images:
  - file: "Batteries.png"
    caption: "Batteries laying on the ground."
  - file: "Pause.png"
    caption: "An in-progress pause screen."
  - file: "Map.png"
    caption: "Isometric screenshot of an earlier iteration of the map."
---

## "FPT"

FPT, or **F**irst **P**erson **T**est, is a small experiment to try and
implement a first person movement system in [Godot]. It involves a player
wander through a dark forest with a flashlight.

### Gallery

---
template: "gallery"
base: "GameDev/FPT"
images:
  - file: "Structure.png"
    caption: "A structure in an empty map."
  - file: "Forest1.png"
    caption: "An earlier iteration of the forest."
  - file: "Forest2.png"
    caption: "The forest."
---

[nwge]: /project/nwge
[WASM-4]: https://wasm4.org/
[LIDAR Garry's Mod addon]:
    https://steamcommunity.com/sharedfiles/filedetails/?id=2813176307
[Godot]: https://godotengine.org/
