
# geoip-geosite-list

# Table of Contents

1. [Introduction](#Introduction)
2. [Installation](#Installation)
3. [Usage](#Usage)

## Introduction

A Python script that generates a txt or json file to specify which domain is supported by a geosite. 

The data is sourced from the repository [v2fly/domain-list-community](https://github.com/v2fly/domain-list-community/)

(GitHub does not display all the contents of the data folder in the repository, but here everything is conveniently in one file, making it easier to search through the file to quickly find the information).

I will also update the existing data in this repository if new domains are added.
(The .txt file contains only the supported domains, while the .json file provides details on which specific domains are hidden behind the name).

[Domains.json](https://github.com/actusnileh/geoip-geosite-list/blob/main/domains.json)

[Domains.txt](https://github.com/actusnileh/geoip-geosite-list/blob/main/domains.txt)

## Installation

1. Clone the repository:
```
git clone https://github.com/actusnileh/geoip-geosite-list.git
```
2. Navigate to the project directory:
```
cd geoip-geosite-list
```
3. Install the required dependencies
```
poetry install
```

## Usage

You can generate the .txt or .json file using the command-line interface provided by the tool.

# Generating a .txt File:
```
python cli.py --generate txt
```
# Generating a .json File:
```
python cli.py --generate json
```
# Checking the Version:
```
python cli.py --version
```
