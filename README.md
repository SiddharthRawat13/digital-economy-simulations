# Digital Economy – Python Simulations

These are two small experiments for my Digital Economy & Transformation assignment.
They use **made-up business data**, not actual data from UPS or Siemens.

## 1. Inventory simulation (`inventory.py`)

A shop sells an item that cannot be kept for the next day. I used 100,000 simulated days to compare stock levels from 80 to 150 units.

- Average daily demand: 100 units
- Standard deviation: 20 units
- Cost for each unsold unit: 2 (illustrative units)
- Cost for each customer order not fulfilled: 6 (illustrative units)
- Random seeds: 42 for finding a stock level, 43 for checking it, and 44 for testing higher demand

**Results** (rounded to two decimal places):

| Stock | Average cost | Average wasted units | Demand fulfilled |
|---|---:|---:|---:|
| 130 (starting policy) | 64.68 | 30.62 | 99.43% |
| 113 (best in training sample) | 50.69 | 16.12 | 96.92% |

When average demand goes up to 120, the average costs are **51.91** (stock 130) and **81.78** (stock 113).

This shows that less wasted stock does not always mean better customer service, and that a plan needs to be tested again if demand changes.

## 2. Order queue simulation (`queue.py`)

Orders arrive randomly during an eight-hour shift. Each worker completes one order at a time and processes orders in arrival order. Arrivals average one every 3 minutes, and service times average 2.5 minutes. We simulate 100 shifts, using random seeds 1000 to 1099, and compare using one or two workers. All orders are completed, even if processing continues beyond the shift.

This simpler worker-availability model gives:

| Workers | Average waiting time |
|---|---:|
| 1 | 10.91 minutes |
| 2 | 0.53 minutes |

These are different from earlier figures in the essay (10.33 and 0.51) because the random-number generation and implementation differ. **The essay should be corrected if these scripts are submitted as its evidence.**

## Run it yourself

You need Python 3 and the two packages below. In a terminal, run:

```bash
pip install -r requirements.txt
python inventory.py
python queue.py
```

The scripts print the numerical results and save `inventory_chart.png` and `queue_chart.png` in the current folder. You can change values such as `DAYS`, `BASELINE_STOCK`, or `SHIFTS` in the files and run them again.

## What this does not show

The experiments do **not** use real sales or staffing records. They do not measure emissions, real labour costs, or prove that a company is environmentally sustainable. They only show how small digital simulations can help businesses compare possible decisions.
