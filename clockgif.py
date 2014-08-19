#!/usr/bin/python

from subprocess import call

frame_filenames = []
for x in range(0, 15):
    frame_filename = "countdown-%d.gif" % x
    if x < 10:
        color = "SpringGreen"
    elif x < 13:
        color = "yellow"
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
          frame_filename])
    frame_filenames.append(frame_filename)

args = ["convert",
        "-delay", "100",
        "-loop", "1"]
for x in range(0, 20):
    args += frame_filenames
args.append("clock.gif")
call(args)
