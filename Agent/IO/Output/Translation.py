from translate import Translator

translator = Translator(to_lang="zh")

def translate_text(text):
    translation = translator.translate(text)
    return translation
