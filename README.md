# Hexdump Tool

A simple Python-based hexdump tool that reads binary data from a file (or generates dummy data) and outputs its hexadecimal representation and ASCII equivalents to a text file.

## Features

- Converts binary data into a human-readable hexadecimal and ASCII representation.
- Outputs the result into a text file.
- Supports both reading from a file and generating a dummy set of data (0 to 255 byte values).

## Requirements

This tool is written in Python 3.x and uses the `hexdump` library for basic formatting. To run the tool, you will need Python installed on your system.

You can install any necessary dependencies with the following command:

```bash
pip install hexdump
```

## Usage

1. **Run the script**:

    Run the `hexdump.py` script by executing it in your terminal.

    ```bash
    python hexdump.py
    ```

2. **Provide a file path**:

    When prompted, enter the path of the binary file you want to hexdump. For example:

    ```
    Enter the file path: my_binary_file.bin
    ```

3. **Optional dummy data**:

    If you want to generate a hexdump from a dummy dataset (byte values from 0 to 255), enter `0` when prompted for the file path:

    ```
    Enter the file path: 0
    ```

4. **Output**:

    The resulting hexdump will be saved to a file named `dump.txt` in the same directory as the script. The file will contain the hexadecimal values, offsets, and ASCII representation of the data.

## Example

For a file containing the following bytes:

```txt
48 65 6c 6c 6f 20 77 6f 72 6c 64
```

The output will look like this:

```txt
00000000  48 65 6c 6c 6f 20 77 6f  72 6c 64                  |Hello world|
```

## Code Explanation

- **custom_hexdump**: This function takes in a `data` (binary data) and an `output_file` name. It then formats the data in both hexadecimal and ASCII formats and writes the result to the specified output file.
- **to_printable_ascii**: This helper function converts byte values to their printable ASCII equivalents, or a period (`.`) for non-printable bytes.
- **Input handling**: The script prompts the user for a file path. If the user enters `0`, it generates a default dataset of bytes from `0x00` to `0xFF`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```