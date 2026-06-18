IMAGES=$(wildcard *.png)
RESIZED=$(patsubst %.png, %.small.png, $(IMAGES))

all: $(RESIZED)

%.small.png: %.png
	convert $< -resize 400 $@
	rm $<
	mv $@ $<
