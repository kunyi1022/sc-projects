def main():
    year = ''
    with open('data/full/baby-1900.txt', 'r') as f:
        for line in f:
            if len(line) == 5:
                year = line[:4]
            else:
                name_lst = line.split(",")
                rank_b = name_lst[0]
                name1_b = name_lst[1]
                name2_b = name_lst[2]
                rank = rank_b.strip()
                name1 = name1_b.strip()
                name2 = name2_b.strip()
                print(f'{year} {rank} {name1} {name2}')




if __name__ == "__main__":
    main()