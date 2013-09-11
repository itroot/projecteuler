#include <iostream>
#include <vector>
#include <algorithm>

size_t upperLimit = 100001;
size_t index = 10000;

struct Rad {
    Rad(size_t n)
    : number(n)
    , rad(1)
    {
    }
    size_t number;
    size_t rad;
};

int main(int /*argc*/, char* /*argv*/[])
{
    std::vector<Rad> v;
    v.reserve(upperLimit);
    for (size_t i=0; i!=upperLimit; ++i) {
        v.push_back(Rad(i+1));
    }
    //std::cout << v.size() << std::endl;
    for (size_t i=1; i!=upperLimit; ++i) {
        if (1 == v[i].rad) {
            size_t number = i + 1;
            size_t start = number;
            while (start <= upperLimit) {
                v[start-1].rad *= number;
                start += number;
            }
        }
    }
    std::sort(v.begin(), v.end(), [](const Rad& lhs, const Rad& rhs) {return lhs.rad < rhs.rad;});
    /*
    for (const auto& e : v) {
        std::cout << e.number << std::endl;
    }
    */
    std::cout << v[index-1].number << std::endl;
    return EXIT_SUCCESS;
}
