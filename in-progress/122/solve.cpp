#include <vector>
#include <memory>
#include <iostream>
#include <algorithm>

struct Node {
    unsigned int number;
    Node* previous;
    std::vector<std::unique_ptr<Node> > nodes;
};

int main() {
    size_t upper_limit = 200;
    std::vector<size_t> result_vec(upper_limit + 1, 0);
    std::unique_ptr<Node> start(new Node({1, nullptr, {}}));
    std::vector<Node*> level = {start.get()};
    std::vector<Node*> new_level;
    size_t iteration_number = 0;
    while (!std::all_of(result_vec.begin() + 2, result_vec.end(), [](size_t i){return i>0;})) {
        ++iteration_number;
        //std::cout << "Iteration: " << iteration_number << std::endl;
        for (Node* node : level) {
            Node * ancestor = node;
            std::vector<Node*> ancestors = {};
            while (nullptr != ancestor) {
                ancestors.push_back(ancestor);
                ancestor = ancestor->previous;
            }
            for (Node* ancestor: ancestors) {
                //std::cout << "Ancestor: " << ancestor->number << std::endl;
                unsigned int new_number = node->number + ancestor->number;
                //std::cout << new_number << " @";
                if (new_number < (upper_limit + 1)) {
                    if (result_vec[new_number] == 0) {
                        result_vec[new_number] = iteration_number;
                    }
                }
                Node* new_node = new Node({new_number, node, {}});
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
    std::cout << std::accumulate(result_vec.begin(), result_vec.end(), 0) << std::endl;
}
