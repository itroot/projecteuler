#include <boost/lexical_cast.hpp>
#include <iostream>
#include <algorithm>

int main(int argc, char* argv[]) {
    if (2 != argc) {
        std::cout << "=)" << std::endl;
        return 1;
    }
    size_t counter = 0;
    size_t power = boost::lexical_cast<size_t>(argv[1]);
    size_t number = 1;
    for (size_t i=0; i!=power; ++i) {
        number *= 10;
    }
    std::cout << "Doing for " << number << std::endl;
    for (size_t i=1; i!=number; ++i) {
        if (0==i%10) {
            continue;
        }
        std::string n = boost::lexical_cast<std::string>(i);
        std::reverse(n.begin(), n.end());
        size_t i2 = boost::lexical_cast<size_t>(n);
        size_t r = i2+i;
        std::string rs = boost::lexical_cast<std::string>(r);
        bool ok=true;
        for (size_t ri=0; ri!=rs.size(); ++ri) {
            switch(rs[ri]) {
                case '1' : case '3' : case '5' : case '7' : case '9' : break;
                default: ok = false;
            }
        }
        ok && ++counter;
    }
    std::cout << counter << std::endl;
}
