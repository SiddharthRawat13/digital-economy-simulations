"""Simple inventory simulation for a fictional business."""
import numpy as np
import matplotlib.pyplot as plt

DAYS = 100000
WASTE_COST = 2
SHORTAGE_COST = 6
BASELINE_STOCK = 130


def make_demand(seed, average=100):
    random = np.random.default_rng(seed)
    demand = random.normal(average, 20, DAYS)
    return np.maximum(0, np.rint(demand)).astype(int)


def check_stock(stock, demand):
    sold = np.minimum(stock, demand)
    waste = stock - sold
    shortage = demand - sold
    cost = WASTE_COST * waste + SHORTAGE_COST * shortage
    fill_rate = 100 * sold.sum() / demand.sum()
    return cost.mean(), waste.mean(), fill_rate


training = make_demand(42)
stock_options = range(80, 151)
costs = [check_stock(q, training)[0] for q in stock_options]
best_stock = stock_options[int(np.argmin(costs))]

print('Best stock quantity:', best_stock)
print('\nNormal demand (100 units on average)')
for q in [BASELINE_STOCK, best_stock]:
    cost, waste, fill = check_stock(q, make_demand(43))
    print(f'Stock {q}: cost={cost:.2f}, waste={waste:.2f}, fulfilled={fill:.2f}%')

print('\nHigher demand (120 units on average)')
for q in [BASELINE_STOCK, best_stock]:
    cost, waste, fill = check_stock(q, make_demand(44, 120))
    print(f'Stock {q}: cost={cost:.2f}, waste={waste:.2f}, fulfilled={fill:.2f}%')

plt.plot(list(stock_options), costs)
plt.axvline(best_stock, linestyle='--', label=f'Best: {best_stock} units')
plt.xlabel('Stock quantity')
plt.ylabel('Average daily penalty cost')
plt.title('Inventory simulation')
plt.legend()
plt.tight_layout()
plt.savefig('inventory_chart.png', dpi=160)
print('\nSaved inventory_chart.png')
