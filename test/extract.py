muitiply_by = 1.52


with open('convert.txt', 'r') as f:
    css = f.read()

numbers = ''.join((ch if ch in '0123456789.' else ' ') for ch in css)
listOfNumbers = [i for i in numbers.split()]
print(listOfNumbers)

for number in listOfNumbers:
    css = css.replace(number, str(round(float(number) * muitiply_by, 3) ))

with open('convertModified.txt', 'w') as f:
    f.write(css)
