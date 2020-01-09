# Hand-Posture-Recognition-OpenCV
Hand posture recognition using skin detection and structural analysis in OpenCV

I wanted to use the knowledge I've aquired in the book I'm currently reading "OpenCV 4 with Python". Taking the skin tones mask and the advanced contours and mixing them.
I would also (someday) compare the shape of the hand to a saved dictionary of shapes so you can get the exact position of hand and fingers. I can imagine it using it to write in sign language. Cool.

The program steps are pretty straight forward:
- Get the frame from the webcam.
- Mask the skin color range. I've used a small window so doesn't take any undesirable colors from the background. Since is not AI...
- Make the mask better with the OpenCV morphological transformations.
- Ready to implement the structural analysis.
- Draw the figure.
- **Pic related:**

![](output.gif)


