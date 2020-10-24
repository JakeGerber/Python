"""
Isolate the Decimal part of a Number
"""

def decimal_isolate(number, digitAmount):
  """
  Isolates the decimal part of a number.
  If digitAmount > 0 round to that decimal place, else print the entire decimal.
  >>> decimalIsolate(35.345, 1)
  0.3
  >>> decimalIsolate(89.345, 2)
  0.34
  >>> decimalIsolate(89.345, 3)
  0.345
  """
  if (digitAmount > 0):
    return round(number - int(number), digitAmount)
  return number - int(number)