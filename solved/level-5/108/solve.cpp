#include <iostream>
#include <vector>

// 1/x+1/y=1/n
// n*x + n*y = x*y
// n*(x+y) = x*y
// x = n*y/(n-y)

namespace uneffective {
std::vector<size_t> fractionize(size_t number)
{
    
}
}

size_t test(size_t n)
{
    size_t result = 0;
    for (size_t x = (n+1); x!=(2*n+1) ; ++x) {
        size_t y = n*x/(x-n);
        //std::cout << x << " " << y << " " << n << std::endl;
        bool match = ((n*(x+y)) == (x*y));
        //std::cout << n << " " << x << " " << y << " " << result << std::endl;
        if (match) {
            //std::cout << "   " << x << " " << y << std::endl;
            ++result;
        }
    }
    //std::cout << n << std::endl;
    return result;
}

int main(int argc, char* argv[])
{
    size_t max_so_far = 0;
    for (size_t n = 1; n!=1000000; ++n) {
        //std::cout << "-- " << n << std::endl;
        size_t number = test(n);
        if (number > max_so_far) {
            std::cout << n << " " << number << std::endl;
            max_so_far = number;
        }
        if (number>1000) {
            std::cout << n << std::endl;
            break;
        }
    }
}
