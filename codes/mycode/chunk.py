##Split a large text into chunks of size max_tokens with an overlap of overlap_tokens.
import heapq
import math
from collections import Counter, defaultdict


def chunk_text(text, max_tokens=100, overlap_tokens=20):
    words = text.split()
    start = 0
    chunks = []
    while start < len(words):
        end = min(start + max_tokens, len(words))

        chunks.append(' '.join(words[start:end]))
        start = end - overlap_tokens
        if end == len(words): break
    return chunks


# text = "This is a sample document for chunking into smaller pieces for processing"
# chunks = chunk_text(text, max_tokens=5, overlap_tokens=2)
#
# for i, c in enumerate(chunks):
#     print(f"Chunk {i + 1}: {c}")


# Top K Similar Chunks (Mini Vector Search)

def top_k_similar_chunks(embeddings, query, k):
    def cosine_similarity(A, B):
        # cosine
        # similarity =
        # ∣∣A∣∣⋅∣∣B∣∣
        # A⋅B
        # ​

        dot = sum(a * b for a, b in zip(A, B))
        nor1 = math.sqrt(sum(a * a for a in A))
        nor2 = math.sqrt(sum(b * b for b in B))
        return dot / (nor1 * nor2)

    min_heap = []
    # O(nlgk)
    for i, embedding in enumerate(embeddings):
        sim = cosine_similarity(embedding, query)
        if len(min_heap) < k:
            heapq.heappush(min_heap, (sim, i))
        else:
            heapq.heappushpop(min_heap, (sim, i))

    return sorted(min_heap, reverse=True)


# embeddings = [
#     [0.1, 0.2, 0.3],
#     [0.4, 0.2, 0.1],
#     [0.9, 0.8, 0.7]
# ]
#
# query = [0.1, 0.2, 0.25]
# k = 2
# print(top_k_similar_chunks(embeddings, query, k))

# Given a list of spans (start, end), merge all overlapping intervals.
# intervals = [(1,5), (3,7), (10,12), (11,15)]

def merge_intervals(intervals):
    st = []
    intervals.sort(key=lambda x: x[0])
    for s, e in intervals:
        if st and st[-1][1] >= s:
            res_s, res_e = st[-1][0], st[-1][1]
            st.pop()
            st.append((res_s, max(res_e, e)))
        else:
            st.append((s, e))
    return st


# intervals = [(1, 5), (3, 7), (10, 12), (11, 15)]
# print(merge_intervals(intervals))


# Given a list of documents and a query, return top K most relevant documents using TF-IDF scoring.
import math
from collections import Counter

def tokenize(text):
    return text.lower().split()


def compute_idf(docs):
    N = len(docs)
    df = {}

    for doc in docs:
        words = set(tokenize(doc))
        for w in words:
            df[w] = df.get(w, 0) + 1

    idf = {}
    for w, count in df.items():
        idf[w] = math.log(N / (1 + count))

    return idf


def compute_tf(doc):
    words = tokenize(doc)
    total = len(words)
    tf = Counter(words)

    return {w: tf[w] / total for w in tf}


def search(docs, query, k):
    idf = compute_idf(docs)
    query_words = tokenize(query)

    scores = []

    for i, doc in enumerate(docs):
        tf = compute_tf(doc)
        score = 0

        for w in query_words:
            if w in tf and w in idf:
                score += tf[w] * idf[w]

        scores.append((score, i))

    # get top k
    scores.sort(reverse=True)
    return scores[:k]
docs = [
    "patient had an accident on jan 10",
    "treatment included surgery and medication",
    "accident reported on feb 5 with minor injuries"
]

query = "accident date"
k = 2
print(search(docs, query, k))
