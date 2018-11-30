# shoki (書記)

![Shoki](http://www.la-grange.net/2017/06/22/shoki-scribe-small.png)

shoki is a secretary in Japanese. This python program is here to help take a text-only file of meeting minutes and convert it into structured data. This structured data can then be converted into other formats.


## Install

```bash
pip install shoki
```

## Usage

```bash
shoki create --location [uri]
```

where `uri` is the location of the content served with a `Content-Type: text/markdown` or `Content-Type: text/plain` encoded as utf-8.


### Example

```bash
shoki create --location https://webcompat-meet.herokuapp.com/0CMnUyYMSBaQJQ97Yxc8Ww/download
```

## History

It was initially defined for addressing the needs of [Mozilla webcompat team](https://wiki.mozilla.org/Compatibility). It's strongly inspired by W3C meetings style. We are [taking minute](https://webcompat-meet.herokuapp.com/0CMnUyYMSBaQJQ97Yxc8Ww) of our meetings on CodiMD. Once the meeting has been done. We generate the minutes with a mediawiki format that we add to the [list of our meetings](https://wiki.mozilla.org/Compatibility/Meetings).

Example: [Web Compatibility team minutes - September 11, 2018](https://wiki.mozilla.org/Compatibility/Meetings/2018-09-11) ([raw source](https://wiki.mozilla.org/index.php?title=Compatibility/Meetings/2018-09-11&action=edit))

## Contributing

If you wish to contribute to this project, read the [contributing guidelines](https://github.com/karlcow/shoki/blob/master/CONTRIBUTING.md).

## Features - ToDo

The required features are:

* [x] Parses meeting date and time
* [x] Parses agenda items and agenda owners
* [x] Parses agenda item description
* [x] Parses action items
* [x] Starts parsing after a dedicated string
* [x] Stops parsing after a dedicated string
* [ ] Handles the output in different formats (can be extended)
* [x] Includes Mediawiki markup output format
* [x] Handles an URI for the text minutes input
* [x] Handles a file for the text minutes input

Some constraints:

* [x] Avoid using regex
* [x] Tests Driven
