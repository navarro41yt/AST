# Android Strings Translator

This project provides an automated solution for translating Android Studio strings.xml files into multiple languages.

## Environment Setup

1. **Clone the Repository:**
   - Clone this repository to your local machine using `git clone https://github.com/navarro41yt/AST.git`.

2. **Install Dependencies:**
   - Create a virtual environment using `python -m venv venv` or install dependencies globally using `pip install -r requirements.txt`.
   - Activate the virtual environment using `source venv/bin/activate` on Linux or `venv\Scripts\activate` on Windows.
   - Install the required libraries using `pip install -r requirements.txt`.

## Usage

1. **Prepare Input:**
   - Place your `strings.xml` content in the [./input/input.xml](./input/input.xml) file.

2. **Define Languages:**
   - Edit [./input/languages.csv](./input/languages.csv) to specify the languages you want to translate to. Separate each language code with commas
   - List of Possible values defined by the [ISO 639 (Set 1)](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) (Some languages like chinese have multiple values, like zh-CN, zh-TW, etc.)

3. **Run the Translation Script:**
   - Execute the `translate.py` script.

4. **View Translations:**
   - Translated files will be generated in the `./output/` folder, with each translation in a separate file.


## Requirements
- Python 3.x
- Libraries: 
  - Libraries used in this project are listed in the [requirements.txt](requirements.txt) file.

## Contributing
Feel free to contribute by opening issues or submitting pull requests.

## License
This project is licensed under the [MIT License](LICENSE).
