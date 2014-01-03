#include <vector>
#include <memory>
#include <iostream>
#include <fstream>
#include <algorithm>

struct Node {
    unsigned int number;
    Node* previous;
    std::vector<std::unique_ptr<Node> > nodes;
};

std::vector<Node*> get_ancestors(Node* node)
{
    Node * ancestor = node;
    std::vector<Node*> ancestors = {};
    while (nullptr != ancestor) {
        ancestors.push_back(ancestor);
        ancestor = ancestor->previous;
    }
    return ancestors;
}

int main() {
    size_t upper_limit = 200;
    std::vector<Node*> result_vec(upper_limit + 1, nullptr);
    std::unique_ptr<Node> start(new Node({1, nullptr, {}}));
    std::vector<Node*> level = {start.get()};
    std::vector<Node*> new_level;
    size_t iteration_number = 0;
    while (!std::all_of(result_vec.begin() + 2, result_vec.end(), [](Node* node){return node!=nullptr;})) {
        ++iteration_number;
        //std::cout << "Iteration: " << iteration_number << std::endl;
        for (Node* node : level) {
            std::vector<Node*> ancestors = get_ancestors(node);
            for (Node* ancestor: ancestors) {
                unsigned int new_number = node->number + ancestor->number;
                Node* new_node = new Node({new_number, node, {}});
                if (new_number < (upper_limit + 1)) {
                    if (nullptr == result_vec[new_number]) {
                        result_vec[new_number] = new_node;
                    }
                }
                node->nodes.push_back(std::unique_ptr<Node>(new_node));
                new_level.push_back(new_node);
            }
        }
        //std::cout << "new_level size: " << new_level.size() << std::endl;
        //std::cout << "new_level first_elem: " << new_level.front()->number << std::endl;
        /*
        for (size_t i = 0; i != upper_limit+1; ++i) {
            std::cout << i << ": " << result_vec[i] << ", ";
        }
        std::cout << std::endl;
        */
        level = new_level;
        new_level.clear();
    }
    unsigned int result = 0;
    std::ofstream out("result-c++.txt");
    for (Node* node : result_vec) {
        std::vector<Node*> ancestors = get_ancestors(node);
        for (size_t i = 0; i != ancestors.size(); ++i) {
            out << ancestors[i]->number;
            if (i != (ancestors.size() - 1)) {
                out << " ";
            }
        }
        out << std::endl;
        size_t size = ancestors.size();
        if (size > 0) {
            result += size - 1;
        }
    }
    std::cout << result << std::endl;
    //std::cout << std::accumulate(result_vec.begin(), result_vec.end(), 0) << std::endl;
}
