# My-Search-Engine

A simple search engine


This search Engine takes in a string query and returns data related to that string query.


we will be using the wikipedia data set as a source of data.

Each document comes in the following format:

```<doc>
    <title>Wikipedia: London Beer Flood</title>
    <url>https://en.wikipedia.org/wiki/London_Beer_Flood</url>
    <abstract>The London Beer Flood was an accident at Meux & Co's Horse Shoe Brewery, London, on 17 October 1814. It took place when one of the  wooden vats of fermenting porter burst.</abstract>
    ...
</doc>

```
The bits were interested in are the title, the url and the abstract text itself. 

### Step1: Download data to your localhost

simple click `https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-abstract.xml.gz` 

store the file in your root folder in folder called data.

### Step2: Add data to the database

run `python3 load.py & `

This command runs in the background and will put out logs in `loaddata.log`

### Step3: Query

run `python3 run.py 'London Beer Flood'`


