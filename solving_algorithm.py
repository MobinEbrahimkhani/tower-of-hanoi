def solving(num_of_disks):
    pole_1, pole_2, pole_3 = '1', '2', '3'
    result = []

    if num_of_disks % 2 == 0:
        pole_2, pole_3 = pole_3, pole_2


    total_moves = (2 ** num_of_disks) - 1
    poles = { '1': list(range(num_of_disks, 0, -1)), '2': [], '3': [] }


    for move in range(1, total_moves + 1):
        if move % 3 == 1:
            if poles[pole_1] and (not poles[pole_3] or poles[pole_1][-1] < poles[pole_3][-1]):
                origin_pole = pole_1
                destination_pole = pole_3
            else:
                origin_pole = pole_3
                destination_pole = pole_1
        elif move % 3 == 2:
            if poles[pole_1] and (not poles[pole_2] or poles[pole_1][-1] < poles[pole_2][-1]):
                origin_pole = pole_1
                destination_pole = pole_2
            else:
                origin_pole = pole_2
                destination_pole = pole_1
        else:
            if poles[pole_2] and (not poles[pole_3] or poles[pole_2][-1] < poles[pole_3][-1]):
                origin_pole = pole_2
                destination_pole = pole_3
            else:
                origin_pole = pole_3
                destination_pole = pole_2


        disk = poles[origin_pole].pop()
        poles[destination_pole].append(disk)
        result.append([origin_pole,destination_pole])
    
    return result


