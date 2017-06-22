# shoki (書記)

![Shoki](http://www.la-grange.net/2017/06/22/shoki-scribe-small.png)

shoki is a secretary in Japanese. This python program is here to help take a text only file of meeting minutes and convert it into structured data. This structured data can then be converted into other formats.

It was initially defined for addressing the needs of Mozilla webcompat team.

## Features

The required features are:

* [x] Parses meeting date and time
* [x] Parses agenda items and agenda owners
* [x] Parses agenda item description
* [x] Parses action items
* [x] Starts parsing after a dedicated string
* [x] Stops parsing after a dedicated string
* [ ] Handles the output in different formats (can be extended)
* [ ] Includes Mediawiki markup output format
* [ ] Handles an URI for the text minutes input
* [ ] Handles a file for the text minutes input

Some constraints:

* [x] Avoid using regex
* [x] Tests Driven
