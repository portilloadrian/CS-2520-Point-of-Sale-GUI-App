# CS-2520 Point of Sale GUI App

A desktop Point of Sale (POS) application built with Python and Tkinter for **CS 2520 – Python for Programmers** (Cal Poly Pomona, Fall 2026).

A tkinter GUI app that serves as a point of sale system that allows users to buy products with a user-friendly UI. App should also keep track of stock within system and allow "administrators" to change stock, add/remove discounts to products, and availability of items within system. Additionally, app should cover edge cases to prevent invalid transactions. 

---

## Features

### Shopping and Checkout
- [ ] Browse available products with name, price, current discount, and stock
- [ ] Add items to a cart, change quantities, and remove items
- [ ] Running subtotal, discounts applied, tax, and grand total
- [ ] Checkout that completes the purchase and shows a receipt

### Inventory Tracking
- [ ] Stock goes down automatically after each completed sale
- [ ] Items that are out of stock can't be added to the cart
- [ ] Inventory is saved so it is still there after the app closes

### Administrator Tools
- [ ] Separate admin mode (e.g. protected by a login or PIN)
- [ ] Restock items or change stock counts
- [ ] Add, change, or remove discounts on products
- [ ] Mark products as available or unavailable
- [ ] Add new products or remove old ones

### Edge-Case Handling (Invalid Transaction Prevention)
- [ ] Block purchases with an empty cart
- [ ] Block quantities that are zero, negative, or not whole numbers
- [ ] Block buying more than the stock on hand
- [ ] Block unavailable items from being sold
- [ ] Block payments that are less than the total, or not valid numbers
- [ ] Reject invalid admin input (negative stock, negative prices, discounts outside 0–100%)
- [ ] Show clear error messages instead of crashing


## Tech Stack

| Component | Tool                          |
|-----------|-------------------------------|
| Language  | Python 3.10+                  |
| GUI       | Tkinter / `ttk` (standard library) |
| Storage   | CSV/ JSON/ SQLite|

## Getting Started

### Prerequisites

- Python **3.10 or newer**
- Tkinter (bundled with most Python installers)
  - **macOS (Homebrew Python):** `brew install python-tk`
  - **Ubuntu/Debian:** `sudo apt install python3-tk`

Check that Tkinter is installed:

```bash
python3 -m tkinter
```

A small test window should appear.

### Installation

```bash
git clone https://github.com/portilloadrian/CS-2520-Point-of-Sale-GUI-App.git
cd CS-2520-Point-of-Sale-GUI-App
```

### Running the App

```bash
python3 main.py
```

## Project Structure

```
CS-2520-Point-of-Sale-GUI-App/
├── main.py        # Entry point; creates the main Tkinter window
├── LICENSE        # MIT License
└── README.md      # This file
```

## Team

| Name |
|------|
| Adrian Portillo |
| Sunhak Lov | 
| Brent Gabrial Jao |
| Parth Patel |

