# A3 Hashing

## Option Implemented
Option A: Basic hash bucket system that hashes input strings into `n` bucket files, allowing collisions within each file.

## Hashing Algorithm / Library
This application uses the [xxhash](https://github.com/Cyan4973/xxHash) Python library, specifically the `xxh32` function, for fast and efficient hashing of strings.

## How to Run

### Prerequisites
- Python 3 installed on your system.  
- `xxhash` library installed via pip:

```bash
pip3 install xxhash
```

### Running the Application

1. Open a terminal or command prompt.  
2. Change directory to the folder containing `hash_app.py`.  
3. Run the application with the number of buckets (`n`) and bucket size limit (`s`) as arguments:

```bash
python3 hash_app.py <number_of_buckets> <bucket_size_limit>
```

Example:

```bash
python3 hash_app.py 5 20
```

4. Enter strings one by one as prompted:

```
Please enter the string: Hello
Hello added to 2.txt
Please enter the string: World
World added to 1.txt
```

5. To exit the application, press `Ctrl + C`.

---

## Notes
- The bucket size limit (`s`) is accepted as an input argument but **overflow bucket handling is not implemented** in this version.
- Strings are hashed and distributed into files named `1.txt` through `n.txt` based on their hash values.
- Multiple strings may be stored in the same bucket file (collisions allowed).

---

## Contact
For any questions or issues, please contact ahmadov.n@outlook.com
