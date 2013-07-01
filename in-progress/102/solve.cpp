#include <fstream>
#include <iostream>
#include <string>

namespace {
    const std::string filename = "triangles.txt";
}

int main() {
    std::cout << "Opening " << filename << " ..." << std::endl;
    std::ifstream in(filename.c_str());
    std::cout << in.rdbuf() << std::endl;
}
