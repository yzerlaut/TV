single_dl() {
    python -m yt_dlp  -f "bv*+mergeall[vcodec=none]" --audio-multistreams -S "height:360" $1
}
list_dl() {
    python -m yt_dlp  -f "bv*+mergeall[vcodec=none]" --audio-multistreams -S "height:360" -a list.txt
}
