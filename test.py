import re
from datetime import datetime
import dateutil.parser as dparser


def parse_out_time(s3_object):
    types = [r'\d{4}-\d{2}-\d{2}', r'\d{4}\d{2}\d{2}', r'\d{4}/\d{2}/\d{2}',
             r'\d{2}-\d{2}-\d{4}', r'\d{2}\d{2}\d{4}', r'\d{2}/\d{2}/\d{4}']
    dates = []
    sample = s3_object

    for i in range(len(types)):
        g = (re.findall(types[i], sample))
        dates.extend(g)

    if not dates:
        print(sample)
    else:
        for i in range(len(dates)):
            try:
                f = dparser.parse(dates[i], fuzzy=True)
                g = sample.replace(dates[i], "")
                sample = g
            except ValueError:
                print("not valid date")

    formatted = sample.replace("//", "/")
    formatted = formatted.lstrip("/")
    return formatted


formatted_s3_object = parse_out_time('20240532Out-TDW-Data/20240610/T_MASTER_SEC20240610.csv')
print(formatted_s3_object)