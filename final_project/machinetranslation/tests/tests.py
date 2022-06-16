from translator import english_to_french
from translator import french_to_english

e2f = 'Hello'
f2e = 'Bonjour'

if (len(e2f) & len(f2e) > 0):
    english_to_french(e2f)
    french_to_english(f2e)
else:
    print('input missing')