from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = None
    original_text = ""
    source_language_name = ""
    target_language_name = ""
    
    if request.method == 'POST':
        # Get form data
        text_to_translate = request.form.get('text_to_translate', '')
        source_lang = request.form.get('source_lang', 'en')
        target_lang = request.form.get('target_lang', 'es')
        
        original_text = text_to_translate
        source_language_name = LANGUAGES.get(source_lang, '')
        target_language_name = LANGUAGES.get(target_lang, '')
        
        # Translate text
        if text_to_translate:
            try:
                translator = Translator()
                result = translator.translate(text_to_translate, src=source_lang, dest=target_lang)
                translation = result.text
            except Exception as e:
                translation = f"Error: {str(e)}"
    
    return render_template('index.html', 
                          languages=LANGUAGES, 
                          translation=translation,
                          original_text=original_text,
                          source_language_name=source_language_name,
                          target_language_name=target_language_name)

if __name__ == "__main__":
    app.run(debug=True)
