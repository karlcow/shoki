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

## How To Contribute

1. Check for open issues or open a new issue. Be descriptive. Give examples.
2. Fork the repository on GitHub.
3. Make sure you always have the latest version of master before coding.
```bash
git checkout master
git fetch upstream
git merge upstream/master
```
3. Create a branch with the issue number and the version of your branch. If it's about issue 69. Then your first attempt will be in a branch name '69/1'.

```bash
git checkout -b 69/1
```
4. Try as much as possible to start with writing tests for the new feature.
5. Once your feature is done. Push the branch to your repo and create a pull request against master on shoki repo.
6. Ask @karlcow for review.

## History

It was initially defined for addressing the needs of [Mozilla webcompat team](https://wiki.mozilla.org/Compatibility). It's strongly inspired by W3C meetings style. We are [taking minute](https://webcompat-meet.herokuapp.com/0CMnUyYMSBaQJQ97Yxc8Ww) of our meetings on CodiMD. Once the meeting has been done. We generate the minutes with a mediawiki format that we add to the [list of our meetings](https://wiki.mozilla.org/Compatibility/Meetings).

Example: [Web Compatibility team minutes - September 11, 2018](https://wiki.mozilla.org/Compatibility/Meetings/2018-09-11) ([raw source](https://wiki.mozilla.org/index.php?title=Compatibility/Meetings/2018-09-11&action=edit))

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
* [ ] Handles an URI for the text minutes input
* [ ] Handles a file for the text minutes input

Some constraints:

* [x] Avoid using regex
* [x] Tests Driven
