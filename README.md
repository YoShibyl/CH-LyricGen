# Clone Hero lyrics generator / auto-filler

This is a simple Python 3 script that inserts syllables of lyrics for a song into a `.chart` file for use with the rhythm game [Clone Hero](https://clonehero.net/).  Its main purpose is to aid in the creation of said charts to make it less tedious to insert lyrics.

It reads the syllables from lines in a plaintext file (`lyrics.txt` by default) and replaces empty lyric events in the chart file (`notes.chart` by default), then saving the result to `output.chart` by default.

## Usage

`python lyricgen.py <input.chart> <lyrics.txt> [output.chart]`

* If the input `.chart` and/or `lyrics.txt` file are not provided, then the script will prompt you for filepaths.  Dragging and dropping the files into the prompts should work.

### lyrics.txt format

Lyrics should be written manually in a plaintext file, as syllables separated by line breaks, with multi-syllable words ending with a hyphen.  If a word needs to have a hyphen in it (such as `all-star`), end the appropriate syllable with an equals sign and a hyphen (example: `all=-` and then `star`)
```
Some-
bo-
dy
once
told
me
the
world
is
gon-
na
roll
me
```

## Disclaimer

I'm not responsible for any damage or data loss caused by misuse of this script.  Always make a backup of the chart you're working with.

Also, I didn't make Clone Hero.  This script is merely a tool for filling in blanks in files.