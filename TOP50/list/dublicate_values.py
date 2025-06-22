from collections import Counter

def find_duplicates(lst):
    counts = Counter(lst)
    duplicates = []
    for item, count in counts.items():
        if count > 1:
            duplicates.append(item)
    return duplicates

print(find_duplicates([1, 2, 3, 2, 4, 5, 1]))  # Output: [1, 2]# it return dublicate values