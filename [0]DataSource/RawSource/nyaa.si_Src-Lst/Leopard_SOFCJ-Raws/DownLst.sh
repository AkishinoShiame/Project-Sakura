#/bin/bash

for i in $(seq 1 1); do
  DLlink="https://nyaa.si/?f=0&c=1_4&q=%22Leopard_SOFCJ-Raws%22+%221280x720+x264+AAC%29%22+-mp4+-mkv&s=downloads&o=desc&p=$i"
  echo "Downloading for page $i..."
  echo "Src Link = $DLlink =>>>"
  wget -p -k $DLlink
  sleep 10
done
