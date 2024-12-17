# TV

>   _a few scripts to download replays from TV replay websites_

## Install

The whole pipeline relies on [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)

Install `yt-dlp`:
```
git clone https://github.com/yt-dlp/yt-dlp
cd yt-dlp
pip install .
```
## Usage

First source the script:
```
source ./bash.sh
```

Then:

### Single Video Link

```
single_dl your_url.html
```
`single_dl` if an alias of `bash.sh`

### Multi Video Link

1) first pre-process the link to extract single videos links
```
python ./franceTV.py your_url.html
# or python ./arte.py your_url.html
```
this creates a `list.txt` file.

2) Download the list of files
```
list_dl
```

`list_dl` if an alias of `bash.sh`

