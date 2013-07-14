#include <gmpxx.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <boost/lexical_cast.hpp>
#include <sstream>

template <typename Number>
struct FibonacciPair {
    FibonacciPair()
    : n1(0)
    , n2(1)
    , index(0)
    {}
    void next() {
        Number next = n1 + n2;
        n1 = n2;
        n2 = next;
        ++index;
    }
    Number n1;
    Number n2;
    size_t index;
};

const size_t threshold = 1000000000;

bool isPandigital(const std::string& s) {
    if (s.length()<9) {
        return false;
    }
    std::vector<bool> v(9, false);
    for (size_t i=0; i!=9; ++i) {
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
    FibonacciPair<mpz_class> exact;
    FibonacciPair<mpz_class> notexact;
    while (true) {
        if (isPandigital(boost::lexical_cast<std::string>(notexact.n1))) {
            if (isPandigital(boost::lexical_cast<std::string>(exact.n1))) {
                std::cout << exact.index << std::endl;
                exit(EXIT_SUCCESS);
            }
        }
        notexact.next();
        exact.next();
        notexact.n1 %= threshold;
    }
}
