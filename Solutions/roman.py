roman_to_hindu_arabic = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1,
}

roman = input('Enter a Roman numeral: ')

hindu_arabic_equivalents = []

for digit in roman:
    if digit not in roman_to_hindu_arabic:
        # raise is a Python statement to raise (or "throw") an exception (error)
        # if we do this, the program will stop, which is what we want
        raise ValueError(f"Bad Roman digit: {digit}")
    hindu_arabic_equivalents.append(roman_to_hindu_arabic[digit])

for index in range(len(hindu_arabic_equivalents) - 1): # don't examine last one
  if hindu_arabic_equivalents[index] < hindu_arabic_equivalents[index + 1]:
      hindu_arabic_equivalents[index] *= -1 # make it negative

print(sum(hindu_arabic_equivalents))
