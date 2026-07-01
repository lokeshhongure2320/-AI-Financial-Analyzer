def search(query, model, index, chunks, k=3):
    query_vec = model.encode([query])
    D, I = index.search(query_vec, k)

    return [chunks[i] for i in I[0]]