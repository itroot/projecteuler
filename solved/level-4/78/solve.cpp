#include <vector>
#include <iostream>

int main()
{
    typedef std::vector<unsigned int> Row;
    typedef std::vector<Row> Table;
    const unsigned int upperLimit=101010;
    Table table;
    table.push_back(Row());
    table[0].push_back(1);
    table.reserve(upperLimit);
    for (unsigned int n=1; n!=upperLimit; ++n) {
        Row row;
        row.push_back(0);
        table.push_back(row);
        table.back().reserve(n);
        for (unsigned int k=1; k<=n; ++k) {
            unsigned int result=table[n][k-1];
            if (n-k<k) {
                result+=table[n-k][n-k];
            } else {
                result+=table[n-k][k];
            }
            table[n].push_back(result%1000000);
        }
    unsigned int number=table[n][n];
    std::cout << n << " " << number << std::endl;
    if (0==number%1000000) {
        break;
    }
    }
}
