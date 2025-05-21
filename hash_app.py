import os
import sys
import xxhash

def get_bucket_number(s, n):
    h = xxhash.xxh32(s).intdigest()
    return (h % n) + 1

def write_to_bucket(bucket_num, string):
    filename = f"{bucket_num}.txt"
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(string + '\n')

def main():
    if len(sys.argv) != 3:
        print("Usage: python hash_app.py <number_of_buckets> <bucket_size_limit>")
        sys.exit(1)

    n = int(sys.argv[1])
    s = int(sys.argv[2])

    print(f"hash_app {n} {s}")
    try:
        while True:
            user_input = input("Please enter the string: ")
            if user_input.strip() == "":
                continue  # Ignore empty inputs
            bucket_num = get_bucket_number(user_input, n)
            write_to_bucket(bucket_num, user_input)
            print(f"{user_input} added to {bucket_num}.txt")
    except KeyboardInterrupt:
        print("\nExiting application.")

if __name__ == "__main__":
    main()
