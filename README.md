# My-Search-Engine

A simple search engine

This application is a mix of [this](https://bart.degoe.de/building-a-full-text-search-engine-150-lines-of-code/) and [this]( https://towardsdatascience.com/create-a-simple-search-engine-using-python-412587619ff5) tutorial.

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

Step1: We are going to stream through the gzipped XML without loading the entire file into memory first
Step2: 
