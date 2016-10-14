#include <iostream>
#include <algorithm>

typedef std::vector<int> Digits;
const size_t DIGIT_NUMBER = 1;

size_t prev2start_index(size_t index) {
    if (index < 2) {
        return 0;
    } else {
        return index - 2;
    }
}

int prev2sum(const Digits& digits, size_t index) {
    size_t prev2start = prev2start_index(index);
    int result = 0;
    for (size_t i = prev2start; i != index; ++i) {
        result += digits[i];
    }
    return result;
}

void traverse(Digits& digits, size_t index, size_t& counter)
{
    //if (index > 0) {
    //    std::cout << index << " " << digits[index - 1] << std::endl;
    //}
    if (index == DIGIT_NUMBER) {
        if (digits.front() != 0) {
            ++counter;
        }
        return;
    }
    int p2s = prev2sum(digits, index);
    //std::cout << "p2s: " << p2s << std::endl;
    for (int next_digit = 0; next_digit < (10 - p2s); ++next_digit) {
        digits[index] = next_digit;
        traverse(digits, index + 1, counter);
    }
}

struct Record {
    int right_digit;
    int two_sum;
    size_t count;
};

int main(int argc, char* argv[]) {
    typedef std::vector<Record> Records;
    Records records;
    for (size_t i = 0; i != 10; ++i) {
        records.push_back({i, i, 1});
    }
    typedef std::vector<Records> Table;
    Table t;
    t.push_back(records);
    for (size_t step = 0; step != 3; ++step) {
        Records records;
        for (size_t i = 0 ; i != 10; ++i) {
            size_t count = 0;
            for (const Record& record : t.back()) {
                if record 
            }
        }
    }
    return 0;
    Digits digits;
    digits.assign(DIGIT_NUMBER, 0);
    size_t counter = 0;
    traverse(digits, 0, counter);
    std::cout << counter << std::endl;
}
