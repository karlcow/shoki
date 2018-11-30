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

## Running unittests

```bash
nosetests -v
```

This will spill out (or more)

```
Return the appropriate data structure. ... ok
Returns the appropriate data structure. ... ok
Todo lines are parsed correctly. ... ok
Extract the discussion structure from list of lines. ... ok
Test lines starting with http. ... ok
Extract the meeting date. ... ok
Return the dictionary for meeting metatada. ... ok
Extract minutes into blocks. ... ok
Extract the topic and owner of a discussion. ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.050s

OK
```

## Testing your development locally

This will install locally the code and will make you able to test your branch locally.

```bash
pip3 install -e .
```

and will spill out something like:

```
Obtaining file:///Users/karl/code/shoki
Installing collected packages: shoki
  Found existing installation: shoki 1.0.0
    Uninstalling shoki-1.0.0:
      Successfully uninstalled shoki-1.0.0
  Running setup.py develop for shoki
Successfully installed shoki
```

Then you can test with:

```bash
shoki create
```

