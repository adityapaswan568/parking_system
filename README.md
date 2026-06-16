# Parking Management System

Python + MySQL project for managing parking records and vehicle details.

---

## Requirements

| Requirement     | Version      |
|-----------------|--------------|
| Python          | 3.7+         |
| MySQL Server    | 5.7+ / 8.0   |
| mysql-connector | latest       |

---
### Clone this Repository
```bash
git clone https://github.com/adityapaswan568/parking_system.git
cd parking_system
```
## Setup Steps

### 1. Install Python dependency

```bash
pip install mysql-connector-python
```

### 2. Start MySQL and run setup script

```bash
mysql -u root -p < setup_db.sql
```

Or paste contents of `setup_db.sql` into MySQL Workbench / command line.

> Default credentials used: host=`localhost`, user=`root`, port=`3307`  
> Change in `parking.py` line 6–13 if yours differ.

### 3. Run the program

```bash
python parking.py
```

---

## Menu Options

| Option | Action                          |
|--------|---------------------------------|
| 1      | Add a parking slot record       |
| 2      | Search / view parking records   |
| 3      | Add vehicle detail              |
| 4      | Remove vehicle record           |
| 5      | View vehicle + parking (JOIN)   |
| 0      | Exit                            |

---

## Database Tables

### `parkmaster12`
| Column     | Type         | Description           |
|------------|--------------|-----------------------|
| pid        | INT (PK)     | Parking slot ID       |
| pnm        | VARCHAR(50)  | Parking slot name     |
| level      | VARCHAR(10)  | Floor / level         |
| freespace  | VARCHAR(3)   | YES or NO             |
| vehicleno  | VARCHAR(20)  | Vehicle plate number  |
| nod        | INT          | Number of days parked |
| payment    | DECIMAL      | Auto-calculated fee   |

### `vehicle`
| Column     | Type         | Description           |
|------------|--------------|-----------------------|
| vid        | INT (PK, AI) | Auto-increment ID     |
| pid        | INT (FK)     | Links to parkmaster12 |
| vnm        | VARCHAR(50)  | Vehicle model name    |
| dateofpur  | DATE         | Date of purchase      |

---

## Payment Calculation

```
Payment = Number of Days × ₹20
```

---

## File Structure

```
parking_system/
├── parking.py       ← main program
├── setup_db.sql     ← run this first in MySQL
└── README.md        ← this file
```
## 🧑‍💻 Author

### [**Aditya Paswan**](https://github.com/adityapaswan568)
