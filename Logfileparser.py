'''
This module parses through the logfiles. It uses the variable 'parse_index' to do so. This parse_index keeps track of the point
where the file was last read and acts a pointer/cursor to make sure the log files are read sequentially without missing anything
'''

def func_finding_error(filepath,parse_index):
    import re
    count = 0
    print(filepath)
    with open(filepath, 'r', encoding='utf-8') as logf:
        logf.seek(parse_index)
        for i in logf:
            x = re.findall("error", i)
            count = count + len(x)
        parse_index = logf.tell()
    return (parse_index, count)