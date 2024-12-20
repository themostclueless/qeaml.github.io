---
title: "Old Game Dev"
desc: "A collection of old screenshots documenting my game development adventures."
keywords: [GameDev]
---

A collection of old screenshots documenting my game development adventures.

Names in quotes are placeholders or codenames.

## WBYH

ca. June 2024

WBYH, or **W**hat **B**rings **Y**ou **H**ere, is a game similar in purpose to
the roulette game described below, also based on [nwge]. This game, however,
simply focused on Manitch, the player character, having a conversation with
Ata. The game would focus long dialogues between the two, with the player
character having to choose between different conversation topics every so often.
Every choice would lead the player to a different path in the conversation,
meaning one would have to replay the game multiple times to see all the possible
outcomes.

### Gallery

---
template: "gallery"
base: "GameDev/WBYH"
images:
  - file: "MainMenu.png"
    caption: "An early main menu."
  - file: "Scene.png"
    caption: "A scene with Manitch and Ata."
  - file: "AtaScene.png"
    caption: "A scene with Ata."
  - file: "End.png"
    caption: "The end of the game."
  - file: "AtaSprite.png"
    caption: "One of Ata's sprites."
  - file: "Error.png"
    caption: "An error message."
---

## Minesweeper

ca. April 2024

A simple clone of the classic game made using [nwge].

### Gallery

---
template: "gallery"
base: "GameDev/Minesweeper"
images:
  - file: "Win.jpg"
    caption: "A victory."
  - file: "Loss.jpg"
    caption: "A loss."
---

## "Roulette"

ca. April 2024

A simple Russian Roulette game made using [nwge]. The primary premise of the
game was talking with your opponent, Ata. The game delved into very dark topics,
and took a very deep look into Ata's past and well as their pessimistic view
of the world. Alike many other nwge games, this was never finished.

### Gallery

---
template: "gallery"
base: "GameDev/Roulette"
images:
  - file: "MissingTexture.jpg"
    caption: "A placeholder texture."
  - file: "Early.jpg"
    caption: "Early in-game screenshot."
---

## "Runes"

ca. February - March 2024

A simple game made using [nwge]. The primary purpose of this game is to train
hand-eye coordination with a graphics tablet by completing simple minigames with
little runes. The game intended to feature Manitch as a main character, who
would offer help for the player as well as sometimes telling stories about
himself and the world he lives in.

One of the tracks originally composed for this game was eventually used in
[Shitting Bricks Simulator 2024].

### Gallery

---
template: "gallery"
base: "GameDev/Runes"
images:
  - file: "Runes.jpg"
    caption: "Some runes lined up."
  - file: "Combo.jpg"
    caption: "A combo."
  - file: "Settings.jpg"
    caption: "The settings menu."
  - file: "Debug.jpg"
    caption: "The debug menu."
  - video: "Debug.mp4"
    caption: "(Video) The debug menu."
  - file: "Speech.jpg"
    caption: "Manitch speaking to the player."
  - file: "Bug.jpg"
    caption: "Buggy text rendering."
  - video: "Intro.mp4"
    caption: "(Video) The intro sequence."
  - video: "Timescale.mp4"
    caption: "(Video) Messing with the timescale."
  - video: "Memory.mp4"
    caption: "(Video) A memory corruption glitch."
---

## TLX Engine

ca. November 2023 - February 2024

One of the very first [nwge]-based games. This was a very ambitious visual novel
project.

The main pattern invented here was a 3-layer structure. From highest to lowest
level:

* The game, contained entirely in a bundle file. Consisting of assets and
  scripts.
* The TLX Engine, written in C++ using nwge. This would handle all the
  rendering, processing etc. This would also contain a game menu that'd allow
  the user to select a game to play.
* The nwge engine, that handles all the lowest level abstractions.

That means that a TLX Engine game is just a bundle file that must be used with
the TLX Engine executable to play.

TLX Engine games were created using TLX Studio, which contained multiple editors
for various aspects of the game, such as a sprite sheet editor or a pose editor.

The primary game that the TLX Engine was designed for, and named after, was
"The Torlaxse Tower". The game would follow the story of Imme and Milian, two
anthropomorphic cats, who would try to break into the Torlaxse Tower to try and
discover the secrets of Pharosium. As with many other big projects like this, it
never got finished.

