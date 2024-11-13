import sys
from modules.scrapy_script import *

RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

if __name__ == '__main__':
    try:
        args = sys.argv[1:]
        arg_dict = {'year': '', 'week': '', 'type': ''}

        for arg in args:
            if '=' in arg:
                key, value = arg.split('=', 1)
                if key in arg_dict:
                    arg_dict[key] = value
                else:
                    print(f"{RED}Error:{RESET} Unexpected argument key: {YELLOW}'{key}'{RESET}")
                    sys.exit(1)
            else:
                print(f"{RED}Error:{RESET} Invalid argument format: {YELLOW}'{arg}'{RESET}")
                sys.exit(1)

        if any(value == '' for value in arg_dict.values()):
            print(f"{RED}Error:{RESET} Missing value for one or more required arguments.")
            sys.exit(1)

        scraper = CrawlerProcess()
        scraper.crawl(custom_spider, arg_dict)
        scraper.start()

    except Exception as e:
        print(f"{RED}Error:{RESET} {YELLOW}'{e}'{RESET} at main function.")
        sys.exit(1)