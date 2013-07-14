#include <gmpxx.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <boost/lexical_cast.hpp>
#include <sstream>
#include <boost/math/special_functions/pow.hpp>

namespace {
const size_t digitNumber = 9;
}

template <typename Number>
struct FibonacciPair {
    FibonacciPair()
    : current(0)
    , next(1)
    , index(0)
    {}
    void advance() {
        next += current;
        std::swap(next, current);
        ++index;
    }
    Number current;
    Number next;
    size_t index;
};


bool isPandigital(const std::string& s) {
    if (s.length() < digitNumber) {
        return false;
    }
    std::vector<bool> v(digitNumber, false);
    for (size_t i=0; i!=digitNumber; ++i) {
        char c=s[i];
        char llimit = '1';
        char ulimit = '9';
        if ((c>=llimit) && (c<=ulimit)) {
            size_t pos = c-llimit;
            if (v[pos]) {
                return false;
            } else {
                v[pos] = true;
            }
        } else {
            return false;
        }
    }
    return true;
}

int main() {
    const size_t decimalBase = 10;
    const size_t threshold = boost::math::pow<digitNumber>(decimalBase);
    FibonacciPair<mpz_class> exact;
    FibonacciPair<mpz_class> notexact;
    while (true) {
        if (isPandigital(boost::lexical_cast<std::string>(notexact.current))) {
            if (isPandigital(boost::lexical_cast<std::string>(exact.current))) {
                std::cout << exact.index << std::endl;
                exit(EXIT_SUCCESS);
            }
        }
        notexact.advance();
        exact.advance();
        notexact.current %= threshold;
    }
}