---
template: "gallery"
base: "GameDev/TLX"
images:
  - file: "DesignDoc1.jpg"
    caption: "The title of the design document of The Torlaxse Tower."
  - file: "DesignDoc2.jpg"
    caption: "Design document excerpt describing a scientist character."
  - file: "DesignDoc3.jpg"
    caption: "Design document excerpt describing a scene in the game."
  - file: "DesignDoc4.jpg"
    caption: "Design document excerpt describing the TLX Engine CLI."
  - file: "DesignDoc5.jpg"
    caption: "Design document excerpt featuring bad words!!!"
  - file: "Imme.jpg"
    caption: "An early sketch of Imme."
  - file: "Milian.jpg"
    caption: "An early sketch of Milian."
  - file: "GameMenu.jpg"
    caption: "TLX Engine game selection menu."
  - file: "GameInfo.jpg"
    caption: "Game information screen."
  - file: "MainMenu.jpg"
    caption: "Early main menu for The Torlaxse Tower."
  - file: "Studio_Toolbar.jpg"
    caption: "TLX Studio toolbar."
  - file: "Studio_Project.jpg"
    caption: "TLX Studio project management functionality."
  - file: "Studio_Sprites.jpg"
    caption: "TLX Studio sprite sheet editor."
  - video: "Studio_Help.mp4"
    caption: "(Video) TLX Studio help system."
  - video: "Studio_Sprites.mp4"
    caption: "(Video) Working with sprite sheets in TLX Studio."
---

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
  - file: "Bake1.png"
    caption: "Broken implementation of the map system."
  - file: "Bake2.jpg"
    caption: "How map blocks are turned into meshes."
  - file: "Bake3.jpg"
    caption: "How map block meshes are connected."
  - file: "Bake4.png"
    caption: "A re-evaluation of the block mesh baking process."
  - file: "Bake5.png"
    caption: "The first correctly loaded map."
  - file: "Map.png"
    caption: "Last ever taken screenshot of the game."
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

ca. June 2021

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

## Five Nights at 2Fort

ca. January 2021 (Clickteam Fusion version), March 2021 (Haxe Flixel version)

This is a [FNAF] fan-game made in [Clickteam Fusion] and later re-implemented in
[Haxe Flixel]. It was a very simple clone of the original game, replacing Freddy
Fazbear's Pizzeria with 2Fort and the animatronics with the Scout, Sniper,
Engineer and Spy from [Team Fortress 2].

The game was initially made in Clickteam Fusion, like the original game. I ended
up trying to re-implement it in Haxe Flixel as a way to test-drive it.

### Gallery

---
template: "gallery"
base: "GameDev/FNA2F"
images:
  - file: "CF_Menu.png"
    caption: "Early main menu with Clickteam Fusion's debugger visible."
  - file: "CF_Office.png"
    caption: "Early version of the office (Clickteam ver.)"
  - video: "CF_TurnAround.mp4"
    caption: "(Video) Turn around animation (Clickteam ver.)"
  - file: "CF_NightInfo.png"
    caption: "Night UI (Clickteam ver.)"
  - file: "CF_Camera.png"
    caption: "The camera UI (Clickteam ver.)"
  - file: "CF_Map.png"
    caption: "The map (Clickteam ver.)"
  - file: "Haxe_Menu.jpg"
    caption: "Early main menu (Haxe ver.)"
  - file: "Haxe_NightInfo.png"
    caption: "Night UI (Haxe ver.)"
  - file: "Haxe_Debug.png"
    caption: "AI Debug UI (Haxe ver.)"
  - file: "Haxe_Office.jpg"
    caption: "The office (Haxe ver.)"
  - file: "BTS1.png"
    caption: "SFM screenshot of one of the camera angles."
  - file: "BTS2.png"
    caption: "SFM screenshot of the office turn animation."
  - file: "BTS3.png"
    caption: "SFM screenshot of 3 Spies behind the player."
  - file: "TeaserOutside.png"
    caption: "A teaser image."
---

## Awdawd

ca. November 2019

This is one of the first games I ever made. It was made in [Clickteam Fusion]
and is a simple top-down shooter.

The game went through a few versions, ultimately stagnating on v0.5. This is the
first game I would compose a soundtrack for, even if it wasn't very good.

### Gallery

---
template: "gallery"
base: "GameDev/Awdawd"
images:
  - file: "Menu.png"
    caption: "The main menu."
  - file: "Tutorial.png"
    caption: "A tutorial."
  - file: "Loading.png"
    caption: "The loading screen."
  - file: "HUD.png"
    caption: "The in-game HUD."
  - file: "Death.png"
    caption: "The death screen."
  - video: "Gameplay1.mp4"
    caption: "(Video) Gameplay."
  - video: "Gameplay2.mp4"
    caption: "(Video) Gameplay."
---

[nwge]: /projects/nwge
[WASM-4]: https://wasm4.org/
[LIDAR Garry's Mod addon]:
    https://steamcommunity.com/sharedfiles/filedetails/?id=2813176307
[Godot]: https://godotengine.org/
[FNAF]: https://en.wikipedia.org/wiki/Five_Nights_at_Freddy%27s
[Clickteam Fusion]: https://www.clickteam.com/clickteam-fusion-2-5
[Haxe Flixel]: https://haxeflixel.com/
[2Fort]: https://en.wikipedia.org/wiki/Team_Fortress_2
[Team Fortress 2]: https://en.wikipedia.org/wiki/Team_Fortress_2
[Shitting Bricks Simulator 2024]: /projects/sbs2024
