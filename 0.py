# YEE

# begin
# read first input line
# if OPCODE = 'START' then
#     begin
#         save #[OPERAND] as starting address
#         initialize LOCCTR to starting address
#         write line to intermediate fileread next input line
#     end
# else initialize LOCCTR to 0
# while OPCODE < > 'END' do
#     begin
#         if this is not a comment line then
#             begin
#                 if there is a symbol in the LABEL field then
#                     begin
#                         search SYMTAB for LABEL
#                         if found then
#                             set error flag (dublicate symbol)
#                         else insert (LABEL, LOCCTR) into SYMTAB
#                     end
#                 search OPTAB for OPCODE
#                 if found then
#                     add 3 {instruction length} to LOCCTR
#                 else if OPCODE = 'WORD' then
#                     add 3 to LOCCTTR
#                 else if OPCODE = 'RESW' then
#                     add 3 * #[OPERAND] to LOCCTR
#                 else if OPCODE = 'RESB' then
#                     add #[OPERAND] to LOCCTR
#                 else if OPCODE = 'BYTE' then
#                     begin
#                         find length of constant in bytesadd length to LOCCTR
#                     end
#                 else set error flag {invalid operation code}
#             end {if not a comment}
#         write line to intermediate file
#         read next input line
#     end {while}
# write last line to intermediate file
# save {LOCCTR - starting address} as program length
# end {Pass 1}



# begin
# read first input line {from intermediate file}
# if OPCODE = 'START' then
#     begin
#         write listing lineread next input line
#     end
# write Header record to object program
# initialize first Text record
# while OPCODE < > 'END' do
#     begin
#         if this is not a comment line then
#             begin
#                 ssearch OPTAB for OPCODE
#                 if found then
#                     begin
#                         if there is a symbol in OPERAND field then
#                             begin
#                                 search SYMTAB for OPERAND
#                                 if found then
#                                     store symbol value as operand address
#                                 else
#                                     begin
#                                         store 0 as operand address
#                                         set error flag {undefined symbol}
#                                     end
#                             end {if symbol}
#                         else
#                             store 0 as operand address
#                         assemble the object code instruction
#                     end {if found}
#                 else if OPCODE = 'BYTE' or 'WORD' then
#                     convert constant to object code
#                 if object code will not fit into the current Text record them
#                     begin
#                         thie Text record to object program
#                         initialize new Text record
#                     end
#                 add object code to Text record
#             end {if not comment}
#         write listing line
#         read next input line
#     end {while}
# write last Text record to object program
# write End record to object program
# write last listing line
# end {Pass 2}








# sic assembler by turtle
# Yee

# Textbook:
# System Software: An Introduction to Systems Programming 3rd Edition
# by Leland L. Beck

# pass 1 (define symbols):
    # 1. assign addresses to all statements in the program 
    # 2. save the addresses assigned to all lables for use in pass 2
    # 3. perform some processing of assembler directives (this includes
    # processing that affects address assignment, such as determining the
    # length of data areas defined by BYTE, RESW, etc.)

# pass 2 (assemble instructions and generate object program):
    # 1. assemble instructions (translates opcodes and looking up addresses)
    # 2. generates data values defined by BYTE, WORD, etc.
    # 3. perform processing of assembler directive not done during pass 1
    # 4. write the object program and the assembly listing


# OPTAB
# hard-coded

# 동작
# 1. read source file
# 2. pass 1
# 3. pass 2
# 4. save file
# 5. end of program



# 튜플로 하지 뭐..
# 다 튜플로 해! 꺄르륵! 
# 입력은 리스트 오브 3-튜플로 하자
# 출력은 리스트 of 리스트(length:3)으로 하자
# 결국 죄다 리스트로 하게되었다
# [label, opcode, operand, loc]
# 아 이거 맘에안드네
# .loc 이렇게 접근하고싶은데 어떻게하지
# 여기도 구조체가 있나?
# 나중에 대소문자 문제 처리해야!
# 파일에서 입력 받을 때 다 upper case 해버리자

#
# functions
#

# 
# def pass1():
# 

# def pass2():
#     # for every line 
#         # 라벨 처리
#         # opcode 처리
#         # operand 처리

