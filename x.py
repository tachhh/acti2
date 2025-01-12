def cal(score):
    res = sum(score) / len(score)
    return f"{res:.2f}"  

def add_score(subject_score, subject, score):
    subject_score_dict = eval(subject_score) 
    if not(score < 0 or subject == ""):
        subject_score_dict[subject] = score
    avgscore = cal(list(subject_score_dict.values()))
    print(f"{subject_score_dict}, Average score: {avgscore}")

x = input("")
paramiter = x.split("|")
subject_score = paramiter[0].strip()
subject = paramiter[1].strip().replace("'", "")
score = int(paramiter[2].strip())
add_score(subject_score, subject, score)