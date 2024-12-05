reports = []
total = 0
repeat = True
with open("input.txt", "r") as f:
    for line in f:
        reports.append(line.strip("\n").split(" "))
    while repeat == True:

        for report in reports:
            for i in range(len(report)-1):
                if report[i] < report[i+1]:
                    if i == 0:
                        initial_state = "up"
                    else:
                        state = "up"
                else:
                    if i == 0:
                        initial_state = "down"
                    else:
                        state = "down"
                if i != 0 :
                    if initial_state != state:
                        repeat = False
                diff = abs(int(report[i+1]) - int(report[i]))
                if not ( diff >=1 and diff <= 3):
                    repeat == False
                total += 1
            
            






    

if __name__ == "__main__":
    print(total)