# OpenDotMatrix
Open Source Dot Matrix font generator, an alternative for [Dionaea's original font](https://dionaea.com/information/fonts.php).

## Supported Unicode blocks
- Basic Latin `0x20-0x7F` (full)
- Latin-1 Supplement `0xA0-0xFF` (12 glyphs: `£, ©, «, », Å, Æ, Ø, å, æ, ò, ó, ø`)
- Cyrillic `0x400-0x4FF` (Belarusian, Russian and Ukrainian)

## Contributions
All contributions are welcome, I'm waiting for PRs with your code pages and glyphs!

If you want to add new glyphs within supported blocks, just do so inside block files within `db` folder!

Be aware of optional `baseline-offset: (x, y)` glyph property, you can offset glyphs by `x` circles to the left and by `y` circles down!

If you want to add support for new blocks, check out these two lists: [plane one](https://www.compart.com/en/unicode/plane/U+0000), [plane two](https://www.compart.com/en/unicode/plane/U+10000)
1. Select the block you'd like to work on
2. Create a new file with suitable block name inside `db` folder
3. Import your newly created file in `db/__init__.py` and add it to the export `GLYPHS` constant
4. Add the wanted glyphs to your block file!
