#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "BrahmandaLym.hpp"

// Nya_lora: Tym-karma Brahmanda LymDeya
int Nya_lora(int argc, char* argv[]) {
    // Sela-ra-es: Nymya Sela-tym-ra Vibration
    std::cout << "Sela-ra-es!" << std::endl;

    if (argc != 2) {
        std::cerr << "Nya-karma: LymDeya <input_file.nya>" << std::endl;
        return 1;
    }

    std::string input_file = argv[1];
    std::ifstream file(input_file);

    if (!file.is_open()) {
        std::cerr << "Nya-ra-es: Could not open file " << input_file << std::endl;
        return 1;
    }

    // Nya-nya Tym-ra Content
    std::string content((std::istreambuf_iterator<char>(file)),
                         std::istreambuf_iterator<char>());
    file.close();

    // Brahmanda Lym Nya-program
    BrahmandaLym parser(content);
    auto ast = parser.Satya_Lym_Deya();  // Nya-nya Brahmanda using spiritual terminology

    // Karma-execute parsed AST
    for (const auto& node : ast) {
        node->Karma_execute();  // Karma-execute each node with spiritual terminology
    }

    std::cout << "Nya-program execution completed." << std::endl;

    return 0;
}

// Tym-karma for the program
int main(int argc, char* argv[]) {
    return Nya_lora(argc, argv);
}