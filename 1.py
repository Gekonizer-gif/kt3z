# Задание 1
def get_books(filename):
    with open(filename, encoding='utf-8') as f:
        data = f.read().splitlines()[1:]
        result = []
        for line in data:
            parts = line.split('|')
            result.append([
                parts[0],
                parts[1],
                parts[2],
                int(parts[3]),
                float(parts[4])
            ])
        return result


print(get_books("books.csv"))


# Задание 2
def filtered_books(books, query):
    result = []
    for b in books:
        if query.lower() in b[1].lower():
            result.append([
                b[0],
                f"{b[1]}, {b[2]}",
                b[3],
                b[4]
            ])
    return result


print(filtered_books(get_books("books.csv"), "python"))


# Задание 3
def calculate_totals(books):
    result = []
    for b in books:
        result.append((b[0], round(b[2] * b[3], 2)))
    return result


print(calculate_totals(filtered_books(get_books("books.csv"), "python")))
