#/bin/bash

for i in $(seq 1 12); do
  DLlink="https://nyaa.si/?f=0&c=1_4&q=%22Raws%5D%22+%22%28MX+1280x720+x264+AAC%29%22+-mp4&s=downloads&o=desc&p=$i"
  echo "Downloading for page $i..."
  echo "Src Link = $DLlink =>>>"
  wget -p -k $DLlink
  sleep 10
done
