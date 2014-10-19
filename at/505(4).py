time_str_list = {
  'sec': 1,
  'min': 60,
  'hour': 60 * 60,
  'day': 60 * 60 * 24,
  'week': 60 * 60 * 24 * 7,
  'month': 60 * 60 * 24 * 30,
  'year': 60 * 60 * 24 * 365,
}

def time_convert(input_dict):
    for time_str, list_values in input_dict.items():
        first_time, last_time = time_str.split("2")
        tmp_list = ["%.2f %s" % (float(i) * time_str_list[first_time] / time_str_list[last_time], last_time) for i in list_values]
        input_dict[time_str] = tmp_list
    return input_dict

input_dict = {
    "sec2min": [20, 40],
    "min2hour": [50, 120],
    "sec2hour": [2500, 100],
    "year2hour": [3],
}
print input_dict
print time_convert(input_dict)