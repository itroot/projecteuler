#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <boost/algorithm/string.hpp>
#include <boost/lexical_cast.hpp>
#include <queue>
#include <array>
#include <set>

namespace {
    const std::string filename = "network.txt";
}

typedef size_t Number;
typedef std::vector<Number> Row;
typedef std::vector<Row> Table;

size_t convertField(const std::string& field)
{
    if ("-" == field) {
        return 0;
    } else {
        return boost::lexical_cast<size_t>(field);
    }
}

Table loadTable(const std::string& filename)
{
    std::ifstream in(filename.c_str());
    Table result;
    std::string line;
    while (std::getline(in, line)) {
        std::vector<std::string> s;
        boost::split(s, line, boost::is_any_of(","));
        Row row(s.size());
        std::transform(s.begin(), s.end(), row.begin(), convertField);
        result.push_back(row);
    }
    return result;
}

struct Edge {
    size_t weight;
    size_t i;
    size_t j;
    bool operator<(const Edge& other) const {
        return weight > other.weight;
    }
};

int main(int argc, char* argv[])
{
    std::priority_queue<Edge> q;
    Table table = loadTable(filename);
    for (size_t i=0; i<table.size(); ++i) {
        for (size_t j=i+1; j<table.size(); ++j) {
            Edge edge;
            size_t weight = table[i][j];
            if (0 == weight) {
                continue;
            }
            edge.weight = weight;
            edge.i = i;
            edge.j = j;
            q.push(edge);
        }
    }
    size_t result = 0;
    size_t all = 0;
    typedef std::set<size_t> Set;
    typedef std::list<Set> List;
    typedef List::iterator Iterator;
    List visited;
    while (!q.empty()) {
        Edge edge = q.top();
        q.pop();
        all += edge.weight;
        Iterator i1 = visited.end();
        Iterator i2 = visited.end();
        for (Iterator it=visited.begin() ; it!= visited.end(); ++it) {
            if (it->end() != it->find(edge.i)) {
                i1 = it;
            }
            if (it->end() != it->find(edge.j)) {
                i2 = it;
            }
        }
        if (i1 == visited.end() && i2 == visited.end()) {
            Set s;
            s.insert(edge.i);
            s.insert(edge.j);
            visited.push_back(s);
        } else if (i1 == visited.end()) {
            i2->insert(edge.i);
            i2->insert(edge.j);
        } else if (i2 == visited.end()) {
            i1->insert(edge.i);
            i1->insert(edge.j);
        } else {
            if (i1==i2) {
                continue;
            }
            i1->insert(i2->begin(), i2->end());
            visited.erase(i2);
        }
        result += edge.weight;
    }
    std::cout << all - result << std::endl;
}
