

# Sales Rules
- Keep a tax rate tied to each product
- Digital payments only (no cash)


# Receipt Contents
- Date
- Total Price
- Separate total price with and without tax
- Individual Items Breakdown (Each product count and total for item)
- POS has admin access point with a pin for each admin

# Method for Storing Inventory
- SQLITE 
    - Top choice
    - Small learning curve
    - Integrated into python
    - Made for storing data and read/writes
- JSON 
    - Simple and easy to understand
    - Requires constantly reading and writing to a file 
    - Would require accessing external storage
- CSV 
    - Also easy to read 
    - Difficult to be writing and reading from external file
    - Has some awkward interactions 