# 
# 함수들은 안쓰는구나?
# 응
# 

#
# optab
#

optab = {"ADD": "18", "AND": "40", "COMP": "28", "DIV":"24", "J": "3C", "JEQ":"30", "JGT":"34", "JLT":"38", "JSUB":"48", "LDA":"00", "LDCH":"50", "LDL":"08", "LDX":"04", "MUL":"20", "OR":"44", "RD": "D8", "RSUB":"4C", "STA":"0C", "STCH":"54", "STL":"14", "STSW":"E8", "STX":"10", "SUB":"1C", "TD":"E0", "TIX":"2C", "WD":"DC"}
# hard coded


#
# symtab
#

symtab = {}
# key:value = symbol name : address



#
# main?
#

fsource = open("source.txt", 'r')
listOfLine0 = []
listOfLine = []
# read source file
while True:
    line = fsource.readline()
    if not line: break
    list0.append(line)

for line in list0:
    line = line.upper()

fsource.close()
# tab으로 나눔
for line in listOfLine0:
    line = line.replace("\n", "")
    temp = line.split("\t")
    listOfLine.append(temp)

del listOfLine0

# pass1

# read first input line
# if OPCODE = 'START' then
#     save #[OPERAND] as starting address
#     initialize LOCCTR to starting address
#     write line to intermediate fileread next input line
# else initialize LOCCTR to 0
# while OPCODE < > 'END' do
#     if this is not a comment line then
#         if there is a symbol in the LABEL field then
#             search SYMTAB for LABEL
#             if found then
#                 set error flag (dublicate symbol)
#             else insert (LABEL, LOCCTR) into SYMTAB
#         search OPTAB for OPCODE
#         if found then
#             add 3 {instruction length} to LOCCTR
#         else if OPCODE = 'WORD' then
#             add 3 to LOCCTTR
#         else if OPCODE = 'RESW' then
#             add 3 * #[OPERAND] to LOCCTR
#         else if OPCODE = 'RESB' then
#             add #[OPERAND] to LOCCTR
#         else if OPCODE = 'BYTE' then
#             find length of constant in bytesadd length to LOCCTR
#         else set error flag {invalid operation code}
#     write line to intermediate file
#     read next input line
# write last line to intermediate file
# save {LOCCTR - starting address} as program length

# listOfLine[i][]
# [0] = label, [1] = opcode, [2] = operand, [3] = loc도 안쓸듯, [4] = flag isComment는 안씀

# for i in range len(listOfLine):
locctr = 0
error_duplicate_symbol = False
error_invalid_operation_code = False
starting_address = 0
program_length = 0
if listOfLine[0][1] == "START":
    starting_address = int(listOfLine[0][2])
    locctr = starting_address
else:
    starting_address = 0
    locctr = starting_address
for line in listOfLine[1:]:
    # _label = line[0]
    # _opcode = line[1]
    # _operand = line[2]
    # _loc = line[3]
    # is comment line
    if line[0].startswith("."):
        pass
    # if this is not a comment line
    else:
        if not line[0] == "":
            if symtab[line[0]]:
                error_duplicate_symbol = True
            else:
                symtab[line[0]] = locctr
                
        if optab[line[1]]:
            line[3] = locctr
            locctr = locctr + 3
        
        elif line[1] == "WORD":
            line[3] = locctr
            locctr = locctr + 3
        
        elif line[1] == "RESW": 
            line[3] = locctr
            locctr = locctr + 3 * int(line[2])
       
        elif line[1] == "RESB": 
            line[3] = locctr
            locctr = locctr + int(line[2] )
      
        elif line[1] == "BYTE": 
            line[3] = locctr
            if line[2].startswith("C"):
                locctr = locctr + len(line[2])
            elif line[2].startswith("X"):
                locctr = locctr + int(line[2][1:-1], 16)    #hex string  to int
       
        else: error_invalid_operation_code = True
        
program_length = locctr - starting_address



# pass 2

