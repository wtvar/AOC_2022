#advent of code 2022 day 1

highest_total = 0
running_total = 0

#part1 solution
with open('input.txt') as text:
    #data = text.read()
    
    for line in text:
        data = line.strip().split('\n')
        #print(data)
        print(data)
        if int(data[0]) != "":
            running_total += int(data[0])

            print(f'running total: {running_total}')
            print(f'highest total: {highest_total}')
        else:
            print(f'end of elf')
            if running_total > highest_total:
                highest_total = running_total
                running_total = 0
                print(f'running total: {running_total}')
                print(f'highest total: {highest_total}')

            
#advent of code 2022 day 1
#part2
highest_total = 0
second_total = 0
third_total = 0
running_total = 0
count = 0
with open('input.txt') as text:
    #data = text.read()
    
    for line in text:
        data = line.strip().split('\n')
        #print(data)
        #print(data)
        if data[0] == "":
            #print(f'end of elf')
            #print(f'running total: {running_total}')
            if running_total > highest_total:
                third_total = second_total
                second_total = highest_total
                highest_total = running_total
                running_total = 0
            elif running_total > second_total:
                third_total = second_total
                second_total = running_total
                running_total = 0
            elif running_total > third_total:
                third_total = running_total
                running_total = 0
            else:
                running_total = 0
                continue
            #print(f'count: {count}')
            count += 1
            
            #print(f'highest total: {highest_total}')
            #print('----------------------------------------')
        else:
            running_total += int(data[0])
            #print(f'continuing to count')
            #print(f'running total: {running_total}')
            #print(f'highest total: {highest_total}')

    print(f'FINAL TOTAL 1st: {highest_total}')
    print(f'FINAL TOTAL 2nd: {second_total}')
    print(f'FINAL TOTAL 3rd: {third_total}')
    print(f'FINAL SUM: {highest_total + second_total + third_total}')
