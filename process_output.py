import os

log_path = "/home/trigger/ChampSim/log_mru_new"

result_log = open("/home/trigger/ChampSim/result_mru_new.txt", "w")
result_log.write("name IPC LLC_HIT LLC_MISS DTLB_HIT DTLB_MISS L1D_HIT L1D_MISS L2C_HIT L2C_MISS STLB_HIT STLB_MISS\n")
for root, dir, files in os.walk(log_path):
    for file in files:
        result_log.write(file + " ")
        file = open(root + "/" + file, "r")
        lines = file.readlines()
        for line in lines:
            if "CPU 0 cumulative IPC:" in line:
                splitted = line.split()
                result_log.write(splitted[4] + " ")
            if "LLC TOTAL" in line:
                splitted = line.split()
                result_log.write(splitted[5] + " " + splitted[7] + " ")
            if "cpu0_DTLB TOTAL" in line:
                splitted = line.split()
                result_log.write(splitted[5] + " " + splitted[7] + " ")
            if "cpu0_L1D TOTAL" in line:
                splitted = line.split()
                result_log.write(splitted[5] + " " + splitted[7] + " ")
            if "cpu0_L2C TOTAL" in line:
                splitted = line.split()
                result_log.write(splitted[5] + " " + splitted[7] + " ")
            if "cpu0_STLB TOTAL" in line:
                splitted = line.split()
                result_log.write(splitted[5] + " " + splitted[7] + "\n")
        file.close()
