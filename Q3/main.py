import threading
import time


def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def single_threading() -> int:
    """Runs jobs using single thread only. Returns time taken in nanoseconds."""
    args_list = [50, 100, 200]

    start = time.perf_counter_ns()
    for arg in args_list:
        factorial(arg)
    end = time.perf_counter_ns()

    total_time_taken = end - start
    return total_time_taken


def multi_threading() -> int:
    """Runs jobs using multithreading. Returns time taken in nanoseconds."""
    args_list = [50, 100, 200]

    threads = [threading.Thread(target=factorial, args=(n,)) for n in args_list]

    start = time.perf_counter_ns()
    for t in threads:
        t.start()

    for t in threads:
        t.join()
    end = time.perf_counter_ns()

    total_time_taken = end - start
    return total_time_taken


def main():
    rounds = 10

    multi_threading_total_time_taken = 0
    single_threading_total_time_taken = 0

    for i in range(rounds):
        multi_threading_total_time_taken += multi_threading()
        single_threading_total_time_taken += single_threading()

    print(
        f"""
Average from {rounds} rounds:
Multi-threading took: {multi_threading_total_time_taken / rounds}ns
Single-threading took: {single_threading_total_time_taken / rounds}ns
"""
    )


if __name__ == "__main__":
    main()
