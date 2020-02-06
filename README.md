This script takes two arguments from the user output:

1. The absoute path to a directory where all your unsorted files are located.
2. The absoulte path to a directory where you would like to put all of your sorted files.

The script requires a package called Mutagen, and depending on your system, may require some additional ones.
To install these packages run `pip install -r requirements.txt`

Keep in mind that files will be moved without copying. All folders and non-audio files are ignored.
