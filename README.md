# Document Database Sandbox

## Program Description

This demo program creates a TinyDB document database as a single file in the root directory.

## How to Run the Program

1. Click the green "Code" button.
1. Click the "Codespaces" tab.
1. Click the green "Create codspace on main" button.
1. When you see the README file show in a tab, the codespace is ready. This may take several minutes.
1. Open the python file and run through the debugger menu on the left hand toolbar.

## Possible Improvements (What We'll Do)

- Update the document - add role for Bobby
  - `users.update({'roles': ['Food Taster', 'Jester', 'Juggler']}, User.name == 'Bobby Beebop')`
  - Check the `db.json` file; what changed?
- Query with a condition - find all users who have a specific role
  - `results = users.search(User.roles.any(['Head Cook']))`
  - How would we accomplish the same thing using SQL?
- Add another table
  - ```
    inventory = db.table("inventory")
    inventory.insert({'item': 'Flour', 'qty': 50, 'unit': 'lbs'})
    inventory.insert({'item': 'Olive Oil', 'qty': 12, 'unit': 'bottles', 'organic': True})
    ```
  - Based on the current inventory schema, is our data structured or semi-structured? Do the fields match?
