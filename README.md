# Minute-Burger-Bun-Expiration-Monitoring-System
A simple console-based inventory management system written in Python for monitoring burger bun quantities and expiration dates. It supports Staff and Manager roles with login authentication, bun inventory management, expiration status monitoring, stock updates, and product removal.

# Features 
Login Menu
- Staff – Login required.
- Manager – Login required.
- Exit – Closes the program.

# Default Login Accounts
| Role | Email | Password |
|---|---|---|
| Staff | `staff@gmail.com` | `staff123` |
| Manager | `manager@gmail.com` | `manager123` |

# Staff Menu 
1. Add Bun
2. View Bun Inventory
- View all inventory.
- View expired buns.
- View buns that are expiring soon.
- View safe buns.
3. Log Out

# Manager Menu 
1. Add Bun
2. View Bun Inventory
3. Manage Inventory
- Edit inventory quantities.
- Change expiration dates.
- Take buns out of stock.
- Remove bun records.
4. Log Out

# Available Bun Types
- Soft Burger Bun
- Brioche Bun
- Oatmeal-Sprinkled Brioche Bun
- Brioche Hotdog Bun
- Signature Hotdog Bun
- New Bun (allows users to enter a custom bun name)

# Key Behaviors 
- **Expiration Date Validation:** Accepts dates in MM/DD/YYYY format and rejects invalid dates or dates that have already passed.
- **Expiration Status:** Labels buns as Expired, Expiring Soon (seven days or fewer remaining), or Safe (more than seven days remaining).
- **Automatic Status Updates:** Recalculates expiration status when inventory is viewed.
- **Inventory Filtering:** Allows users to view all buns or filter them by expiration status.
- **Stock Management:** Managers can change quantities, take buns out of stock, and remove products.
- **Combining Records:** Adds new quantities to an existing record when the bun type and expiration date match.
- **Custom Bun Types:** Allows users to add new bun names for future use.
- **Input Validation:** Prevents negative quantities, invalid menu choices, and quantities exceeding available stock when taking buns out.
- **Back Option:** Users can type BACK to return to the previous menu in supported input prompts.

# Project Structure
The program uses Python lists and dictionaries to manage inventory information:
- users — Stores login credentials and roles.
- bun_types — Stores available bun types.
- products — Stores bun names, quantities, expiration dates, days remaining, and expiration statuses.
The datetime module is used to validate dates and calculate expiration status.

# Limitation
- **Console-Based:** The system uses a text-based interface rather than a graphical user interface.
- **Temporary Storage:** Inventory records are stored in memory and reset when the program closes.
- **No Database or File Saving:** Inventory data is not saved between sessions.
- **Single-Computer Use:** The program does not provide online access or simultaneous use across multiple devices.
- **Manual Monitoring:** Staff must open the program and view the inventory to check expiration status; automatic notifications are not included.

# Notes
- Staff can add buns and view inventory.
- Managers have additional inventory management permissions.
- The system allows the Expired status to be displayed, but the date-entry function rejects expiration dates that have already passed.

# Author
Created as a student project for the Introduction to Computing course under the Bachelor of Science in Information Technology program. Feel free to improve it (add file saving, better UI, etc.).
