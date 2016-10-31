# Data Scraper using BS4 and Mechanize


I wrote this script to automate renaming of files, using a lookup table.

### How it works:
- So I basically get a list of the files in the current directory
- I Iterate through the files
- While Iterating through the files, I iterate throught he lookup table
- If the current file, matches the row LookUp-ID (unique identifier), then file rename takes place.


### Instructions:

- Make sure the LookUp table consists of files that need to be renamed `FROM`, and `TO`
- Place your input files that need to be renamed, in a directory
- Depending on the file extension, you change change this. You could improve this script by handling the file-extension.
- I have used windows `\` for `long_path`, you might want to change to a forward `/` if you are using this on a *nix based system.

### How to Run:

```sh
$ cd renamer
$ python renamer.py
```

