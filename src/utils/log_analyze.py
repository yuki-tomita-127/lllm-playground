import json
import sys


# TODO: This code was written in a hurry and not carefully, so I need to rewrite it someday. (For now, it's working.)
load_start_time = 0
load_end_time = 0
gguf_file_name = ''

speed_list = []
first_eval_speed = 0
first_generate_speed = 0
second_eval_speed = 0
second_generate_speed = 0
third_eval_speed = 0
third_generate_speed = 0

file_name = sys.argv[1]

with open(file_name, 'r', encoding="utf-8") as file:
    flag1 = False
    flag2 = False
    for i, line in enumerate(file):
        if i == 5:
            line = line.strip()
            # line dump to json
            converted_line = json.loads(line)
            load_start_time = int(converted_line["timestamp"])
            print(f"load_start_time: {load_start_time}")
        
        elif i == 6:
            line = line.strip()
            # search index for 'from' in line
            start_index = line.find('from') + 5
            # search index for '.gguf' in line
            end_index = line.find('.gguf')
            path = line[start_index:end_index]
            # extract file name from path
            file_name = path.split('/')[-1]
            gguf_file_name = file_name
            print(f"gguf_file_name: {gguf_file_name}")
        
        elif line.startswith('llama server'):
            flag1 = True

        elif flag1 and line.startswith('{"timestamp"'):
            line = line.strip()
            # line dump to json
            converted_line = json.loads(line)
            load_end_time = int(converted_line["timestamp"])
            print(f"load_end_time: {load_end_time}")
            flag1 = False
            flag2 = True
        
        elif flag2 and line.startswith('print_timings'):
            if ' tokens per second' in line:
                index = line.find(' tokens per second')
                speed_list.append(line[index-5:index])
                # print(line[index-5:index])
            else:
                flag2 = False
        
        elif line.startswith('print_timings'):
            flag2 = True
            index = line.find(' tokens per second')
            speed_list.append(line[index-5:index])
            # print(line[index-5:index])

if load_start_time != 0 and load_end_time != 0:
    print(f"load_time: {load_end_time - load_start_time}")

print()

for i, speed in enumerate(speed_list):
    if i == 0:
        first_eval_speed = speed
        print(f"first_eval_speed: {first_eval_speed}")
    elif i == 1:
        first_generate_speed = speed
        print(f"first_generate_speed: {first_generate_speed}")
    elif i == 2:
        second_eval_speed = speed
        print(f"second_eval_speed: {second_eval_speed}")
    elif i == 3:
        second_generate_speed = speed
        print(f"second_generate_speed: {second_generate_speed}")
    elif i == 4:
        third_eval_speed = speed
        print(f"third_eval_speed: {third_eval_speed}")
    elif i == 5:
        third_generate_speed = speed
        print(f"third_generate_speed: {third_generate_speed}")

print()
print(f"average_eval_speed: {(float(first_eval_speed) + float(second_eval_speed) + float(third_eval_speed)) / 3:.2f}")
print(f"average_generate_speed: {(float(first_generate_speed) + float(second_generate_speed) + float(third_generate_speed)) / 3:.2f}")
