---
name: rachel-brand-standard-jul31
description: Rachel-Lyn Cavano's Jul 31 2026 HTML brand guidelines are the new brandkit standard and conflict with the Jul 30 Roboto kit on font, green hex, and orange
metadata:
  type: project
---

Jul 31 2026, thread "Re: latest DWO deck -- re-create in HTML?" (Tom Russell kickoff Jul 30, Naveen fronted the build Jul 31 11:50am with https://dwostoryqbr.netlify.app/).

**Rachel-Lyn Cavano, Senior Graphic Designer, is the brand authority.** Her 4:05pm email is now the standard for all HTML deliverables and SUPERSEDES [[intradiem-brandkit-current-jul30]]. Melissa Spies (VP Marketing) flagged it first, "the orange looks off, the teeny tiny fonts," then brought Rachel in for detail.

**Her brand-compliance rules, verbatim scope:**
- Open Sans if Claude can use it, otherwise **Tahoma as the only font**
- No all caps anywhere. Title or sentence case only.
- Text colors ONLY: white, dark green `#014637`, "Deep Green #22875", Intradiem Green `#2CB56E`. Never gray except `#363636`.
- No text under 10pt
- No red, and no color outside the Intradiem Color Palette in her attachment
- Opening and closing slides use the new brand background she attached

**Her design-fidelity rules:** the HTML should pull in the same graphics as the slides or recreate them, never redesign.
- Slide 4: the workforces graphic became four plain boxes and lost the story. Recreate in HTML or pull the image.
- Slide 10: the See / Anticipate / Act continuous loop is better than the static slide, keep it. Fix the looping line cutting through text, either jump the word or make the text background dark green instead of transparent.
- Slide 14: some logos have white backgrounds. Make them transparent or she will send new files.

**All three conflicts RESOLVED Jul 31 from her own attachment, not by guessing:**
1. Font is Open Sans (web) with Tahoma fallback, **not Roboto**. Confirmed.
2. Intradiem Green is `#2CB56E`. Her attachment gives RGB 44, 181, 110 and 44 = `2C`, so her hex is right and the Jul 30 kit's `#2DB56E` is wrong.
3. Orange `#F58220` is legitimate; it is in her own palette as the primary CTA fill. Melissa's "the orange looks off" was about `#FE5000`, an older red-orange that is still live in the deck. Keep `#F58220`, never typeset it.

**Deep Green RESOLVED: `#228751`.** Her email's `#22875` dropped a digit; the attachment states `#228751` in both the palette and the CSS variables block. Confirm with her, but do not treat it as open.

**Two ambiguities inside her own materials, still worth her ruling:** the email permits `#2CB56E` as a text colour while the section table says accents are never a text colour, and the attachment bans reduced-opacity rgba as a text colour, which this deck leaned on heavily for secondary text. Both are resolved the stricter way in [[intradiem-brand-kit-machine-jul31]].

**Naveen handed Dallas the lane publicly** at 4:11pm: "Please reach out to @Dallas Andrews for any further help. He will be able to help you pick up all things around building these tools through AI and managing them." That closes the earlier question of whether to claim the Rachel walkthrough; it is already claimed on Dallas's behalf in front of Tom, Chris, Melissa, and Rachel. Rachel separately offered to meet to see how Claude generates these so she can write proper HTML brand guidelines. Different from [[naveen-shield-dynamic]]: the shield was about deck creative, this is tooling enablement, Dallas's public lane.

**Also live:** per Tom's kickoff, Rachel already built a "brand" skill in Claude that is drifting ("we have seen Claude vary from that"). Fixing that drift is the durable version of this work, not repainting one deck.

**Source files:** Rachel's guidelines arrived as a 1.2MB HTML where 99% is four embedded base64 images. Split, readable version at `~/Downloads/rachel-brand-guidelines/` (guidelines.html plus small-figure-*.png). Never open the original, it killed four sessions. See [[context-discipline-jul31]].
