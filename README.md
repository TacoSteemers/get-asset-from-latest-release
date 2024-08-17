Get the latest asset from a release in a GitHub repository
==========================================================

A small tool to get an updated asset from the latest release in a given GitHub repository, other than any release with `snapshot` in the name.

The tool uses bash, curl and python3. There was no real design there; it is just what I ended up with.

It can be called as follows:

    ./get-asset-from-latest-github-release -r https://github.com/plantuml/plantuml -o ~/bin/plantuml.jar -a plantuml.jar;

Here we search in a repository (mentioned in argument -r) for the latest release for that repository, and then download an asset (mentioned in argument -a) to a local file path (mentioned in argument -o).

Note that we skip releases that contain the word 'snapshot'.






