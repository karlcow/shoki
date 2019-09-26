## How To Contribute

1. Check for open issues or open a new issue. Be descriptive. Give examples.
2. Fork the repository on GitHub.
```bash
git clone git@github.com:[username]/shoki.git
```
replace the username with your github username.
3. Install a virtual environment
```bash
cd shoki
python3 -m venv env
source env/bin/activate
pip install -r requirements-dev.txt
```
4. Make sure you always have the latest version of master before coding.
```bash
git checkout master
git fetch upstream
git merge upstream/master
```
5. Create a branch with the issue number and the version of your branch. If it's about issue 69. Then your first attempt will be in a branch name '69/1'.
```bash
git checkout -b 69/1
```
6. Try as much as possible to start with writing tests for the new feature.
7. Then run tests. See below.
8. Once your feature is done. Push the branch to your repo and create a pull request against master on shoki repo.
9.  Ask @karlcow for review.

## Running unittests

```bash
pytest -v
```

This will spill out (or more)

```
================================================================= test session starts =================================================================
platform darwin -- Python 3.7.4, pytest-5.1.3, py-1.8.0, pluggy-0.13.0 -- /Users/karl/code/shoki/env/bin/python3
cachedir: .pytest_cache
rootdir: /Users/karl/code/shoki
collected 10 items

tests/test_datacore.py::TestShokiDatacore::test_minutes_data PASSED                                                                             [ 10%]
tests/test_formatter.py::TestShokiFormatter::test_convert_unknown_format PASSED                                                                 [ 20%]
tests/test_parsing.py::TestShokiParsing::test_extract_todo PASSED                                                                               [ 30%]
tests/test_parsing.py::TestShokiParsing::test_from_blocks_to_structure PASSED                                                                   [ 40%]
tests/test_parsing.py::TestShokiParsing::test_is_link PASSED                                                                                    [ 50%]
tests/test_parsing.py::TestShokiParsing::test_meeting_date PASSED                                                                               [ 60%]
tests/test_parsing.py::TestShokiParsing::test_meta_headers PASSED                                                                               [ 70%]
tests/test_parsing.py::TestShokiParsing::test_meta_yaml PASSED                                                                                  [ 80%]
tests/test_parsing.py::TestShokiParsing::test_minutes_blocks PASSED                                                                             [ 90%]
tests/test_parsing.py::TestShokiParsing::test_topic_owner PASSED                                                                                [100%]

================================================================= 10 passed in 0.11s ==================================================================
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
