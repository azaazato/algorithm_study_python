def hanoi(disk_number, f, t, w, tower_dict):

    if disk_number > 0:
        hanoi(disk_number-1, f, w, t, tower_dict)
        tower_dict[t].insert(0, tower_dict[f].pop(0))
        print((tower_dict['left'], tower_dict['center'], tower_dict['right']))
        hanoi(disk_number-1, w, t, f, tower_dict)


if __name__ == '__main__':
    disk_number = int(input())
    tower_dict = {'left': [i for i in range(1, disk_number+1)], 'center': [], 'right': []}
    print((tower_dict['left'], tower_dict['center'], tower_dict['right']))
    hanoi(disk_number, 'left', 'right', 'center', tower_dict)
