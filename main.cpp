#include <iostream>
#include <vector>
#include <iomanip>
#include <cctype>
#include <cstring>
#include <string>
#include <cmath>
// #include  <bits/stdc++.h>

// int main()
// {
//     std::cout << "Testing" << std::endl;
//     // (growth rate 'r') xn+1 = r * x (1-x)
//     long max {3787047968108841941};
//     unsigned long people_on_earth {max};

//     std::cout << people_on_earth << std::endl;
//     std::cout << "Short Size: " << sizeof(short) << std::endl;
//     std::cout << "Int Size: " << sizeof(int) << std::endl;

//     std::cout << std::endl;
//     return 0;
// }

// #include <iostream>

// Logistic map
double f(const double r, const double x)
{
    return (r * x * (1 - x));
}

double rand_unit()
{
    return (((double)rand()) / RAND_MAX);
}

int main()
{
    // std::cout << rand_unit() << std::endl;
    // std::cout << rand_unit() << std::endl;
    // std::cout << rand_unit() << std::endl;
    std::cout << f(2, 0.6) << std::endl;
    // const double r_min = 3.0;
    // const double r_max = 4.0;

    // const int num_intervals = 1;
    // const int max_iterations = 600;

    // srand(time(NULL));

    // double r = r_min;
    // double x_n;

    // for (int i = 0; i < num_intervals; ++i)
    // {

    //     r += (r_max - r_min) / num_intervals;
    //     x_n = f(r, rand_unit());

    //     for (int j = 0; j < max_iterations; ++j)
    //     {
    //         x_n = f(r, x_n);
    //         if (j >= 300)
    //             std::cout << std::fixed ;
    //             std::cout << r << ' ' << x_n << " ++ " << std::endl;
    //     }
    // }

    std::cout << std::endl;
    return 0;
}
