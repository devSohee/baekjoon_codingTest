def solution(data, ext, val_ext, sort_by):
    e = ["code", "date", "maximum", "remain"]
    ext_idx = e.index(ext)
    sort_idx = e.index(sort_by)
    answer = []
    for d in data:
        if d[ext_idx] < val_ext:
            answer.append(d)
            
    return sorted(answer, key = lambda x: (x[sort_idx]))
