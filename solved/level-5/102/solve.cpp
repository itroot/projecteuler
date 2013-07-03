#include <fstream>
#include <iostream>
#include <string>
#include <functional>
#include <vector>
#include <numeric>
#include <array>
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

struct Vector {
    Vector(const Point& point)
    : x(point.x)
    , y(point.y)
    {}
    Vector(const Point& start, const Point& end)
    : x(end.x - start.x)
    , y(end.y - start.y)
    {}
    int x;
    int y;
};

int square(const Vector& lhs, const Vector& rhs) {
    return abs(lhs.x * rhs.y - lhs.y * rhs.x);
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
        int triangleDoubleSquare = square(edge(0, 1), edge(1, 2));
        int sumOfSquares = pieSquare(0, 1) + pieSquare(1, 2) + pieSquare(0, 2);
        return sumOfSquares == triangleDoubleSquare;
    }
private:
    Vector edge(size_t start, size_t end) const {
        return Vector(pointList[start], pointList[end]);
    }
    int pieSquare(size_t lhs, size_t rhs) const {
        return square(pointList[lhs], pointList[rhs]);
    }
private:
    std::array<Point, 3> pointList;
};

struct Solution {
    Solution()
    : result(0)
    {}
    void processLine(const std::string& line) {
        Triangle triangle(line);
        if (triangle.isContainsOrigin()) {
            ++result;
        }
    }
    size_t result;
};

int main() {
    Solution solution;
    std::ifstream in(filename.c_str());
    onEachLine(in, std::bind(&Solution::processLine, &solution,  std::placeholders::_1));
    std::cout << solution.result << std::endl;
}
