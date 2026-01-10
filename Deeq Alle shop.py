#DEEQ ALLE SHOP MANAGEMENT SYSTEM

import mysql.connector
from datetime import datetime

# =========================
# DATABASE CONNECTION
# =========================
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="!@#$%asd!1",
        database="orbitdb"
    )

# =========================
# ADD PRODUCT
# =========================
def add_product():
    name = input("Geli magaca alaabta: ")
    buy_price = float(input("Geli qiimaha lagu soo iibsaday Dollor ahaan $: "))
    sell_price = float(input("Geli qiimaha lagu iibinayo cash ahaan $: "))
    quantity = int(input("Geli tirada alaabta: "))

    conn = get_connection()
    cur = conn.cursor()

    query = """
    INSERT INTO products (name, buy_price, sell_price, quantity)
    VALUES (%s, %s, %s, %s)
    """
    cur.execute(query, (name, buy_price, sell_price, quantity))
    conn.commit()

    print("✅ Alaab waa lagu daray")

# =========================
# SELL PRODUCT
# =========================
def sell_product():
    product_id = int(input("Geli Product ID: "))
    qty = int(input("Geli tirada la iibinayo: "))

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT sell_price FROM products WHERE id = %s", (product_id,))
    price = cur.fetchone()

    if price is None:
        print("❌ Alaab lama helin")
        return

    sell_price = price[0]
    total = sell_price * qty

    cur.execute(
        "INSERT INTO sales (product_id, quantity, total_price) VALUES (%s, %s, %s)",
        (product_id, qty, total)
    )

    cur.execute(
        "UPDATE products SET quantity = quantity - %s WHERE id = %s",
        (qty, product_id)
    )

    conn.commit()
    print("✅ Iib waa la diiwaangeliyay")

# =========================
# PROFIT REPORT
# =========================
def report(period):
    conn = get_connection()
    cur = conn.cursor()

    query = f"""
    SELECT 
        SUM(s.total_price) AS income,
        SUM(p.buy_price * s.quantity) AS cost
    FROM sales s
    JOIN products p ON s.product_id = p.id
    WHERE s.sale_date >= DATE_SUB(NOW(), INTERVAL {period})
    """
    cur.execute(query)
    income, cost = cur.fetchone()

    if income is None:
        print("📊 Wax iib ah lama helin")
        return

    profit = income - cost

    print("\n📊 WARBIXIN – DEEQ ALLE SHOP")
    print("Dakhliga:", income)
    print("Kharashka:", cost)
    print("Faa’iido/Khasaaro:", profit)

# =========================
# MAIN MENU
# =========================
def main():
    while True:
        print("""
=============================
  DEEQ ALLE SHOP SYSTEM
=============================
1. Ku dar Alaabta
2. Iibi Alaabta
3. Warbixinta Todobaadka
4. Warbixinta Bilasha
5. Warbixinta Sanadka
0. Ka Bax
""")
        choice = input("Dooro mid ka mid ah: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            sell_product()
        elif choice == "3":
            report("7 DAY")
        elif choice == "4":
            report("1 MONTH")
        elif choice == "5":
            report("1 YEAR")
        elif choice == "0":
            print("👋 Mahadsanid – Deeq Alle Shop")
            break
        else:
            print("❌ Doorasho khaldan")

# =========================
# RUN SYSTEM
# =========================
main()
