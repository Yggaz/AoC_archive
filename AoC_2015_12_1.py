import re

print(
      sum(
          map(
              int,
              re.findall(r'-?\d+',
                         open('input_2015_12.txt', 'r', encoding='utf-8').read()
                         )
          )
      )
)
