import pickle
import os

filename = 'score.bin'

def save_data(scores):
    with open(filename, 'wb') as file:
        pickle.dump(scores, file)

def load_data():
    scores = []
    with open(filename, 'rb') as file:
        scores = pickle.load(file)
    return scores
    
def input_scores() :
    scores = []
    i = 1
    while True:
        score = int(input(f'#{i}? '))
        if score < 0:
            break
        scores.append(score)
        i += 1
    save_data(scores)
    return scores

def get_average(lst):
    total = 0
    for n in lst:
        total += n
    return total / len(lst)

def show_scores(lst):
    for n in lst:
        print(n, end=' ')
    print()
    
if os.path.exists(filename):
    print('[파일 읽기]')
    scores = load_data()
else:
    print('[점수입력]')
    scores = input_scores()

print('\n[점수출력]')
print('개인점수: ', end='')
show_scores(scores)

avg = get_average(scores)
print(f'평균: {avg:.1f}')
