def main(n):
    source, auxiliary, target = '1', '2', '3'
    result = []

    if n % 2 == 0:
        auxiliary, target = target, auxiliary


    total_moves = (2 ** n) - 1
    stacks = { '1': list(range(n, 0, -1)), '2': [], '3': [] }


    for move in range(1, total_moves + 1):
        if move % 3 == 1:
            if stacks[source] and (not stacks[target] or stacks[source][-1] < stacks[target][-1]):
                from_peg = source
                to_peg = target
            else:
                from_peg = target
                to_peg = source
        elif move % 3 == 2:
            if stacks[source] and (not stacks[auxiliary] or stacks[source][-1] < stacks[auxiliary][-1]):
                from_peg = source
                to_peg = auxiliary
            else:
                from_peg = auxiliary
                to_peg = source
        else:
            if stacks[auxiliary] and (not stacks[target] or stacks[auxiliary][-1] < stacks[target][-1]):
                from_peg = auxiliary
                to_peg = target
            else:
                from_peg = target
                to_peg = auxiliary


        disk = stacks[from_peg].pop()
        stacks[to_peg].append(disk)
        result.append(f"from {from_peg} to {to_peg}")
    return result
    
print(main(4))


