#include <iostream>
#include <boost/lexical_cast.hpp>
#include <algorithm>

bool isBouncy(size_t number)
{
    std::string s = boost::lexical_cast<std::string>(number);
    bool increasing = std::is_sorted(s.begin(), s.end());
    bool decreasing = std::is_sorted(s.rbegin(), s.rend());
    return !increasing && !decreasing;
}

int main(int argc, char* argv[])
{
    const size_t p_base = 100;
    const size_t p_part = 99; 
    size_t start=0;
    size_t bouncyCount = 0;
    while (true) {
        ++start;
        if (isBouncy(start)) {
            ++bouncyCount;
        }
        if ((p_base*bouncyCount) > (start*p_part)) {
            break;
        }
    }
    std::cout << start-1 << std::endl;
}
