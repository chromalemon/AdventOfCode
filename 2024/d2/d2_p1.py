reports = []
total = 0
safe = True

with open("input.txt", "r") as f:
    for line in f:
        reports.append(line.strip("\n").split(" "))

    for report in reports:
        print(report)
        for i in range(len(report)-1):
            if int(report[i]) < int(report[i+1]):
                if i == 0:
                    initial_state = "up"
                    print(initial_state)
                else:
                    state = "up"
            else:
                if i == 0:
                    initial_state = "down"
                else:
                    state = "down"
            if i != 0 :
                if initial_state != state:
                    safe = False
                    

            diff = abs(int(report[i]) - int(report[i+1]))
            if not ( diff >=1 and diff <= 3):
                safe == False

        if safe == True:
            total += 1
            print("HI")
        safe = True
        
            






    

if __name__ == "__main__":

    print(total)