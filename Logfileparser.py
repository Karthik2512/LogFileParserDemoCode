def func_finding_error(filepath,parse_index):
    import re
    count = 0
    with open(filepath, 'r', encoding='utf-8') as logf:
        logf.seek(parse_index)
        for i in logf:
            x = re.findall("error", i)
            count = count + len(x)
        parse_index = logf.tell()
    return (parse_index, count)