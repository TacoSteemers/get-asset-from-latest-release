from urllib.request import urlretrieve
import tempfile
import argparse

parser = argparse.ArgumentParser("get-latest-released-asset-url-from-github");
parser.add_argument("githubRepoUrl", help="The URL to a repository on GitHub. Example: https://github.com/plantuml/plantuml");
parser.add_argument("assetName", help="An asset file name as listed on a release page in the repository. Example: plantuml.jar as listed on https://github.com/plantuml/plantuml/releases/tag/v1.2024.6");
args = parser.parse_args();

github_repo_url = args.githubRepoUrl;
asset_name = args.assetName;


github_url = "https://github.com";
github_url_length = len(github_url);
tags_post_fix = "/tags";
tag_in_fix = "/releases/tag/";
asset_in_fix = "/releases/download/";
href_open = 'href="';
href_close = '"';

short_repo_url = github_repo_url[github_url_length : github_url_length + len(github_repo_url)]
tmp_file = tempfile.NamedTemporaryFile();
urlretrieve(github_repo_url + tags_post_fix, tmp_file.name);

tag_url =  '';
target_url = '';
with open(tmp_file.name, 'r') as reader:
    line = reader.readline()
    while line != '':
        if (('href="' + short_repo_url + tag_in_fix) in line) and (not "snapshot" in line):
            tmp = line[line.find(href_open) + len(href_open) : len(line)];
            tag_url = github_url + tmp[0 : tmp.find(href_close)];
            break;
        line = reader.readline();

# From 
# https://github.com/plantuml/plantuml/releases/tag/v1.2024.6
# To
# https://github.com/plantuml/plantuml/releases/download/v1.2024.6/plantuml.jar
target_url = tag_url.replace(tag_in_fix, asset_in_fix) + "/" + asset_name;
print(target_url);
