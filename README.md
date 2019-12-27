# endpointdiff
endpointdiff is a simple wrapper script around LinkFinder (https://github.com/GerbenJavado/LinkFinder) to quickly identify whether endpoints have changed based on diffs of JS files.

## Installation
endpointdiff supports Python3. It depends on LinkFinder, so it will also need the dependencies LinkFinder has.

```
# After cloning this repository, clone `LinkFinder` within:
git clone https://github.com/GerbenJavado/LinkFinder.git

# Install the dependencies
pip3 install -r requirements.txt
```

The structure should look like:

```
├── endpointdiff
│   ├── LinkFinder/
```

## Usage

Short Form    | Long Form     | Description
------------- | ------------- |-------------
-n            | --new         | Input a new: URL, file or folder. For folders a wildcard can be used (e.g. '/*.js').
-o            | --old         | Input an old: URL, file or folder. For folders a wildcard can be used (e.g. '/*.js').
-r            | --regex       | RegEx for filtering purposes against found endpoints (e.g. ^/api/)
-s            | --save        | File location to save the diff output to.
-c            | --cookies     | Add cookies to the request
-h            | --help        | show the help message and exit

Most if not all of the `LinkFinder` functionality should be able to be leveraged. Some examples on usage are:

If you want to determine the diff in endpoints for 2 JS URLs:

`python3 endpointdiff.py -o https://site.com/oldjs -n https://site.com/newjs`

If you want to determine the diff in endpoints for a saved local version, and then save the output:

`python3 endpointdiff.py -o old/js/file.js -n https://site.com/newjs -s path/to/save.txt`

If you want to analyze entire folders against each other:

`python3 endpointdiff.py -o old/*.js -n new/*.js`