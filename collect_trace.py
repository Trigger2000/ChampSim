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
    progress_counter = 0
    for test in group:
        results = open("/home/trigger/ChampSim/log_mru_new/log_" + test + ".txt", "w")
        print(progress_counter)
        progress_counter += 1
        result = subprocess.run([exec_file, "--warmup_instructions", "10000000",
                                          "--simulation_instructions" , "50000000",
                                          root + "/" + test], stdout=subprocess.PIPE)
        results.write(str(result.stdout.decode('utf-8')))
        results.close()
    print("finished")

pool = multiprocessing.Pool()
for i in range(4):
    pool.apply_async(func=execute_bench, args=(groups[i], i,))

pool.close()
pool.join()
