import random

def generate_text(CC):
    current_char = CC
    text = current_char
    while current_char != ' ':
        if current_char == 'し':
            next_char = random.choice(['か', 'た'])
        elif current_char == 'か':
            next_char = 'の'
        elif current_char == 'の':
            next_char = 'こ'
        elif current_char == 'こ':
            next_char = random.choices(['の', 'こ', 'し'], weights=[2, 1, 1])[0]
        elif current_char == 'た':
            next_char = 'ん'
        elif current_char == 'ん':
            next_char = random.choice([' ', 'た'])
        text += next_char
        current_char = next_char

    return text

detc = int(input("試行回数を入力してください: "))
count = 0

while True:
    count += 1
    generated_text = generate_text("し")
    with open("file.txt", "a") as f:
        f.write(f"試行回数: {count}, 生成された文字列: {generated_text}\n")
    if count == detc:
        print(f"処理が完了しました。試行回数: {count}")
        break