import os
import string
import sys

# CHLyricsGen is a Python 3 script that fills in blank "lyric " events in .chart files for Clone Hero.

# ARGUMENTS:
# python lyricgen.py <input.chart> <lyrics.txt> [output.chart]

print(" ")
if len(sys.argv) < 3:
    inpChart = input("Filename/path of input chart? (*.chart)\n> ").replace("\"","")
    inpLyric = input("Filename/path of lyric syllables, separated by new lines?\n(*.txt) See README for how to format lyrics.\n> ").replace("\"","")
    outChart = input("Enter a new filename for the output chart.\n Leave blank to write to `./output.chart`\n> ").replace("\"","")
    if inpChart == "": inpChart = "./notes.chart"
    if inpLyric == "": inpLyric = "./lyrics.txt"
    if outChart == "": outChart = "./output.chart"
elif len(sys.argv) >= 3:
    inpChart = sys.argv[1].replace("\"","")
    inpLyric = sys.argv[2].replace("\"","")
    if len(sys.argv) < 4: outChart = inpChart

chartFile_in = open(inpChart,'r')
lyricFile = open(inpLyric,'r')
lyrics = lyricFile.read().splitlines()
chart = str(chartFile_in.read())

print("\nFilling in %d lyric syllables..." % len(lyrics))
for syllable in lyrics:
  
    print("Syllable `%s`" % syllable)
    chart = chart.replace('E \"lyric \"', 'E \"lyric %s\"' % syllable, 1)

chartFile_out = open(outChart,'w+')
chartFile_out.write(chart)

lyricFile.close()
chartFile_in.close()
chartFile_out.close()

print("Exported chart with lyrics to %s" % outChart)