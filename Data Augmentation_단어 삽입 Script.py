import os
import random

def add_maewoo_to_file(file_path):
    # '매우'를 추가할 위치를 랜덤하게 결정
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        random_position = random.randint(0, len(content))
        
    # '매우'를 추가한 새로운 내용 생성
    word_to_insert = ' 그러니까 '
    new_content = content[:random_position] + word_to_insert + content[random_position:]
    
    # 파일에 새로운 내용 저장
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def main():
    folder_path = r"C:\Users\USER\Desktop\대출사기형_txt - 복사본 (3)"
    for i in range(1, 5793):
        file_path = os.path.join(folder_path, f'file    ({i}).txt')
        add_maewoo_to_file(file_path)
        print("완료")

if __name__ == '__main__':
    main()
