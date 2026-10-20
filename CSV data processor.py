
import csv
import os


def read_csv_file(filename):
    """Read employee or sales data from a CSV file."""
    records = []

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames:
                print("Error: CSV file is empty or has no header.")
                return records

            for row in reader:
                records.append(row)

    except FileNotFoundError:
        print("Error: CSV file not found.")
    except PermissionError:
        print("Error: Permission denied while reading the file.")
    except csv.Error as error:
        print("Error reading CSV file:", error)

    return records


def process_data(records):
    """Calculate statistics from numeric columns."""
    if not records:
        print("No records available to process.")
        return

    print("\n========== CSV SUMMARY REPORT ==========")
    print("Total records:", len(records))

    for column in records[0].keys():
        values = []

        for record in records:
            value = record.get(column, "")

            try:
                if value is not None and value.strip() != "":
                    values.append(float(value))
            except (ValueError, AttributeError):
                continue

        if values:
            total = sum(values)
            average = total / len(values)
            highest = max(values)

            print(f"\nColumn: {column}")
            print(f"Valid numeric values: {len(values)}")
            print(f"Total: {total:.2f}")
            print(f"Average: {average:.2f}")
            print(f"Highest value: {highest:.2f}")

    print("\n========================================")


def main():
    print("===== CSV DATA PROCESSOR =====")

    filename = input("Enter CSV file name (example: employees.csv): ").strip()

    if not filename:
        print("Error: Please enter a valid file name.")
        return

    records = read_csv_file(filename)

    if records:
        process_data(records)


if __name__ == "__main__":
    main()
