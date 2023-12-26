
import json


with open('data/log/20231227_0317.txt', 'r', encoding="utf-8") as file:
    flag1 = False
    flag2 = False
    for i, line in enumerate(file):
        if i == 5:
            line = line.strip()
            # line dump to json
            converted_line = json.loads(line)
            print(converted_line["timestamp"])
        
        elif i == 6:
            line = line.strip()
            # search index for 'from' in line
            start_index = line.find('from') + 5
            # search index for '.gguf' in line
            end_index = line.find('.gguf')
            path = line[start_index:end_index]
            # extract file name from path
            file_name = path.split('/')[-1]
            print(file_name)
        
        elif line.startswith('llama server'):
            flag1 = True

        elif flag1 and line.startswith('{"timestamp"'):
            line = line.strip()
            # line dump to json
            converted_line = json.loads(line)
            print(converted_line["timestamp"])
            flag1 = False
            flag2 = True
        
        elif flag2 and line.startswith('print_timings'):
            if ' tokens per second' in line:
                index = line.find(' tokens per second')
                print(line[index-5:index])
            else:
                flag2 = False
        
        elif line.startswith('print_timings'):
            flag2 = True
            index = line.find(' tokens per second')
            print(line[index-5:index])
