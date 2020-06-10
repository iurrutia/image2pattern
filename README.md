# README 

### image2stitch
A mini-project to make images into knitting pattern colour charts using k-means. [https://image2stitch.space](https://image2stitch.space)


![](other/demo_vid2.gif)


## The back-story
Some time in 2012 or 2013, my then-roommate went to Blizzcon. I was just learning to knit, and I was also very much into learning how to four-gate (I wasn't very skilled at Starcraft). Long story short, I created a zerg colour chart, and knitted a sweater for Manfred, Starcraft caster Day9's stuffed bunny toy. The pattern I made is here: [link](https://www.ravelry.com/patterns/library/zerg-starcraft-colour-chart) My roommate gave the sweater to Day9 at Blizzcon:

![](other/manfred.jpg)

But what if you are not a zerg player, like Manfred the bunny?
![](other/example.jpg)

We can output a knitting chart for that looks like this:

![](other/output.jpg)

## What does the app do?

Knit stitches are wider than they are taller (1.25 wide = 1 tall). Images are resized to the correct ratio, then pixelated. The colour space is reduced by performing k-means clustering on the rgb or hsv colourspace for the image. The user is shown a preview of the image with the reduced colourset, and given the option to download a file (dataframe) with the colour labels k-means (relabelled from zero to n, the number of colours.)


## How to use

### Online version 
(Can only handle so many requests...)

[Live App: https://image2stitch.space](https://image2stitch.space)

### To clone and run:

Requires python3 and pip.

```pip install -r requirements.txt```

```streamlit run front_end.py```

