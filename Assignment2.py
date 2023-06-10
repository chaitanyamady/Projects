def DateQuarter(date, quarter):
    year = int(date[:4])
    month = int(date[4:])

    if month == 1:
        previous_month = str(year - 1) + '12'
    else:
        previous_month = str(year) + str(month - 1).zfill(2)

    current_quarter = quarter + "_" + str(year)

    if quarter == "Q1":
        previous_quarter = "Q4" + "_" + str(year - 1)
    else:
        quarter_number = int(quarter[1:])
        previous_quarter = "Q" + str(quarter_number - 1) + "_" + str(year)

    future_month = str(year + 1) + str(previous_month[-2:])

    result_dict = {
        'previous_month': previous_month,
        'current_quarter': current_quarter,
        'previous_quarter': previous_quarter,
        'future_year_month': future_month
    }

    return result_dict


result = DateQuarter("202208", "Q3")
print(result)
