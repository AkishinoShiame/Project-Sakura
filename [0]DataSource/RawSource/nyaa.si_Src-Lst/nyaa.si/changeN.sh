#/bin/bash

for i in $(seq 1 14); do
  mv "index.html?f=0&c=1_4&q=\"(MX+1280x720+x264+AAC)\"+-mp4&s=downloads&o=desc&p=$i" "index-$i.html"
done
