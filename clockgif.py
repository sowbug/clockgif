#!/usr/bin/python

from subprocess import call

SECONDS = 15
SLIDES = 20

frame_filenames = []
for x in range(0, SECONDS):
    frame_filename = "countdown-%d.gif" % x
    if x < SECONDS - 5:
        color = "green1"
    elif x < SECONDS - 2:
        color = "yellow"
    elif x < SECONDS - 1:
        color = "orange"
    else:
        color = "red"
    call(["convert",
          "-background", "black",
          "-bordercolor", "black",
          "-fill", color,
          "-font", "EHSMB.TTF",
          "-pointsize", "24",
          "-border", "8x8",
          "label:00:%02d" % (15 - x),
#          "-fill", "yellow",
#          "-draw", "rectangle 0,0 %d,4" % (93 * (x + 1) / SLIDES),
          frame_filename])
    frame_filenames.append(frame_filename)

args = ["convert",
        "-delay", "100",
        "-loop", "1"]
for x in range(0, SLIDES):
    args += frame_filenames
args.append("clock.gif")
call(args)
