# IMPORTAÇÃO DAS BIBLIOTECAS

import nltk
import string

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag

# DOWNLOAD DE RECURSOS

nltk.download('punkt')
nltk.download('punkt_tab')

nltk.download('stopwords')

nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

nltk.download('wordnet')

# INPUT - INSERIR TEXTO PARA PROCESSAMENTO 

texto = input("Digite um texto para processamento NLP:\n")

# SEGMENTAÇÃO EM SENTENÇAS

sentencas = sent_tokenize(texto)

print("SEGMENTAÇÃO EM SENTENÇAS")

for i, sentenca in enumerate(sentencas, start=1):
    print(f"Sentença {i}: {sentenca}")

# SEGMENTAÇÃO EM PALAVRAS

palavras = word_tokenize(texto)

print("SEGMENTAÇÃO EM PALAVRAS")

print(palavras)

# REMOÇÃO DE STOPWORDS E PONTUAÇÃO

stop_words = set(stopwords.words('portuguese'))

palavras_filtradas = []

for palavra in palavras:

    palavra_lower = palavra.lower()

    if (
        palavra_lower not in stop_words
        and palavra not in string.punctuation
    ):
        palavras_filtradas.append(palavra_lower)

print("REMOÇÃO DE STOPWORDS")

print(palavras_filtradas)

# STEMMING

stemmer = PorterStemmer()

stemming = []

for palavra in palavras_filtradas:
    radical = stemmer.stem(palavra)
    stemming.append(radical)

print("STEMMING")

print(stemming)

# LEMATIZAÇÃO

lemmatizer = WordNetLemmatizer()

lematizacao = []

for palavra in palavras_filtradas:
    lema = lemmatizer.lemmatize(palavra)
    lematizacao.append(lema)

print("LEMATIZAÇÃO")

print(lematizacao)

# MARCAÇÃO MORFOSSINTÁTICA

marcacao = pos_tag(palavras)

print("POS TAGGING)")

for palavra, classe in marcacao:
    print(f"{palavra} --> {classe}")

# FINALIZAÇÃO

print("PROCESSAMENTO FINALIZADO COM SUCESSO")
