import gensim

qs = ["Do students need to own a computer to attend Holberton School",
"What is the job market like for software and operations engineers",
"Do you help students find a job after Holberton School",
"Do you deliver a degree",
"Do you accept international students",
"What does Full Stack Engineer mean",
"Can I attend Holberton School online",
"How does housing work"]

FILE = "google_vecs.gensim"
try:
    model = gensim.models.Word2Vec.load(FILE)
except:
    print("Constructing model")
    # download from https://docs.google.com/uc?id=0B7XkCwpI5KDYNlNUTTlSS21pQmM&export=download
    model = gensim.models.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
    model.init_sims(replace=True)
    model.save(FILE)

while True:
    str1 = raw_input("question: ")
    l1 = str1.split(" ")
    l1 = filter(lambda word: word in model.vocab, l1)

    qs_l = [[0, filter(lambda word: word in model.vocab, l.lower().split(" ")), l] for l in qs]

    if not l1:
        print("Didn't understand your question")
        continue
    try:
        for i, l in enumerate(qs_l):
            qs_l[i][0] = model.n_similarity(l1, l[1])
        q = max(qs_l, key=lambda l: l[0])
        print(q[0], q[2])
    except Exception, e:
        print("Exception: ", e)
