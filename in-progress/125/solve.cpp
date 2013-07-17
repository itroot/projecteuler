#include <iostream>
#include <array>
#include <algorithm>
#include <iterator>
#include <boost/lexical_cast.hpp>
/// @todo make enumerate class
#include <boost/iterator/counting_iterator.hpp>
/// @todo move to own power header
#include <boost/math/special_functions/pow.hpp>

/// @todo see http://wordaligned.org/articles/sums-and-sums-of-squares
/// @todo add common header with printContainer

namespace moveit {
template <typename Container>
std::ostream& print(std::ostream& ostream, const Container& container)
{
    std::ostream_iterator<typename Container::value_type> out(ostream , "\n");
    std::copy(container.begin(), container.end(), out);
    return ostream;
}
}

namespace {
    typedef size_t Number;
    const Number upperLimitSqrt = 10000;
    const Number upperLimit = upperLimitSqrt * upperLimitSqrt;
    typedef std::array<Number, upperLimitSqrt> NumberArray;
    typedef boost::counting_iterator<Number> Counting;
}

template <typename Iterator>
bool isPalindromic(Iterator begin, Iterator end)
{
    std::reverse_iterator<Iterator> rend(end);
    return std::equal(begin, begin+(end-begin)/2, rend);
}

template<class Iterator, class Handler>
void for_each_indexed(Iterator begin, Iterator end, Handler handler) {
    size_t index = 0;
    for (Iterator it = begin; it != end; ++it) {
        handler(*it, index);
        ++index;
    }
}

template<class Iterator, class Handler>
void for_each_iterator(Iterator begin, Iterator end, Handler handler) {
    for (Iterator it = begin; it != end; ++it) {
        handler(it);
    }
}

int main(int /*argc*/, char* /*argv*/[])
{
    NumberArray numberArray;
    std::copy(Counting(0), Counting(upperLimitSqrt), numberArray.begin());
    NumberArray squareArray;
    std::transform(numberArray.begin(), numberArray.end(), squareArray.begin(), boost::math::pow<2, Number  >);
    NumberArray squareSumArray;
    Number sum = 0;
    for_each_indexed(squareArray.begin(), squareArray.end(), [&](Number n, size_t i) {
        sum += n;
        squareSumArray[i] = sum;
    });
    Number result = 0;
    for_each_iterator(squareSumArray.begin(), squareSumArray.end(),
        [&](NumberArray::iterator it)
        {
            for_each_iterator(squareSumArray.begin(), it,
                [&](NumberArray::iterator jt)
                {
                    Number number = *it - *jt;
                    if (number >=  upperLimit) {
                        return;
                    }
                    std::string s = boost::lexical_cast<std::string>(number);
                    if (isPalindromic(s.begin(), s.end())) {
                        result += number;
                    }
                }
            );
        }
    );
    std::cout << result << std::endl;
}
