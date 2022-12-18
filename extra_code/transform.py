import locale
import re

def money_to_float(money: str) -> float:
  locale.setlocale(locale.LC_ALL, 'en_US')
  return locale.atof(money.strip("$"))

def get_apartment_number(address: str) -> int:
    if regex := re.match(".*?UNIT (\d*).*?", address):
        return regex.group(1)
    elif regex := re.match(".*?#(\d*).*?", address):
        return regex.group(1)
