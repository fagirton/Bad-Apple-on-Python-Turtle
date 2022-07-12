# Bad Apple on Python Turtle (Unfinished)
Probably the worst possible way to watch Bad Apple

Here's preview:
![Preview](preview-v0.5.gif)

This program draws every single frame of Bad Apple video inside Python Turtle Graphics,
 but since Turtle is incredibly slow, you'll see the end of it only after 4 hours. 
This project was made in one day, so I haven't figured out how to optimise drawing and get rid of weird lines across picture (let me know if you know how).

## Basic explanation of how it works
1. FFMPEG converts video to PNG images with threshold filter from [here](https://video.stackexchange.com/questions/28758/ffmpeg-convert-video-to-black-white-with-threshold/28759#28759)
2. OpenCV opens frame and tells color of each pixel in every row
3. Turtle moves through each of 360 lines (height of the video itself) and places pen down each time OpenCV says there's black
4. Process repeats from step 2 when Turtle ends drawing frame and clears screen

## For this project I used
FFMPEG for converting video to monochrome images
OpenCV-Python works with images
Turtle Graphics draws Bad Apple clip with worst speed ever possible
