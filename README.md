# CS-2520 Point of Sale GUI App

A desktop Point-of-Sale (POS) application for **CS 2520 - Python for Programmers** at Cal Poly Pomona (Fall 2026).

The finished application is intended to let customers browse products, build a cart, complete a digital payment, and receive a receipt. It will also provide authenticated administrators with tools to manage inventory, products, discounts, and product availability.

## Current Project Status

The project currently contains the initial data and module structure, but the application logic is not implemented yet.

- [x] JSON inventory file created with 100 products.
- [x] Product records include prices, stock, categories, and tax rates.
- [x] Category-based tax policy defined.
- [x] Separate files created for authentication, cart handling, checkout, receipts, and data access.
- [x] References and design decisions documented.
- [ ] Replace the placeholder Tkinter demo with the POS interface.
- [ ] Implement JSON loading and saving.
- [ ] Implement cart operations.
- [ ] Implement checkout and payment authorization.
- [ ] Implement inventory updates after successful sales.
- [ ] Implement receipt generation and sales-history storage.
- [ ] Implement admin authentication and protected admin tools.
- [ ] Add automated tests for validation and edge cases.

## Planned Features

### Shopping and Checkout

- Browse products with names, prices, categories, tax rates, and stock.
- Add products to a cart.
- Change quantities or remove products.
- Calculate subtotal, tax, discounts, and grand total.
- Process a digital payment.
- Generate a receipt after a successful transaction.

### Inventory Tracking

- Reduce stock after a completed sale.
- Prevent adding unavailable products to a cart.
- Prevent purchases that exceed current stock.
- Save inventory changes to JSON so they persist after the application closes.
- Store completed sales separately from the current inventory.

### Administrator Tools

- Provide a separate admin login.
- Restock products or change stock counts.
- Add, edit, and remove products.
- Add, change, or remove discounts.
- Mark products as available or unavailable.

### Validation and Error Handling

The application should prevent:

- Checkout with an empty cart.
- Zero, negative, or non-whole-number quantities.
- Purchases above available stock.
- Purchases of unavailable products.
- Invalid or declined payments.
- Negative prices or stock values.
- Discounts outside the range of 0-100%.
- Application crashes caused by invalid user input.

## Data and Storage Design

The project uses JSON because the dataset is small, easy to inspect, and appropriate for this class project.

### Inventory

data.json stores the current product inventory. It currently contains 100 products with this structure:

~~~
{
    "product_id": 1,
    "product_name": "bananas",
    "price": 1.86,
    "stock": 37,
    "categories": ["food", "produce", "fruits"],
    "tax_rate": 0.0
}
~~~

### Tax Rates

Tax rates are assigned based on product categories. When a product has multiple categories, its tax rate should be the highest rate associated with any of those categories.

The current sample policy uses:

- Essential groceries: 0.00
- Taxable goods, drinks, snacks, household items, pet products, personal care, and sports products: 0.0825
- Alcohol: 0.10

These are sample rates for the project and are not intended to represent a universal legal tax policy.

### Administrators

admins.json stores administrator records. It currently contains placeholder credentials for the team.

Before committing or publishing the finished application, plaintext passwords must be replaced with salted password hashes. The visible test password 0000 must not be used in a finished version. Hiding admin buttons is only a user-interface feature; every admin operation must also verify that the admin is authenticated.

### Sales and Receipts

The sales/ folder is intended to store completed sales as JSON files. Receipt generation will be handled by receipts.py.

Customers do not need accounts for this project. A completed sale only needs to record transaction information such as:

- Receipt ID
- Date and time
- Items and quantities
- Subtotal
- Tax
- Discounts
- Total
- Payment status
- Non-sensitive payment information, such as payment method or last four digits

Full card numbers, CVV codes, and customer account balances must not be stored. Payment authorization will be simulated for the class project unless a real payment service is later added.

## Project Structure

~~~
CS-2520-Point-of-Sale-GUI-App/
├── main_gui.py          # Tkinter interface and application entry point
├── data.py              # JSON loading and saving
├── cart.py              # Cart operations
├── checkout.py          # Totals, validation, payment, and inventory updates
├── auth.py              # Administrator authentication
├── receipts.py          # Receipt creation and storage
├── data.json            # Current product inventory
├── admins.json          # Administrator credentials
├── sales/               # Completed sale records
├── References.md        # External references used by the team
├── choices.md           # Project design decisions
├── LICENSE              # MIT License
└── README.md            # Project documentation
~~~

The intended dependency direction is:

~~~
Tkinter interface -> application logic -> JSON storage
~~~

The GUI should call the processing modules instead of directly editing JSON files.

## Getting Started

### Prerequisites

- Python 3.10 or newer
- Tkinter, usually included with Python
  - macOS Homebrew Python: brew install python-tk
  - Ubuntu/Debian: sudo apt install python3-tk

Check that Tkinter is installed:

~~~
python3 -m tkinter
~~~

### Running the App

From the project directory:

~~~
python3 main_gui.py
~~~

The current file launches only the placeholder GUI. The complete POS workflow will be added as the modules are implemented.

## Known Critiques and Next Priorities

1. Implement and test the data-access layer before building the full GUI.
2. Implement cart and checkout validation independently from Tkinter.
3. Add an explicit available field and discount field to products when those features are implemented.
4. Replace plaintext administrator passwords with salted hashes.
5. Define a safe write strategy so interrupted JSON writes do not corrupt inventory.
6. Add tests for stock validation, tax calculation, payment approval, and receipt creation.
7. Correct minor documentation and naming issues, including the capitalization of References.md and spelling in the reference notes.

## Team
---------------------
|       Name        |
|-------------------|
| Adrian Portillo   |
| Sunhak Lov        |
| Brent Gabrial Jao |
| Parth Patel       |
---------------------
