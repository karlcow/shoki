# shoki (書記)

shoki is a secretary in Japanese. This python program is here to help take a text only file of meeting minutes and convert it into structured data. This structured data can then be converted into other formats.

It was initially defined for addressing the needs of Mozilla webcompat team.

## Features

The required features are:

* Parses meeting date and time
* Parses agenda items and agenda owners
* Parses agenda item description
* Parses action items
* Starts parsing after a dedicated string
* Stops parsing after a dedicated string
* Handles the output in different formats (can be extended)
* Includes Mediawiki markup output format
