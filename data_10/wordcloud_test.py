from PIL import Image  # для работы с изображениями
import matplotlib.pyplot as plt 
from wordcloud import WordCloud  # pip install wordcloud

result_dict = {"Василий" : 100, "Питонов" : 20, "программист" : 5, "оптимист" : 1}

def make_wordcloud(result_dict):
    """
    Сохраняет облако слов в изображение result_image.png
    """
    wc_arguments_dict = {
        "background_color" : "white",
        "max_words" : 1000,
        "width" : 1000,
        "height" : 1000,
        "relative_scaling" : 0.5,
        "normalize_plurals" : False
    }
    wc = WordCloud(**wc_arguments_dict).generate_from_frequencies(result_dict)
    plt.figure(figsize=(10, 10))
    plt.axis("off")
    plt.imshow(wc)
    plt.savefig("result_image.png", dpi=100, facecolor='k', bbox_inches='tight')

make_wordcloud(result_dict)