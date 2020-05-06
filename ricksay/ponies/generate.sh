#!/bin/zsh
# This script generates ponyfiles from downloaded images
# Prerequisites: Java, Zsh

function export_images {
  # params: character magic_magnify_factor
  for if in sprites/$1/*.png; do
    fname=$(basename $if)
    of=$1/${fname%.*}.pony
    if [ ! -f "$of" ]; then
      print "Processing $if"
      java -jar util-say.jar --import image --magnified $2 --file $if \
        --export ponysay --file "$of"
    fi
  done
}

print "Started Schwifting!"
for char in Rick Morty Beth Jerry Summer; do
    print "Time of $char"
    mkdir -p $char
    export_images $char 3
done
print "Wubba Lubba Dub Dub, Done!"
