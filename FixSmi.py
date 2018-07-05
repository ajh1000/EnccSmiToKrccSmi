import os
import cchardet as chardet
import codecs


'''
srt는 ansi가 아닌 다른 형식으로 인코딩 되어 있어도 TV에서 정상적으로 자막이 출력됐었음.
smi만 고치면 해결됨
'''

# Getting the current work directory (cwd)
thisdir = os.getcwd()
smiDirArr=list()
srtDirArr=list()


# r=root, d=directories, f = files
for r, d, f in os.walk(thisdir):
    for file in f:
        if '.smi' in file:
            smiDirArr.append(os.path.join(r, file))


print('Fixing Smi...')
count = 1
for dir in smiDirArr:
    print(count,'/',len(smiDirArr))

    #인코딩 타입 찾기
    with open(dir, 'rb') as file:
        det = chardet.detect(file.read())['encoding']

    #알맞게 인코딩하여 읽기
    #수정 작업
    with open(dir, 'r', encoding=det) as file:
        lines = file.read()
        lines = lines.replace('encc','krcc')
        lines = lines.replace('ENCC','KRCC')
        lines = lines.replace('ENUSCC','KRCC')
        lines = lines.replace('</P></SYNC>', '')

        #remove <samiparam> tag
        firstIdx=lines.find('<SAMIParam>')

        #found target tag
        if firstIdx > -1:
            endIdx = lines.find('</SAMIParam>')
            lines = lines[:firstIdx] + lines[endIdx + (len('</SAMIParam>') + 1):]



    #ANSI로 인코딩하여 덮어쓰기
    with open(dir, 'w', encoding='cp949') as file:
        file.write(lines)

    count+=1

print('')
print('Completed!!!')
input('Press Enter To Exit...')
