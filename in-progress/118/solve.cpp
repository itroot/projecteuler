#include <vector>
#include <iostream>
#include <cstddef>
#include <functional>
#include <fstream>

struct Rake {
    Rake(std::function<void()> f)
    :   f_(f)
    {}
    ~Rake()
    {
        f_();
    }
    std::function<void()> f_;
};

struct Primes {
    Primes()
    : square_limit_(1)
    , square_counter_(0)
    , square_value_(1)
    , current_(1)
    {}
    void grow(size_t limit) {
        while (current_ < limit) {
            Rake rake([&](){++current_;});
            ++square_counter_;
            if (square_counter_ == square_limit_) {
                square_counter_ = 0;
                square_limit_ += 2;
                square_value_ += square_limit_;
                continue;
            }
            bool is_prime = true;
            for (size_t prime: primes_) {
                if (prime > square_limit_/2) {
                    break;
                }
                size_t remainder = current_ % prime;
                if (0 == remainder) {
                    is_prime = false;
                    break;
                }
            }
            if (is_prime) {
                primes_.push_back(current_);
            }
        }
    }
    size_t square_limit_;
    size_t square_counter_;
    size_t square_value_;
    size_t current_;
    std::vector<size_t> primes_;
};

int main() {
    size_t limit = 100000000;
    //limit = 100;
    Primes primes;
    primes.grow(limit);
    std::ofstream out("primes-100000000.list");
    for (size_t prime: primes.primes_) {
        out << prime << std::endl;
    }
}

#if 0
struct Wave {
    Wave(size_t period)
    :   period_(period)
    ,   counter_(0)
    {
    }
    void increment() {
        counter_ = (counter_ + 1) % period_;
    }
    bool correlate() {
        return 0 == counter_;
    }
    size_t period_;
    size_t counter_;
};

int main() {
    std::vector<Wave> v;
    size_t current = 2;
    v.push_back(Wave(2));
    while (true) {
        ++current;
        bool new_wave = true;
        for (Wave& wave : v) {
            wave.increment();
            new_wave = new_wave && !wave.correlate();
        }
        if (new_wave) {
            v.push_back(current);
            std::cout << current << std::endl;
        }
    }
}
#endif
