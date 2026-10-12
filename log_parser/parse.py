import re
from pathlib import Path

pattern = r'\d{1,3}(\.\d{1,3}){3}'

def parse_log(path):
    success = []
    failure = []
    try:
        with open(path, 'r') as file:
            for line in file:
                if 'successfully' in line:
                    ips = re.search(pattern,line)
                    if ips:
                        success.append(ips.group())
                if 'Failed' in line:
                    ips = re.search(pattern,line)
                    if ips:
                        failure.append(ips.group())
        return success,failure
    except FileNotFoundError:
        print(f'File {path} not found.')
        return [],[]

filename = Path(__file__).parent / 'logs.txt'

success,failure = parse_log(filename)

def count_map(iplist):
    count_dict = {}
    for i in iplist:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    count_dict = dict(sorted(count_dict.items(),key = lambda x:x[1],reverse=True))
    return count_dict

if __name__ == "__main__":
    successet = count_map(success)
    failset = count_map(failure)

    for key in successet:
        print(f"IP : {key} -- Successful Attempts : {successet[key]}")


    for key in failset:
        print(f"IP : {key} -- Failed Attempts : {failset[key]}")
        if failset[key] > 5:
            print(f"IP : {key} has more than 5 failed attempts. Please check for potential threats.")
