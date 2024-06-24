import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import spacy

# Download the vader_lexicon
nltk.download('vader_lexicon')

def perform_semantic_analysis(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)

    tokens = [token.text for token in doc]
    entities = [(entity.text, entity.label_) for entity in doc.ents]

    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)

    compound_score = sentiment['compound']
    if compound_score > 0.5:
        overall_sentiment = 'Positive'
    elif compound_score < -0.5:
        overall_sentiment = 'Negative'
    else:
        overall_sentiment = 'Neutral'

    result = {
        "Tokens": tokens,
        "Entities": entities,
        "Sentiment": {
            "compound": compound_score,
            "positive": sentiment['pos'],
            "neutral": sentiment['neu'],
            "negative": sentiment['neg'],
            "overall": overall_sentiment
        }
    }

    return result

# Example usage
# text = "The new iPhone has amazing features and an incredible camera quality."
# analysis_result = perform_semantic_analysis(text)
# print(analysis_result)




# from gtts import gTTS
# import os
# from django.conf import settings


# def convert_text_to_audio(text):
#     tts = gTTS(text=text, lang='en')  # language is set to English ('en')
#     audio_file_path = os.path.join("../media", 'output_audio.mp3')
#     tts.save(audio_file_path)
#     return audio_file_path  # Return the path to the saved audio file


# # Example usage
# text = "The blaah iPhone has amazing features and an incredible camera quality."
# analysis_result = convert_text_to_audio(text)
# print(analysis_result)



from nltk import word_tokenize, sent_tokenize
import textwrap

def summarize_text(text):
    # Split the text into sentences and paragraphs
    sentences = sent_tokenize(text)
    paragraphs = [sentences[i:i+5] for i in range(0, len(sentences), 5)]

    # Initialize the summary
    summary = ""

    # Loop through each paragraph
    for para in paragraphs:
        # Tokenize each sentence in the paragraph
        tokenized_sentences = [word_tokenize(sentence) for sentence in para]

        # Calculate the importance score for each sentence
        scores = [len(set(tokenized_sentence)) / len(tokenized_sentence) for tokenized_sentence in tokenized_sentences]
        max_index = scores.index(max(scores))

        # Add the most important sentence to the summary
        if summary != "":
            summary += " "  # Add a space between paragraphs
        summary += " ".join(para[max_index])

    # Strip leading and trailing whitespace from the summary
    summary = summary.strip()

    # Replace double spaces with single spaces
    summary = summary.replace('  ', '#')

    summary = summary.replace(' ', '')

    summary = summary.replace('#', ' ')

    return summary

# Example usage
# text = "This implementation ensures that each audio file generated has a unique filename, preventing accidental overwrites of existing files. Adjust the function as per your project's specific requirements and file handling practices."
# analysis_result = summarize_text(text)
# print(analysis_result)
