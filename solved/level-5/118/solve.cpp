#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>
#include <boost/lexical_cast.hpp>

bool unique_digits(const std::string& line)
{
    std::vector<bool> digits(9, false);
    for (char c: line) {
        if (c=='0' or digits[c-'1']) {
            return false;
        } else {
            digits[c-'1'] = true;
        }
    }
    return true;
}

struct CategoryItem {
    std::string digits;
    size_t number;
};

typedef std::vector<CategoryItem> CategoryVector;

size_t solve(const CategoryVector& cv, std::string digits, size_t index)
{
    if (9 == digits.size()) {
        return 1;
    }
    size_t result = 0;
    for (size_t i = index ; i != cv.size() ; ++i) {
        const CategoryItem& ci = cv[i];
        std::string new_line = digits + ci.digits;
        if (unique_digits(new_line)) {
            result += ci.number * solve(cv, new_line, i+1);
        }
    }
    return result;
}


int main() {
    std::ifstream in("../lib/data/primes-100000000.list");
    std::string line;
    std::vector<std::string> primes;
    std::map<std::string, size_t> categories;
    while (std::getline(in, line)) {
        if (!unique_digits(line)) {
            continue;
        }
        std::sort(line.begin(), line.end());
        categories[line] += 1;
        primes.push_back(line);
    }
    CategoryVector category_items;
    for (auto data: categories) {
        category_items.push_back({data.first, data.second});
    }
    std::cout << solve(category_items, "", 0) << std::endl;
}