# read first input line {from intermediate file}
# if OPCODE = 'START' then
#     write listing lineread next input line
# write Header record to object program
# initialize first Text record
# while OPCODE < > 'END' do
#     if this is not a comment line then
#         ssearch OPTAB for OPCODE
#         if found then
#             if there is a symbol in OPERAND field then
#                 search SYMTAB for OPERAND
#                 if found then
#                     store symbol value as operand address
#                 else
#                     store 0 as operand address
#                     set error flag {undefined symbol}
#             else
#                 store 0 as operand address
#             assemble the object code instruction
#         else if OPCODE = 'BYTE' or 'WORD' then
#             convert constant to object code
#         if object code will not fit into the current Text record them
#             thie Text record to object program
#             initialize new Text record
#         add object code to Text record
#     write listing line
#     read next input line
# write last Text record to object program
# write End record to object program
# write last listing line

# [0] = label, [1] = opcode, [2] = operand, [3] = loc (사용함), [4] = flag isComment는 안씀

header_record = ""
if listOfLine[0][1] == "START":
    #이거 program 이름 부분 도 처리..해줘..
    header_record = "H" + listOfLine[0][1].ljust(6) + hex(starting_address).zfill(6) + hex(program_length).zfill(6)
    # H + program name + starting address of object program (hexadecimal) + program length in bytes (hexadecimal)
    # 1 +      6       +                        6                         +                    6               
else:
    pass

error_undefined_symbol = False
error_opcode = False

# 이 리스트는 immediate file 의 라인 하나마다의 object code 들을 원소로 가짐니다
text_record_list = []

for line in listOfLine[1:]:
    # 라인 하나당 이 변수에 텍스트를 써넣을거임
    # 그리고 그 텍스트를 object code에 써넣을거임
    temp_object_code = ""
    temp_object_code_list = []

    if not line[0].startswith("."):
        # then this is a comment line
        if optab[line[1]]:
            #if line[1] in optab:
            #if key in dic:
            temp_object_code_list[0] = optab[line[1]]
            if line[2]:
                if symtab[line[2]]:
                    temp_object_code_list.append(symtab[line[2]])
                else:
                    temp_object_code_list[1] = "0"
            else:
                temp_object_code_list[1] = "0"
            temp_object_code += temp_object_code_list[0]
            temp_object_code += hex(int( ( "0" + bin(int(temp_object_code_list[1], 16)).zfill(15) ), 2)) #bin to hex 함수를 만들어서  쓰렴,,
            # 중간에 "0" indicates indexed-addressing mode
            text_record_list.append((temp_object_code, list[3])
            ####################################### this fucking elif code block has INVALID SYNTAX error #########################
            #####################################################################################################################
        elif expression:
            pass
        elif line[1] != "END":
            error_opcode = True
        elif line[1] == "BYTE" or line[1] == "WORD":
            # convert constant to object code:
            if line[2].startswith("C"):
                temp_object_code = map(ord, line[2][1:-1])
            elif line[2].startswith("X"):
                temp_object_code = line[2][1:-1]
            else:
                # 오류 처리는..?
                # 다음에 해
                # 너무하네
                temp_object_code = line[2].zfill(6)
            text_record_list.append((temp_object_code, line[3]))
        else:
            break



# Text record
# T + starting address for object code in this record (hexadecimal) + 
# length of object code in this record in bytes (hexadecimal) + 
# object code, represented in hexadecimal (2 columns per byte of object code)
# 1 + 6 + 
# 2 + 
# 60 (column 10-69)

# End record
# E + address of first excutable instruction in object program (hexadecimal)
# 1 +                                  6                                    

fobject = open("object.txt", 'w')
fobject.write(header_record)
fobject.write("\n")
i = 0
temp_temp = "T"
# Tuple, ("object code", "loc")
for linetuple in text_record_list:
    if i == 0:
        temp_temp = "T"
        temp_temp += linetuple[1]
    i += len(linetuple[0]) /2
    if i > 60:
        fobject.write(temp_temp + "\n")
        temp_temp = "T"
        i = 0
        break
    else:
        temp_temp += linetuple[0]
    


    # temp_temp.append(linetuple.)



    # if object code will not fit into the current Text record them
#             thie Text record to object program
#             initialize new Text record
#         add object code to Text record


fobject.close