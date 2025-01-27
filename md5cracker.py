import os, sys
import hashlib

def main() -> int:
    WELCOME_STR = """
___  ________ _____ _____ ______  ___  _____  _   __
|  \\/  |  _  \\  ___/  __ \\| ___ \\/ _ \\/  __ \\| | / /
| .  . | | | |___ \\| /  \\/| |_/ / /_\\ \\ /  \\/| |/ / 
| |\\/| | | | |   \\ \\ |    |    /|  _  | |    |    \\ 
| |  | | |/ //\\__/ / \\__/\\| |\\ \\| | | | \\__/\\| |\\  \\
\\_|  |_/___/ \\____/ \\____/\\_| \\_\\_| |_/\\____/\\_| \\_/
                                                    
                                                    """  
    HELP_STR = f"\nUsage: python3 {sys.argv[0]} -w wordlist_path.txt hash.txt\n"

    print(WELCOME_STR)

    wordlist = ''
    hash_file = ''
    argument = ''

    if len(sys.argv) == 1:
        print(HELP_STR)
        return 1

    for arg in sys.argv:
        if arg[0] == '-':
            argument = 'wordlist'
            continue
        elif argument:
            if argument == 'wordlist':
                wordlist = arg
            argument = ''
        else:
            hash_file = arg

    if hash_file and wordlist:
        if not os.path.isfile(hash_file):
            print('f{hash_file} file not found')
            return 1
        if not os.path.isfile(wordlist):
            print(f'{wordlist} file not found')
            return 1

        print("Starting brute md5...")

        hash_fstream = open(hash_file)
        hash_str = hash_fstream.readline().replace('\n', '')
        hash_fstream.close()

        with open(wordlist) as file:
            lines = file.readlines()
        
        line_cnt = len(lines)
        print(f"Wordlist contain {line_cnt} strings\n")

        found_password = 0
        for ind, line in enumerate(lines):
            line = line.strip()
            percent = ind/line_cnt*100
            print("\r                                                  ", end='')
            print(f"\r{ind}/{line_cnt}: {percent:.2f}%", end='')

            if hash_str == hashlib.md5(line.encode('utf-8')).hexdigest():
                print(f"PASSWORD FOUND: {line}")
                found_password = 1
                break
            
        if not found_password:
            print("\n\nPassword had not been found :(") 

    else:
        print(HELP_STR)
        return 1

    return 0

if __name__ == '__main__':
    main()
