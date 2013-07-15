#include <gmpxx.h>
#include <iostream>
#include <fstream>
#include <bitset>
#include <boost/lexical_cast.hpp>
#include <sstream>
#include <boost/math/special_functions/pow.hpp>
#include <algorithm>

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
    const std::string digits9("123456789");
    return is_permutation(digits9.begin(), digits9.end(), s.begin());
}

template<typename Number>
bool isPanhead(const Number& number)
{
    return isPandigital(boost::lexical_cast<std::string>(number));
}

void truncate(size_t& number) {
    const size_t decimalBase = 10;
    const size_t threshold = boost::math::pow<digitNumber>(decimalBase);
    number %= threshold;
}

int main() {
    FibonacciPair<mpz_class> exact;
    FibonacciPair<size_t> tail;
    while (true) {
        if (isPanhead((tail.current)) && isPanhead(exact.current)) {
            std::cout << exact.index << std::endl;
            break;
        }
        tail.advance();
        exact.advance();
        truncate(tail.current);
    }
}
