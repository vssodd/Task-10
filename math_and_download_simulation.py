import math
import time

# Part 1: Logarithm or Exponential based on input
n = int(input("Enter the number of values: "))

for _ in range(n):
    x = float(input("Enter a number: "))
    if x > 0:
        rounded_x = math.ceil(x)
        result = math.log(rounded_x)
        print('x =', rounded_x, 'log(x) =', result)
    else:
        rounded_x = math.floor(x)
        result = math.exp(rounded_x)
        print('x =', rounded_x, 'exp(x) =', result)

# Part 2: File download simulation
seconds = 0
downloaded = 0
file_size = float(input('Enter file size (MB): '))
con_speed = float(input('Enter internet speed (MB/s): '))

while downloaded < file_size:
    downloaded += con_speed
    if downloaded > file_size:
        downloaded = file_size
    percentage = (downloaded / file_size) * 100
    seconds += 1
    print('Elapsed:', seconds, 'sec.', 'Downloaded:', downloaded, 'of', file_size, 'MB', round(percentage), '%')
    time.sleep(0.5)

print('Download completed in', seconds, 'seconds.')
