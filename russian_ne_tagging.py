
import polyglot
from polyglot.text import Text, Word

# Language detection
text = 'Tere, tere, vanakere. Siin räägib härra Putin. Ma ei tea mida tulevik toob. Äkki koliks Iirimaale.'

print(text.language.name)
