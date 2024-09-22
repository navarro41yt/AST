from enum import Enum
import os
from typing import List
import xml.etree.ElementTree as ET

from googletrans import Translator

INPUT_FOLDER = 'input'

INPUT_FILE = os.path.join(INPUT_FOLDER, 'input.xml')
LANGUAGES_FILE = os.path.join(INPUT_FOLDER, 'languages.csv')

OUTPUT_FOLDER = 'output'

class LanguagesE(Enum):
    es = 'Spanish'
    ca = 'Catalan'
    gl = 'Galician'
    eu = 'Basque'
    
    en = 'English'
    pt = 'Portuguese'
    it = 'Italian'
    fr = 'French'
    de = 'German'
    
    ru = 'Russian'
    
    zh_CN = 'Chinese (Simplified)'
    zh_TW = 'Chinese (Traditional)'
    ja = 'Japanese'
    ko = 'Korean'
    
    @classmethod
    def get(cls, code: str) -> str:
        normalized_code = code.replace('-', '_')
        
        try:
            return cls[normalized_code].value
        except KeyError:
            return code


class StringTranslator:

    def __init__(self, input_file: str, languages_file: str, output_dir: str) -> None:
        self.input_file = input_file
        self.languages_file = languages_file
        self.output_dir = output_dir

        self.translator = Translator()
        self.langs = self._get_languages()
        self.root = self._get_root()

    def _get_languages(self) -> List[str]:
        with open(self.languages_file, 'r') as file:
            return file.read().split(',')

    def _get_root(self) -> ET.Element:
        with open(self.input_file, mode='r') as file:
            xml_data = file.read()

        return ET.fromstring(xml_data)

    def _create_output_files(self) -> None:
        for lang in self.langs:
            lang_file = os.path.join(OUTPUT_FOLDER, f'{lang}.xml')
            
            with open(lang_file, mode='w') as file:
                file.write('<resources>\n')

    def translate(self) -> None:
        self._create_output_files()

        for lang in self.langs:
            output_file = os.path.join(OUTPUT_FOLDER, f'{lang}.xml')
            
            with open(output_file, mode='a', encoding='utf-8') as file:
                for e in self.root.findall('string'):
                    tranlatable_attr = e.attrib.get('translatable')
                    if tranlatable_attr == 'false':
                        continue

                    try:
                        translation = self.translator.translate(
                            text=e.text, dest=lang, src='en').text.replace("'", "\\'")
                    except:
                        print(f'Unknown Language: {lang}')
                        break

                    tranlation_string = f'<string name="{e.attrib['name']}">{translation}</string>'
                    file.write(f'{tranlation_string}\n')
                file.write('</resources>')

            print(f'Translated "{LanguagesE.get(lang)}"')


if __name__ == '__main__':
    st = StringTranslator(INPUT_FILE, LANGUAGES_FILE, OUTPUT_FOLDER)
    st.translate()
