#include <iostream>

/**
 * How's approximation works
 * you have list of variables (x_i, y_i), you get a polynome as
 * sum for each j and i !=j : ((x-x_i) .. xj/(x_i - xj)) * yi ...  == 0, 
 * to make coefs integer, we can multiply.
 * see : http://en.wikipedia.org/wiki/Polynomial_interpolation
 * 
 * I think is will be easear to do in python
 */

int main(int argc, char* argv[])
{
    std::cout << "test" << std::endl;
}
