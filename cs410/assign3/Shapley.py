import sys
import math


def write_output(shapleys):
    o = open("Shapley.txt", "w")
    j = 1
    for i in shapleys:
        o.write(f"{j}, {i}\n")
        j += 1
    o.close()
    print("Shapley Values Saved to file: Shapley.txt")


def shapley(in_file):
    # extract info from input file -done
    f = open(in_file, "r")
    n = int(f.readline())

    lines = []
    line_buff = f.readline()
    while line_buff:
        line = line_buff.split("}")

        # clean up our coalition array
        line[0] = line[0].replace("{", "").split(",")
        line[0] = [eval(i) for i in line[0]]
        line[1] = int(line[1].replace(",", "").replace("\n", ""))

        lines.append(line)
        line_buff = f.readline()
    f.close()

    # info extracted, time to calculate shapleys

    shapleys = []
    c = 1 / math.factorial(n)

    # calc shapleys - only thing left
    for i in range(1, n + 1):
        p_shapley = 0

        # summation loop
        for j in lines:
            # TODO: go through every coalition and see if a value needs to be calculated
            coalition = j[0]
            utility = j[1]
            m_utility = 0
            if i in coalition:
                m_utility = utility
                other_agents = []
                for x in coalition:
                    if x != i:
                        other_agents.append(x)

                if other_agents:
                    sub_ind = 0
                    for x in lines:
                        x[0].sort()
                        other_agents.sort()
                        if x[0] == other_agents:
                            m_utility -= lines[sub_ind][1]
                            break
                        sub_ind += 1
            sub_coal_len = (coalition.__len__() - 1)
            m_utility *= math.factorial(sub_coal_len)
            m_utility *= math.factorial(n - sub_coal_len - 1)
            p_shapley += m_utility

        p_shapley *= c
        shapleys.append(p_shapley)

    # write to output -done
    write_output(shapleys)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: shapley.py <filename>")
        print("   where <filename> is a path to a txt file:")
        print(" Exiting...")
        sys.exit(-1)
    shapley(sys.argv[1])
