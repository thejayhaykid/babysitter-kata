# Babysitter
This kata simulates a babysitter working and getting paid for one night. The rules are pretty straight forward.

A babysitter simulator as described from [this repository](https://github.com/PillarTechnology/kata-babysitter) using test driven development.

---

This repository uses Python 3.6 and [pytest](https://pytest.org) as the testing framework.

## Usage Instructions

This project was tested on Linux and macOS only (***NOTE: On my MacBook, I had to use `$ python3` and `$ pip3` to get the correct versions as Python 2 is preinstalled***), the process for virtualenv is a little different for Windows.

Open a terminal window and navigate to the root folder of this project

```bash
$ cd /path/to/root/babysitter-kata
```

Virtualenv is required with Python 3.6, if you do not have virtualenv installed, run this command:

```bash
$ pip install -U virtualenv
```

*Note: if you have Python 2 and Python 3 installed, you may need to use `pip3` instead or enter the command like `$ python3.6 -m pip install -U virtualenv`*

With virtualenv installed, create a virtualenv while remaining in the root folder:

```bash
$ virtualenv venv
```

Activate virtualenv:

```bash
$ source /venv/bin/activate
```

Then install needed packages:

```bash
(venv) $ pip install -r requirements.txt
(venv) $ pip install -e .
```
*The second command installs the local package, allowing use with the `babysitter` CLI while in the virtualenv.*

After that you should be able to run the main.py file `(venv) $ babysitter` or run tests `(venv) $ pytest`. 

With the babysitter CLI, you can use the following flags:

- `--help` -- Will pull up a well formatted listing of all of the flags
- `-s TEXT` or `--start TEXT` -- to enter the start time. Example: `(venv) $ babysitter -s 1800`
- `-e TEXT` or `--end TEXT` -- to enter the end time. Example: `(venv) $ babysitter -e 1800`
- `-f [A|B|C]` or `--family [A|B|C]` -- to select the family. Example `(venv) $ babysitter -f B`

Any of the three flags not accounted for will receive a prompt to enter the value.

When done, exit the virtualenv with:

```bash
(venv) $ deactivate
```

---

## Notes

This is going to stay very strict to the provided requirements to make a minimum viable product so that it can be shipped. Because of that there have been some architectural decisions that have been made in the planning portion, such as:

1. The three families will be hardcoded into the program. It would be preferable to have them defined in an input file or even a database so that they could be more easily edited. But since they do not need to be editable and there are only three, it saves time to define them directly in the program.
2. The work hours will also be hardcoded for the same reasons.
3. The CLI will be used to just define one babysitting event.
4. Because of the requirement "gets paid for full hours (no fractional hours)", I made the decision to use a standard rounding pattern. Minute 00 to minute 29 are rounded down and minute 30 to minute 59 are rounded up and hour.
5. Decided to take time input as a 4 digit 24 hour input. Midnight is 0000, 5 PM is 1700.

The initial commit for this project is a project skeleton only, with the minimum requirements for an organized python project.

I ran a [testing coverage](https://pypi.org/project/pytest-cov/) tool after class was completed and here are the results:

```bash
=========================== test session starts ===========================
platform linux -- Python 3.6.8, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
rootdir: /home/jake/python/babysitter-kata
plugins: cov-2.7.1
collected 15 items

test/babysitter_test.py ..........                                  [ 66%]
test/variable_rate_test.py .....                                    [100%]

----------- coverage: platform linux, python 3.6.8-final-0 -----------
Name                       Stmts   Miss  Cover
----------------------------------------------
babysitter/__init__.py         1      0   100%
babysitter/babysitter.py      54      0   100%
----------------------------------------------
TOTAL                         55      0   100%


======================== 15 passed in 0.07 seconds ========================
```
