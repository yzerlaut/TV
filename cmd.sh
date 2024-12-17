# Downloading Single Movie from URL
# --- argument is URL
single_dl() {
    python -m yt_dlp -o "%(title)s.%(ext)s" -f "bv*+mergeall[vcodec=none]" --audio-multistreams -S "height:360" --write-subs $1
}
# Downloading Multiples Movies from URL
# --- argument is folder destination
list_dl() {
    python -m yt_dlp  -o "%(title)s.%(ext)s" -f "bv*+mergeall[vcodec=none]" --audio-multistreams -S "height:360" --write-subs -a list.txt $1/
}
