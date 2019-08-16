# --coding: utf8--

import snowballstemmer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from sklearn.cluster import AgglomerativeClustering

from modules.io import read_file_to_string, write_string_file


class LemmatizedTfidfVectorizer(TfidfVectorizer):
    """
    Vectorizer that first lemmatizes words.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.stemmer = snowballstemmer.stemmer('English')

    def build_analyzer(self):
        analyzer = super(LemmatizedTfidfVectorizer, self).build_analyzer()

        def lemmatize(phrase):
            words = analyzer(phrase)
            return [self.stemmer.stemWord(word)
                    for word in words]

        return lemmatize


def go_cluster(input_path, output_path):

    data = read_file_to_string(input_path)

    keywords = [line for line in data.splitlines() if line]

    vec = LemmatizedTfidfVectorizer(stop_words=ENGLISH_STOP_WORDS)
    vectorized = vec.fit_transform(keywords)

    ac = AgglomerativeClustering().fit(vectorized.toarray())
    clusters = {}

    for keyword, cluster_id in zip(keywords, ac.labels_):
        clusters.setdefault(cluster_id, []).append(keyword)

    clustered_keywords = ""
    for items in clusters.items():
        for single_item in items[1]:
            clustered_keywords += single_item + '\n'
        clustered_keywords += '\n'

    write_string_file(output_path, clustered_keywords)
