def solution(msg):
    answer = []
    vocab = {chr(i) : i-64 for i in range(ord('A'), ord('Z')+1)}
    ls = list(msg[::-1])
    done, buffer = '', ls.pop()
    while len(done) < len(msg):
        if buffer in vocab and ls: 
            buffer += ls.pop()
            continue
        elif buffer in vocab and not ls:
            answer.append(vocab[buffer])
            done += buffer
            return answer
        # add new word
        vocab[buffer] = len(vocab)+1
        # 
        answer.append(vocab[buffer[:-1]])
        done += buffer[:-1]
        buffer = buffer[-1]
    
    return answer