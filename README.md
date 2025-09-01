# Pixel Manipulation Project

## Overview
The Pixel Manipulation Project is a Python-based application designed for manipulating image pixels. This project includes functionalities for encrypting and decrypting images by altering pixel values. It serves as a practical example of image processing techniques using Python.

## Installation
To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd pixel-manipulation-project
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To use the pixel manipulation functionalities, you can run the main script in the `src` directory. Here are some examples of how to manipulate images:

1. **Encrypting an Image**:
   ```python
   from src.pixel_manipulation import manipulate_image

   input_image_path = 'path/to/input_image.png'
   output_image_path = 'path/to/encrypted_image.png'
   key = 42  # Example key

   manipulate_image(input_image_path, output_image_path, key)
   ```

2. **Decrypting an Image**:
   ```python
   from src.pixel_manipulation import decrypt_image

   input_image_path = 'path/to/encrypted_image.png'
   output_image_path = 'path/to/decrypted_image.png'
   key = 42  # Example key

   decrypt_image(input_image_path, output_image_path, key)
   ```

## Testing
Unit tests for the pixel manipulation functions are located in the `tests` directory. To run the tests, use the following command:
```
pytest tests/test_pixel_manipulation.py
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.