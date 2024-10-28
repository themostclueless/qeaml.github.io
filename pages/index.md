---
title: Home
desc: qeaml's personal website
---

<p id="first-p">
Hello! My name is <strong>qeaml</strong> (pronounced key-mill). I'm AGE years
old and live in the beautiful country of Poland.
</p>

<script>
let now = new Date();
let age = now.getFullYear() - 2006;
// if after march 8th
if(now.getMonth() > 2 || (now.getMonth() == 2 && now.getDate() > 8)) {
    age++;
}
let paragraph = document.getElementById("first-p");
paragraph.innerHTML = paragraph.innerHTML.replace("AGE", age);

if(now.getMonth() == 2 && now.getDay() == 8) {
    paragraph.innerHTML += " It's my birthday today! 🎉";
}

// halloween
if(now.getMonth() == 9 && now.getDate() == 31) {
    paragraph.innerHTML += " Have a spooky Halloween! 🎃";
}

// polish day of independence
if(now.getMonth() == 10 && now.getDate() == 11) {
    paragraph.innerHTML += " Happy Polish Independence Day! 🇵🇱";
}
</script>

## Links

* [BlueSky]
* [GitHub]
* [Discord] (nwge game studios server)
* [itch.io]
* [Bandcamp]
* [Spotify]
* [YouTube]
* [PronounsPage]
* [GameBanana]

If you wish to get in contact, the best way is through **BlueSky**. Keep in mind
that I have next to no filter whenever posting, so be prepared to see some odd
thoughts when scrolling through my profile(s).

## Other Stuff

* [Windows Registry Tweaks](/WindowsRegistry)
* [List of Lithuanians](/LT)

[Projects]: /projects
[GitHub]: https://github.com/qeaml
[itch.io]: https://qeaml.itch.io
[Discord]: https://discord.gg/y7GxumVE3G
[BlueSky]: https://bsky.app/profile/qeaml.bsky.social
[Bandcamp]: https://qeaml.bandcamp.com
[Spotify]:
    https://open.spotify.com/artist/0dWlVjsXUfWpdTjqrgV8BV?si=Dl8NuvVhRWeOTu9cJ3fmQQ
[YouTube]: https://youtube.com/@qeaml
[PronounsPage]: https://en.pronouns.page/@qeaml
[LinkTree]: https://linktr.ee/qeaml
[GameBanana]: https://gamebanana.com/members/1479808
