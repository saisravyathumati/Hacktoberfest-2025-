from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)
    return list(groups.values())

if __name__ == "__main__":
    words = input("Enter words separated by space: ").split()
    print(group_anagrams(words))
