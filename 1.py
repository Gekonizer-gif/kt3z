# Задание 1
def get_books(filename):
    with open(filename, encoding='utf-8') as f:
        rows = f.read().split('\n')[1:]
        return [
            [
                p[0],
                p[1],
                p[2],
                int(p[3]),
                float(p[4])
            ]
            for p in (line.split('|') for line in rows)
            if len(p) == 5
        ]


print(get_books("books.csv"))


# Задание 2
def filtered_books(books, query):
    return [
        [
            b[0],
            b[1] + ", " + b[2],
            b[3],
            b[4]
        ]
        for b in books
        if query.lower() in b[1].lower()
    ]


print(filtered_books(get_books("books.csv"), "python"))


# Задание 3
def calculate_totals(books):
    return [
        (b[0], round(b[2] * b[3], 2))
        for b in books
    ]


print(calculate_totals(filtered_books(get_books("books.csv"), "python")))
