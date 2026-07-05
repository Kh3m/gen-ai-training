import sqlite3

conn = sqlite3.connect("staff.db")

cur = conn.cursor()

cur.execute("SELECT name, role, email, manager FROM staff")

rows = (cur.fetchall())

print(rows)

print("\n")
print("="*50)
print("\n")

context = "\n".join(f"{n} ({r}) in {d}, reports to {m}" for n, r, d, m in rows)

print(context)