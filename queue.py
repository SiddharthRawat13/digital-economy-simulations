"""Simple order queue simulation for a fictional business."""
import heapq
import numpy as np
import matplotlib.pyplot as plt

SHIFTS = 100
SHIFT_MINUTES = 480


def make_orders(seed):
    random = np.random.default_rng(seed)
    arrivals = []
    services = []
    clock = 0
    while True:
        clock += random.exponential(3)  # About one order every 3 minutes
        if clock > SHIFT_MINUTES:
            break
        arrivals.append(clock)
        services.append(random.exponential(2.5))
    return arrivals, services


def average_wait(arrivals, services, workers):
    # Each value stores when a worker will be free again.
    free_times = [0.0] * workers
    heapq.heapify(free_times)
    waits = []
    for arrival, service in zip(arrivals, services):
        free_at = heapq.heappop(free_times)
        start = max(arrival, free_at)
        waits.append(start - arrival)
        heapq.heappush(free_times, start + service)
    return np.mean(waits)


waits_one = []
waits_two = []
for seed in range(1000, 1000 + SHIFTS):
    arrivals, services = make_orders(seed)
    waits_one.append(average_wait(arrivals, services, 1))
    waits_two.append(average_wait(arrivals, services, 2))

print('Average waiting time across 100 shifts')
print(f'One worker: {np.mean(waits_one):.2f} minutes')
print(f'Two workers: {np.mean(waits_two):.2f} minutes')

plt.bar(['One worker', 'Two workers'], [np.mean(waits_one), np.mean(waits_two)])
plt.ylabel('Average wait (minutes)')
plt.title('Order queue simulation')
plt.tight_layout()
plt.savefig('queue_chart.png', dpi=160)
print('Saved queue_chart.png')
