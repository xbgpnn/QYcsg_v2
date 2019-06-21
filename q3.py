# import datetime
# day = datetime.date(2019,5,20)
# print(day.strftime('%j'))


from datetime import datetime


def is_leap_year(year):
    # 判断年份是平年还是闰年
    is_leap = False
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leap = True
    return is_leap


def main():
    input_date_str = input('请输入日期（yyyy/mm/dd）:')
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')
    print(input_date)

    year = input_date.year
    month = input_date.month
    day = input_date.day

    # 月份-天数字典
    month_day_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    # 天数-月份字典
    # day_month_dict = {30: {4, 6, 9, 11}, 31: {1, 3, 5, 7, 8, 10, 12}}

    days = day

    for i in range(1, month):
        days += month_day_dict[i]

    if is_leap_year(year) and month > 2:
        days += 1
    print('这是{}年的第{}天'.format(year, days))


if __name__ == '__main__':
    main()