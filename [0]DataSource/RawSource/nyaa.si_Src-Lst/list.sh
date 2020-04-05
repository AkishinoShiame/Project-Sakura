#/bin/bash

for i in $(seq 1 14); do
  DLlink="https://nyaa.si/?f=0&c=1_4&q=%22%28MX+1280x720+x264+AAC%29%22+-mp4&s=downloads&o=desc&p=$i"
  echo "Downloading for page $i..."
  echo "Src Link = $DLlink =>>>"
  wget -p -k $DLlink -O lndex-$i.html
  sleep 10
done
