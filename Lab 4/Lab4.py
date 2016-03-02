def main():
    f = open("names.txt", "r")
    print("Finding Names")
    find_my_name(f)
    print("Done Finding names")
    print('---- Calling appeared_first_in ----')
    print('Jessica first appeared in', appeared_first_in(f, 'Jessica'))
    print('Kharmen first appeared in', appeared_first_in(f, 'Kharmen'))
    print('Orchid first appeared in', appeared_first_in(f, 'Orchid'))
    print('C3P0 first appeared in', appeared_first_in(f, 'C3P0'))
    print('---- appeared_first_in finished ----')
    print('---- Calling get_summary_for_name ----')
    print(get_summary_for_name(f, 'Aragorn'))
    print(get_summary_for_name(f, 'Legolas'))
    print(get_summary_for_name(f, 'Leia'))
    print(get_summary_for_name(f, 'Kelly'))
    print('---- get_summary_for_name finished ----')


def find_my_name(f):
    f.seek(0)
    for line in f:
        if ",Chris," in line:
            print(line)
def appeared_first_in(f, name):
    f.seek(0)
    for line in f:
        if "," + name + "," in line:
            return int(line[0:4])
    return -1
def get_summary_for_name(f, name):
    f.seek(0)
    first_year =0
    count = 0
    total = 0
    for line in f:
        item = line.split(",")
        if item[1] == name:
            if(first_year == 0):
                first_year = int(item[0])
            count+=1
            total += int(item[3])
    return '{}: appears in {} years, first in {}, {:,} total babies'.format(
            name, count, first_year, total)

main()