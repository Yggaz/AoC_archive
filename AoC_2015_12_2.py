import re

json = open('input_2015_12.txt', 'r', encoding='utf-8').read()
while True:
    attr_start = json.find(':"red"')
    if attr_start > 0:
        left_brackets = 0
        right_brackets = 0
        cur_pos = attr_start
        while left_brackets < 1:
            cur_pos -= 1
            if json[cur_pos] == '}':
                left_brackets -= 1
            elif json[cur_pos] == '{':
                left_brackets += 1
        struct_start = cur_pos
        cur_pos = attr_start
        while right_brackets < 1:
            cur_pos += 1
            if json[cur_pos] == '}':
                right_brackets += 1
            elif json[cur_pos] == '{':
                right_brackets -= 1
        struct_end = cur_pos
        json = json[:struct_start] + json[struct_end + 1:]
    else:
        break

print(
      sum(
          map(
              int,
              re.findall(r'-?\d+',
                         json
                         )
          )
      )
)
