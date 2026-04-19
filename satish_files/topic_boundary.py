from sklearn.linear_model import LogisticRegression
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Train model
model = LogisticRegression().fit([[0.9],[0.2]], [0,1])

def split_topics(text):
    s = text.split(". ")
    v = CountVectorizer().fit_transform(s)

    print(s[0])
    prev_topic = False   # 🔹 control multiple splits

    for i in range(1, len(s)):
        sim = cosine_similarity(v[i-1], v[i])[0][0]
        pred = model.predict([[sim]])[0]

        # 🔹 Apply condition to avoid repeated splits
        if pred == 1 and not prev_topic:
            print("\n--- New Topic ---")
            prev_topic = True
        else:
            prev_topic = False

        print(s[i])

# Input
text = input("Enter text: ")
split_topics(text)
