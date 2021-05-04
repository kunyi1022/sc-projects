"""
File: Milestone1.py
Name: 林坤毅 Jordan
-----------------------
This file tests the milestone 1 for
our babyname.py project
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    if name not in name_data:
        name_data[name] = {year: rank}
    elif name in name_data:
        if year not in name_data[name]:
            name_data[name][year] = rank
        elif year in name_data[name]:
            if int(rank) < int(name_data[name][year]):
                name_data[name] = {year: rank}

        # for check_year, check_rank in name_data[name].items():
        #     if year != check_year:
        #         name_data[name][year] = rank
        #         break
        #         # dictionary changed size during iteration
        #         # https://www.itread01.com/content/1544689808.html
        #     elif year == check_year and int(rank) < int(check_rank):
        #         name_data[name] = {year: rank}

# 加基本資料（名子、年、排名）
# 同名不同年份的要再額外加資料
# 同年同名 儲存較低排名的（較前面的）

# ------------- DO NOT EDIT THE CODE BELOW THIS LINE ---------------- #


def test1():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    print('--------------------test1----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test2():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    # add_data_for_name(name_data, '2001', '104', 'Kylie')
    print('--------------------test2----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test3():
    name_data = {'Kylie': {'2010': '57'}, 'Sammy': {'1980': '451', '1990': '200'}, 'Kate': {'2000': '100'}}
    add_data_for_name(name_data, '1990', '900', 'Sammy')
    add_data_for_name(name_data, '2010', '400', 'Kylie')
    add_data_for_name(name_data, '2000', '20', 'Kate')
    print('-------------------test3-----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test4():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    add_data_for_name(name_data, '2000', '108', 'Kate')
    add_data_for_name(name_data, '1990', '200', 'Sammy')
    add_data_for_name(name_data, '1990', '90', 'Sammy')
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('--------------------test4----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def main():
    args = sys.argv[1:]
    if len(args) == 1 and args[0] == 'test1':
        test1()
    elif len(args) == 1 and args[0] == 'test2':
        test2()
    elif len(args) == 1 and args[0] == 'test3':
        test3()
    elif len(args) == 1 and args[0] == 'test4':
        test4()


if __name__ == "__main__":
    main()
