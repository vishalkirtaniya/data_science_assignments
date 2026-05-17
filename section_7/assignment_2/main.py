import numpy as np

np.random.seed(42)

# Shape: (5 warehouses, 7 days, 4 metrics)
# Metrics: [shipments_sent, shipments_received, damaged_goods, processing_time_hrs]
warehouse_data = np.random.randint(low=[50, 40, 0, 2],
                                    high=[200, 180, 20, 12],
                                    size=(5, 7, 4))

# This gives you a 3D array of shape (5, 7, 4).

# Part A:
# 1: Print the entire data for Warehouse 3 (index 2)
warehouse_3 = warehouse_data[2, :, :]
print(warehouse_3)
print(f"shape: {warehouse_3.shape}" )
print("---------------------------------------")

# 2: Extract Day 1's data across all warehouses (all warehouses, first day, all metrics)
day_1_all_warehouses = warehouse_data[:, 0, :]
print(day_1_all_warehouses)
print(f"shape: {day_1_all_warehouses.shape}")
print("---------------------------------------")

# 3: Extract the processing time (metric index 3) for all warehouses across all days — print its shape
processing_time_all_warehouses = warehouse_data[:, :, 3]
print(processing_time_all_warehouses)
print(f"shape : {processing_time_all_warehouses.shape}")
print("---------------------------------------")

# 4: Get the damaged goods count (metric index 2) for warehouse 1 on Day 5
damaged_goods = warehouse_data[0, 4, 2]
print(f"damaged goods: {damaged_goods}")
print("---------------------------------------")

# Part B — Axis-Based Aggregations
# Answer the following business questions using NumPy functions. No loops.
# 1: Total shipments sent (metric 0) per warehouse across all 7 days → shape should be (5,)
total_shipments = np.sum(warehouse_data[:, :, 0], axis=1)
print(total_shipments)
print(f"shape: {total_shipments.shape}")
print("---------------------------------------")

# 2: Average damaged goods (metric 2) per day across all warehouses → shape should be (7,)
avg_damaged_goods = np.mean(warehouse_data[:, :, 2], axis=0)
print(avg_damaged_goods)
print(f"shape: {avg_damaged_goods.shape}")
print("---------------------------------------")

# 4: Which warehouse had the highest total shipments sent? Use np.argmax()
highest_shipment_sent = np.sum(warehouse_data[:, :, 0], axis=1)
highest_warehouse = np.argmax(highest_shipment_sent)
print(f"warehouse with highest total shipments sent: {highest_warehouse}")
print("---------------------------------------")

# 5: Which day had the lowest average damaged goods? Use np.argmin()
lowest_damaged_goods = np.mean(warehouse_data[:, :, 2], axis=0)
warehouse = np.argmin(lowest_damaged_goods)
print(f"warehouse with lowest avg damaged goods: {warehouse + 1}")
print("---------------------------------------")

# Part C — Broadcasting in Action
# You've been told that each warehouse has a reporting overhead (fixed hours to add to processing time):
overhead = np.array([1, 2, 1, 3, 2])  # one value per warehouse, shape (5,)
# 1: Add this overhead to the processing time column for all days — using broadcasting, no loops. The overhead for each warehouse should apply to all 7 days.
reshaped_overhead = overhead.reshape(5,1)
added_overheads = warehouse_data[:, :, 3] + reshaped_overhead

# 2: Print the updated processing times and verify the shape is still (5, 7)
print(added_overheads)
print(added_overheads.shape)
print("---------------------------------------")

# 3: Now normalize the shipments sent column (metric 0) across all warehouses and days:

## Subtract the column mean
## Divide by the column standard deviation
## Print the normalized values and verify the mean is approximately 0 and std is approximately 1
shipment_sent = warehouse_data[:, :, 0]
mean = np.mean(shipment_sent)
std = np.std(shipment_sent)
normalization = (shipment_sent - mean) / std

print(f"normalization: \n{normalization}")
print(f"mean: {mean}")
print(f"std: {std}")
print("---------------------------------------")

# Part D — Statistical Deep Dive
# Using the full warehouse_data array:
# 1: Compute the median shipments received (metric 1) per warehouse
shipment_recieved = warehouse_data[:, :, 1]
median = np.median(shipment_recieved, axis=1)
print(f"median: {median}")
print("---------------------------------------")

# 2: Compute the 95th percentile of damaged goods (metric 2) across the entire dataset
damaged_goods = warehouse_data[:, :, 2]
percentile = np.percentile(damaged_goods, 95)
print(f"percentile: {percentile}")
print("---------------------------------------")

# 3: Compute the cumulative shipments sent (metric 0) for Warehouse 1 across 7 days — what does this tell you?
shipment_sentby_warehouse1 = warehouse_data[1, :, 0]
cum = np.cumsum(shipment_sentby_warehouse1)
print(shipment_sentby_warehouse1)
print(cum)
print("---------------------------------------")


# 4: Compute the correlation between total shipments sent and total shipments received across the 5 warehouses (collapse the days axis first using np.sum)
total_shipments_sent = np.sum(warehouse_data[:, :, 0], axis=1)
total_shipments_received = np.sum(warehouse_data[:, :, 1], axis=1)
correlation = np.corrcoef(total_shipments_sent, total_shipments_received)
print(f"correlation matrix: \n{correlation}")
print("---------------------------------------")


# 5: Find all unique values of damaged goods across the entire dataset and print how many unique values exist
unique_values = np.unique(warehouse_data[:, :, 2])
print(np.size(unique_values))
print("---------------------------------------")


# Part E — Putting It Together: Daily Report
# Write a function daily_report(data, day_index) that takes the full 3D array and a day index, and prints:

def daily_report(data, day_index):
    total_ship_sent = np.sum(data[:, day_index, 0])
    avg_ship_received = np.mean(data[:, day_index, 1])
    warehouse_with_most_damaged_goods = np.argmax(data[:, day_index, 2]) + 1
    avg_processing_time = np.mean(data[:, day_index, 3])
    print(f"------ Daily Report: Day {day_index + 1} ------")
    print(f"total shipment sent: {total_ship_sent}")
    print(f"average shipment recieved: {avg_ship_received}")
    print(f"warehouse with most damaged goods: {warehouse_with_most_damaged_goods}")
    print(f"Average processing time today: {avg_processing_time} hrs")

daily_report(warehouse_data, 2)