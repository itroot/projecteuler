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

#include <set>

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
    //const Number upperLimitSqrt = 32;//10000;
    const Number upperLimitSqrt = 10000;
    //const Number upperLimit = 1000;//upperLimitSqrt * upperLimitSqrt;
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

template<class Iterator, class DataIterator, class Handler>
void distinct_collection_step(Iterator begin, Iterator end, DataIterator data_begin, DataIterator data_end, DataIterator current, Handler handler)
{
    if (current == data_end) {
        handler(data_begin, data_end);
        return;
    }
    if (begin == end) {
        return;
    }
    for_each_iterator(begin, end,
        [&](Iterator it)
        {
            *current = it;
            distinct_collection_step(it+1, end, data_begin, data_end, current+1, handler);
        }
    );
}

template<class Iterator, class Handler>
void for_distinct_collection(Iterator begin, Iterator end, size_t size, Handler handler)
{
    std::vector<Iterator> data;
    data.resize(size);
    distinct_collection_step(begin, end, data.begin(), data.end(), data.begin(), handler);
}

int main(int /*argc*/, char* /*argv*/[])
{
    NumberArray numberArray;
    std::copy(Counting(0), Counting(upperLimitSqrt), numberArray.begin());
    NumberArray squareArray;
    std::transform(numberArray.begin(), numberArray.end(), squareArray.begin(), boost::math::pow<2, Number>);
    NumberArray squareSumArray;
    Number sum = 0;
    for_each_indexed(squareArray.begin(), squareArray.end(), [&](Number n, size_t i) {
        sum += n;
        squareSumArray[i] = sum;
    });
    //Number result = 0;
    std::set<Number> resultSet;
    for_distinct_collection(squareSumArray.begin(), squareSumArray.end(), 2,
        [&](std::vector<NumberArray::iterator>::iterator begin, std::vector<NumberArray::iterator>::iterator end)
        {
            Number number = **(begin+1) - **begin;
            if (number >=  upperLimit) {
                return;
            }
            std::string s = boost::lexical_cast<std::string>(number);
            if (1 == (*(begin+1) - *begin)) {
                return;
            }
            if (isPalindromic(s.begin(), s.end())) {
                //std::cout << *begin - squareSumArray.begin() << " " << *(begin+1) - squareSumArray.begin() << std::endl;
                //std::cout << "@ " << number << std::endl;
                //std::cout << std::endl;
                resultSet.insert(number);
                //result += number;
            }
        }
    );
    std::cout << std::accumulate(resultSet.begin(), resultSet.end(), 0L) << std::endl;
}
