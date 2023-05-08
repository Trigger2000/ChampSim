#include <string>
#include <cstring>
#include <iostream>

#include "ooo_cpu.h"

namespace
{
    uint64_t cur_ip = 0;
    uint8_t cur_predict = 0;
    bool first_init = false;
} // namespace

void O3_CPU::initialize_branch_predictor() { std::cout << "CPU " << cpu << " Oracle branch predictor" << std::endl; }

uint8_t O3_CPU::predict_branch(uint64_t ip)
{
    if (!first_init) {
        std::string line;
        std::getline(log_file, line);
        cur_ip = std::stoi(strtok(const_cast<char*>(line.c_str()), " "));
        cur_predict = std::stoi(strtok(nullptr, " "));
        first_init = true;
    }

    if (ip == cur_ip) {
        std::string line;
        std::getline(log_file, line);
        if (log_file.eof()) {
            return cur_predict;
        }
        uint8_t result = cur_predict;
        cur_ip = std::stoi(strtok(const_cast<char*>(line.c_str()), " "));
        cur_predict = std::stoi(strtok(nullptr, " "));
        // std::cout << cur_ip << " " << static_cast<int64_t>(cur_predict) << std::endl;
        return result;
    }
    return 1;
}

void O3_CPU::last_branch_result(uint64_t ip, uint64_t branch_target, uint8_t taken, uint8_t branch_type)
{
    // (void*)ip;
}
