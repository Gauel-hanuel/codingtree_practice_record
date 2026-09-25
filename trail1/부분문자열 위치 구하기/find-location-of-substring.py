input_str = input()
target_str = input()

import sys

if target_str in input_str:
    for i in range(len(input_str) - len(target_str)+1):
        if input_str[i:i+len(target_str)] == target_str:
            print(i)
            sys.exit()
        else:
            pass
else:
    print(-1)
    
        
