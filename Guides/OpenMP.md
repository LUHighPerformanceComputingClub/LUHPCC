# OpenMP

To run these examples in VSCode:
- ensure Visual Studio is installed
- open Developer Console
- navigate to the directory with the .cpp files
- `code .`

## Pure OpenMP Summing
```
#include <omp.h>
#include <iostream>
#include <vector>

#define N 1000000
#define NUM_THREADS 4

int main() {
    std::vector<int> arr(N);
    long long sum = 0;

    for (int i = 0; i < N; i++)
        arr[i] = i + 1;

    omp_set_num_threads(NUM_THREADS);

    #pragma omp parallel for reduction(+:sum)
    for (int i = 0; i < N; i++)
        sum += arr[i];

    std::cout << "Sum: " << sum << std::endl;
    return 0;
}
```

## OpenMP Factorial
```
#include <omp.h>
#include <iostream>
#include <vector>

#define N 10

long long factorial(int n) {
    if (n == 0 || n == 1) return 1;
    return n * factorial(n - 1);
}

int main() {
    std::vector<long long> results(N);

    omp_set_num_threads(4);

    #pragma omp parallel
    {
        #pragma omp single
        {
            for (int i = 1; i <= N; i++) {
                #pragma omp task shared(results) firstprivate(i)
                {
                    results[i - 1] = factorial(i);
                }
            }
        }
    }

    for (int i = 0; i < N; i++) {
        std::cout << "Factorial of " << (i + 1) << " is: " << results[i] << std::endl;
    }

    return 0;
}
```

## OpenMP + MPI Sum
```
#include <stdio.h>
#include <mpi.h>
#include <omp.h>

#define N 1000000
#define NUM_THREADS 4

int main(int argc, char** argv) {
    int rank, size;
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    omp_set_num_threads(NUM_THREADS);

    int chunk_size = N / size;
    int start = rank * chunk_size;
    int end = start + chunk_size;

    long long local_sum = 0;
    int arr[N];

    for (int i = start; i < end; i++)
        arr[i] = i + 1;

    #pragma omp parallel for reduction(+:local_sum)
    for (int i = start; i < end; i++)
        local_sum += arr[i];

    long long global_sum = 0;
    MPI_Reduce(&local_sum, &global_sum, 1, MPI_LONG_LONG, MPI_SUM, 0, MPI_COMM_WORLD);

    if (rank == 0)
        printf("Total Sum: %lld\n", global_sum);

    MPI_Finalize();
    return 0;
}
```