#include <fstream>
#include <iostream>
#include <string>
#include <functional>
#include <vector>
#include <numeric>
#include <boost/algorithm/string.hpp>
#include <boost/lexical_cast.hpp>

namespace {
    const std::string filename = "triangles.txt";
}

void onEachLine(std::ifstream& in, std::function<void(const std::string&)> handler)
{
    std::string line;
    while (std::getline(in, line)) {
        handler(line);
    }
}

struct Point {
    int x;
    int y;
};

int scalar_product(const Point& lhs, const Point& rhs) {
    return lhs.x*rhs.x+lhs.y+rhs.y;
}

class Triangle {
public:
    Triangle(const std::string& line) {
        std::vector<std::string> sequence;
        boost::split(sequence, line, boost::is_any_of(","));
        std::vector<int> result(sequence.size());
        std::transform(sequence.begin(), sequence.end(), result.begin(), boost::lexical_cast<int, std::string>);
        for (size_t i = 0; i != result.size()/2; ++i) {
            pointList[i].x = result[2*i];
            pointList[i].y = result[2*i+1];
        }
    }
    bool isContainsOrigin() const {
        std::vector<std::vector<int>> f = {{0, 1}, {1, 2}, {0, 2}};
        unsigned int obtuseAngleNumber = std::count_if(f.begin(), f.end(), [&](const std::vector<int>& v) {return scalar_product(pointList[v[0]], pointList[v[1]])<0;});
        return obtuseAngleNumber > 1;
    }
private:
    Point pointList[3];
};

void processLine(const std::string& line) {
    Triangle triangle(line);
    if (triangle.isContainsOrigin()) {
        std::cout << "Yes" << std::endl;
    }
}

int main() {
    std::cout << "Opening " << filename << " ..." << std::endl;
    std::ifstream in(filename.c_str());
    onEachLine(in, processLine);
}
