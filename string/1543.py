target = input()
word = input()

answer = 0
index = 0
target_len = len(target)
word_len = len(word)
while index <= target_len - word_len + 1:
    if target[index:index+word_len] == word:
        answer += 1
        index += word_len
    else:
        index += 1

print(answer)
