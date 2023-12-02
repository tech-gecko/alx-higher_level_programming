#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    sorted_names = sorted(dir(hidden_4))
    filtered_names = [
        name for name in sorted_names
        if not name.startswith('__')
    ]
    for name in filtered_names:
        print(name)
