import os
import subprocess
import multiprocessing

benchs_path = "/home/trigger/benchs"
exec_file = "/home/trigger/ChampSim/bin/champsim"

# my laptop has 4 physical cores
groups = [[], [], [], []]
counter = 0

for root, dir, files in os.walk(benchs_path):
    for file in files:
        groups[counter % 4].append(file)
        counter += 1

# print(groups)

def execute_bench(group, counter):
    results = open("/home/trigger/ChampSim/result_hp_" + str(counter) + ".txt", "w")
    results.write("name IPC MPKI\n")
    progress_counter = 0
    for test in group:
        print(progress_counter)
        progress_counter += 1
        result = subprocess.check_output([exec_file, "--warmup_instructions", "50000000",
                                          "--simulation_instructions" , "200000000", 
                                          "--log_file", "/home/trigger/ChampSim/log_hp/log_" + test + ".txt",
                                          root + "/" + test])
        splitted = result.split()
        results.write(test + " " + str(float(splitted[len(splitted) - 1 - splitted[::-1].index(b'IPC:') + 1])) + " " +
                      str(float(splitted[splitted.index(b'MPKI:') + 1])) + "\n")
        results.flush()
    print("finished")
    results.close()

pool = multiprocessing.Pool()
for i in range(4):
    pool.apply_async(func=execute_bench, args=(groups[i], i,))

pool.close()
pool.join()
