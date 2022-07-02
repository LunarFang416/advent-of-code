## Advent of Code - AOC

These are my [AOC](https://adventofcode.com/) solutions.

### AOC Helper CLI 
The aoc cli can help automate tasks when you are solving AOC problems.
To use the cli, create a .env file and configure it with your specifc AOC Cookies which you can acquire using Chrome/Firefox
developer tools. Your .env file should look like this.
```
COOKIES=[YOUR COOKIES HERE]
```

```console
usage: aoc [-h] {download,submit,setup} ...

positional arguments:
  {download,submit,setup}
    download            Download AOC Input
    submit              Submit AOC Answer
    setup               Setup Boilerplate python file for AOC

optional arguments:
  -h, --help            show this help message and exit
```

#### File Setup
Setup boilerplate for your solution file in python with pytest parametrize configured to test your code against
sample test cases provided on the AOC challenge page.

```console
usage: aoc setup [-h] -y YEAR -d DAY -p {1,2}

optional arguments:
  -h, --help            show this help message and exit
  -y YEAR, --year YEAR  AOC input download year (2015-2021).
  -d DAY, --day DAY     AOC challenge day (1:25).
  -p {1,2}, --part {1,2}
                        Part of the AOC challenge you want to setup boilerplate for
```

#### Input Download
Download challenge input for any AOC challenge which will be written in the AOC challenge year folder.

```console
usage: aoc download [-h] -y YEAR -d DAY

optional arguments:
  -h, --help            show this help message and exit
  -y YEAR, --year YEAR  AOC input download year (2015-2021).
  -d DAY, --day DAY     AOC challenge day (1:25).
```

#### Solution Submission
Submit solution for AOC challenge. Will give feedback on whether your submission was correct and will indicate time 
until you can re-submit your solution if it is incorrect.

```console
usage: aoc submit [-h] -y YEAR -d DAY -p {1,2}

optional arguments:
  -h, --help            show this help message and exit
  -y YEAR, --year YEAR  AOC input download year (2015-2021).
  -d DAY, --day DAY     AOC challenge day (1:25).
  -p {1,2}, --part {1,2}
                        Part of the AOC challenge you want to submit
```

