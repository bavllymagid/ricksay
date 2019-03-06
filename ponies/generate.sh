#!/bin/bash
# This script generates ponyfiles from downloaded images

function export_images {
  # params: character magic_magnify_factor
  for if in png/$1/*.png; do
    fname=$(basename $if)
    of=$1/${fname%.*}.pony
    if [ ! -f "$of" ]; then
      echo "Processing $if"
      java -jar util-say.jar --import image --magnified $2 --file $if \
        --export ponysay --file "$of"
    fi
  done
}

# Morties
export_images Morty 8

# Ricks
export_images Rick 12
