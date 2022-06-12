import requests
import argparse
import pprint
import os
import sys
import re
import json
from datetime import datetime
from decouple import config
from typing import Sequence
from typing import Optional
from typing import Tuple
from typing import Dict

HERE = os.path.dirname(os.path.abspath(__file__))
AOC_URL = "https://adventofcode.com"

TOO_QUICK = r"You gave an answer too recently"
WRONG = r"That's not the right answer"
RIGHT = r"That's the right answer"
DONE = r"You don't seem to be solving"

def get_cookie_headers() -> Dict[str, str]:
	return {'session' : config('COOKIE')}

def valid_day_int(s: str) -> int:
	"""
	Custom type for --day argparse argument.
	Returns error if day not in range (1, 25)
	"""
	try:
		day = int(s)
	except:
		raise argparse.ArgumentTypeError(f"Expected integer from range (1:25), received {s}")
	
	if day < 0 or day > 25:
		raise argparse.ArgumentTypeError(f"Day can only be in range (1:25), received {s}")
	
	return day

def latest_aoc() -> int:
	"""
	Returns the latest AOC to ever have occured or occuring.
	"""
	latest_aoc = datetime.now().year
	if datetime.now().month != 12:
		return latest_aoc - 1
	return latest_aoc

def valid_year_int(s: str) -> int:
	"""
	Custom type for the --year argparse argument.
	Will return an error if the AOC for the current year has not happend.
	Year < 2015 will also return an error, as that was the first AOC.
	"""
	latest_year = latest_aoc()
	try:
		year = int(s)
	except:
		raise argparse.ArgumentTypeError(f"Expected integrer from (2015 - {latest_year}), recieved {s}")
	
	if year < 2015 or year > latest_year:
		raise argparse.ArgumentTypeError(f'No AOC for the year {year}') 	
	
	return year

def aoc_ongoing() -> bool:
	"""
	Returns true if aoc is currently ongoing (it is the month of december)
	"""
	return datetime.now().month == 12

def current_aoc() -> Tuple[str, str]:
	return (datetime.now().year, datetime.now().day)

def get_input(year: int, day: int) -> str:
	"""
	Gets AOC challenge input.
	"""
	url = f"{AOC_URL}/{year}/day/{day}/input"
	data = requests.get(url, cookies=get_cookie_headers())
	return data

def post_answer(year: int, day: int, part: int, answer: int) -> str:
	"""
	Submits AOC challenge answer
	"""
	params = {'level': part, 'answer' : answer}
	headers = {'Content-Type': 'application/x-www-form-urlencoded'}
	url = f"{AOC_URL}/{year}/day/{day}/answer"
	data = requests.post(
		url, data={"level": part, "answer" : answer},
		cookies=get_cookie_headers()
	)
	return data.content.decode()		

def aoc(argv: Optional[Sequence[str]] = None) -> None:
	aoc_occuring = aoc_ongoing()
	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers(dest="command")
	subparsers.required = True	

	download_parser = subparsers.add_parser('download', help="Download AOC Input")
	submit_parser = subparsers.add_parser('submit', help="Submit AOC Answer")
	
	for subparser in (download_parser, submit_parser):
		subparser.add_argument(
			"-y", "--year", type=valid_year_int, 
			required= not aoc_occuring, 
			help=f"AOC input download year (2015-{latest_aoc()})."
		)
		subparser.add_argument(
			"-d", "--day", type=valid_day_int, 
			required= not aoc_occuring,
			help="AOC challenge day (1:25)."
		)

	submit_parser.add_argument(
		"-p", "--part", choices=(1, 2),
		type=int, required=True,
		help="Part of the AOC challenge you want to submit"
	)
	
	args = parser.parse_args(argv)		
	if aoc_occuring:
		args.year, args.day = current_aoc()
	
	if args.command == 'download':
		aoc_dir = os.path.join(HERE, str(args.year))

		if not os.path.isdir(f"{HERE}/{args.year}"):
			os.mkdir(os.path.join(aoc_dir))
		
		aoc_input = get_input(args.year, args.day)
		if aoc_input.status_code != 200:
			raise requests.exceptions.HTTPError(f"HTTP error {aoc_input.status_code}")
		
		with open(f"{aoc_dir}/day{args.day}input.txt", "w") as f:
			f.write(aoc_input.content.decode())
	
	if args.command == 'submit':
		answer = int(input("Enter your answer "))
		content = post_answer(args.year, args.day, args.part, answer)	
		
		if re.search(TOO_QUICK, content):
			print(re.search(r"<article><p>\s*?(.*)\s*?<a", content).group(1))
			return 1	
		
		if re.search(WRONG, content):
			print(WRONG)
			return 1		

		if re.search(RIGHT, content):	
			print(f'\033[42m{RIGHT}\033[m')
			return 0
		else:
			print(re.search(r"<article><p>\s*?(.*)\s*?<a", content).group(1))
			return 1

