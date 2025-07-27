"""Project: 1

You had saved the items and their price details in a text file, 
which you purchased yesterday from a nearby super market.
You need to know:
1. How many items did you purchase?
2. How many items are free?
3. What is the total amount you had to pay?
4. What is the discount amount?
5. What is the final amount did you pay after the discount?
Help yourself by writing a python code to do this. Include necessary code to handle the possible exceptions.
Note:
Data is stored in a text file Purchase-1.txt.
Each line contains one item's details.
Item name and price is separated by a space.
You have to enter the file name during run time."""

#Code

def process_purchase_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        total_items = 0
        free_items = 0
        total_price = 0.0
        discount_amount = 0.0

        for line in lines:
            parts = line.strip().split()
            if not parts:
                continue
            if parts[0].lower() == "discount":
                try:
                    discount_amount += float(parts[1])
                except:
                    continue
                continue

            try:
                item_name = ' '.join(parts[:-1])
                price = float(parts[-1])
                total_items += 1

                if price == 0:
                    free_items += 1
                else:
                    total_price += price

            except ValueError:
                print(f" Skipping invalid line: {line.strip()}")

        final_amount = total_price - discount_amount
        if final_amount < 0:
            final_amount = 0.0

        print("\n🛒 Purchase Summary")
        print("--------------------------")
        print(f"Total items purchased : {total_items}")
        print(f"Free items            : {free_items}")
        print(f"Total price (before discount): ₹{total_price:.2f}")
        print(f"Discount amount              : ₹{discount_amount:.2f}")
        print(f"Final amount to be paid      : ₹{final_amount:.2f}")

    except FileNotFoundError:
        print(" File not found. Please check the file name.")
    except Exception as e:
        print(" An unexpected error occurred:", e)

# Run the program
filename = input("Enter the filename (e.g., Purchase-1.txt): ")
process_purchase_file(filename)
