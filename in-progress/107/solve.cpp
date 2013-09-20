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
    const std::string filename = "test-network.txt";
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
        //std::cout << row[0] << std::endl;
        result.push_back(row);
    }
    return result;
}

struct Edge {
    size_t weight;
    std::array<size_t, 2> verticeArray;
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
            edge.verticeArray[0] = i;
            edge.verticeArray[1] = j;
            q.push(edge);
        }
    }
    //std::cout << q.size() << std::endl;
    size_t result = 0;
    typedef std::set<size_t> Set;
    typedef std::vector<Set> Vector;
    typedef Vector::iterator Iterator;
    Vector visited;
    while (!q.empty()) {
        Edge edge = q.top();
        q.pop();
        Iterator i1 = visited.end();
        Iterator i2 = visited.end();
        for (Iterator it=visited.begin() ; it!= visited.end(); ++it) {
            if (it->end() != it->find(edge.verticeArray[0])) {
                i1 = it;
            }
            if (it->end() != it->find(edge.verticeArray[1])) {
                i2 = it;
            }
        }
        std::cout << "Start: " << edge.weight << ", size: " << visited.size() << std::endl;
        for (Set& s: visited) {
            std::cout << "[";
            for (size_t i: s) {
                std::cout << i << ",";
            }
            std::cout << "],";
        }
        std::cout << " @ " << edge.verticeArray[0] << " " << edge.verticeArray[1] << std::endl;
        if (i1 == visited.end() && i2 == visited.end()) {
            std::cout << "No one: " << edge.weight << std::endl;
            Set s;
            s.insert(edge.verticeArray[0]);
            s.insert(edge.verticeArray[1]);
            visited.push_back(s);
        } else if (i1 == visited.end()) {
            std::cout << "1: " << edge.weight << std::endl;
            i2->insert(edge.verticeArray[0]);
            i2->insert(edge.verticeArray[1]);
        } else if (i2 == visited.end()) {
            std::cout << "2: " << edge.weight << std::endl;
            i1->insert(edge.verticeArray[0]);
            i1->insert(edge.verticeArray[1]);
        } else {
            if (i1==i2) {
                std::cout << visited.size() << std::endl;
                std::cout << "Fail: " << edge.weight << std::endl;
                continue;
            }
            i1->insert(i2->begin(), i2->end());
            visited.erase(i2);
        }
        /*
        if ((visited.end() != visited.find(edge.verticeArray[0])) && (visited.end() != visited.find(edge.verticeArray[1]))) {
            std::cout << "No: " << edge.weight << std::endl;
            continue;
        } else {
        */
           // visited.insert(edge.verticeArray[0]);
           // visited.insert(edge.verticeArray[1]);
            result += edge.weight;
            //std::cout << edge.weight << std::endl;
        //}
        std::cout << "Ok: " << edge.weight << std::endl;
    }
    std::cout << result << std::endl;
}
