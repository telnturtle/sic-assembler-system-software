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

# ??????
# 1. read source file
# 2. pass 1
# 3. pass 2
# 4. save file
# 5. end of program



# ?????? ?????? ???????????? ???????????????
# ??? ??????. ?????? ????????? ??????
# ?????? ?????? ?????? ?????? ???????????? ????????????
# [label, opcode, operand, loc]
# .loc ????????? ????????????????????? ??????????????? ??? ???????????? ???????????????
# ????????? ???????????? ??????? ??? ????????????
# ????????? ???????????? ?????? ????????????! ??? ??????
# ???????????? ?????? ?????? ??? ??? upper case ????????????. ??? ??????

#
# functions
#

def hextobin(hexval):
    thelen = len(str(hexval)) *4
    binval = bin(int(str(hexval), 16))[2:]
    while (len(binval) < thelen):
        binval = '0' + binval
    return binval # return string

def bintohex(binval):
    thelen = len(binval) / 4
    hexval = hex(int(binval, 2))[2:]
    while (len(hexval) < thelen):
        hexval = '0' + hexval
    return hexval # return string

def dectohex(decval):
    # hex()??? string??? ????????????? ?????????.
    return hex(decval)[2:]

# def hextodec(hexval):
#     return int(hexval, 16)
# ????????? ??????????????? ????????? ????????????

def take(num, lyst):
    rlist = []
    for i in range(0,num):
        rlist.append(lyst[i])
    return rlist


#
# optab
#

optab = {"ADD": "18", "AND": "40", "COMP": "28", "DIV":"24", "J": "3C", "JEQ":"30", "JGT":"34", "JLT":"38", "JSUB":"48", "LDA":"00", "LDCH":"50", "LDL":"08", "LDX":"04", "MUL":"20", "OR":"44", "RD": "D8", "RSUB":"4C", "STA":"0C", "STCH":"54", "STL":"14", "STSW":"E8", "STX":"10", "SUB":"1C", "TD":"E0", "TIX":"2C", "WD":"DC"}
# hard coded


#
# symtab
#

symtab = {}
# key:value = symbol_name:address
# symbol = variable



#
# main?
#

fsource = open("source.txt", 'r')
listOfLine = []
# read source file
while True:
    line = fsource.readline()
    if not line: break
    listOfLine.append(line)

fsource.close()

for i in range(len(listOfLine)):
    listOfLine[i] = listOfLine[i].upper()

# tab?????? ??????
for i in range(len(listOfLine)):
    _temp = listOfLine[i].replace("\n", "")
    listOfLine[i] = ["", "", "", ""]
    listOfLine[i] = (_temp.split("\t")) + ["", "", "", "", ""]
    listOfLine[i] = take(4, listOfLine[i])

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
# [0] = label, [1] = opcode, [2] = operand, [3] = loc??? ?????????, [4] = flag isComment??? ??????

# for i in range len(listOfLine):
locctr = 0
error_duplicate_symbol = False
error_invalid_operation_code = False
starting_address = 0
program_length = 0
flag_address_of_first_excutable_instruction_is_not_writed_yet = True
address_of_first_excutable_instruction = 0


# first line of source
if listOfLine[0][1] == "START":
    starting_address = int(listOfLine[0][2], 16)
    locctr = starting_address
else:
    starting_address = 0
    locctr = starting_address


# ????????? ????????? ?????????
for i in range(1, len(listOfLine)):
    # _label = line[0]
    # _opcode = line[1]
    # _operand = line[2]
    # _loc = line[3]
    # ?????? ????????? ?????? ??? ??????????????? (line -> listOfLine[i])
    if listOfLine[i][0].startswith("."):
        # then this is a comment line
        pass
    # if this is not a comment line
    else:
        if not listOfLine[i][0] == "":
            if listOfLine[i][0] in symtab:
                error_duplicate_symbol = True
            else:
                symtab[listOfLine[i][0]] = locctr
                
        if listOfLine[i][1] in optab:
            if flag_address_of_first_excutable_instruction_is_not_writed_yet:
                # End record??? ?????????
                address_of_first_excutable_instruction = locctr
            listOfLine[i][3] = locctr
            locctr = locctr + 3
        
        elif listOfLine[i][1] == "WORD":
            listOfLine[i][3] = locctr
            locctr = locctr + 3
        
        elif listOfLine[i][1] == "RESW": 
            listOfLine[i][3] = locctr
            locctr = locctr + 3 * int(listOfLine[i][2])
       
        elif listOfLine[i][1] == "RESB": 
            listOfLine[i][3] = locctr
            locctr = locctr + int(listOfLine[i][2])
      
        elif listOfLine[i][1] == "BYTE": 
            listOfLine[i][3] = locctr
            if listOfLine[i][2].startswith("C"):
                locctr = locctr + len(listOfLine[i][2][2:-1])
            elif listOfLine[i][2].startswith("X"):
                locctr = locctr + int(listOfLine[i][2][2:-1], 16)    #hex string  to int
       
        else: error_invalid_operation_code = True
        
program_length = locctr - starting_address




#####################################debug######################################3


# print("after pass 1")
# print("symtab:")
# for value in symtab:
#     print(value)





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

# [0] = label, [1] = opcode, [2] = operand, [3] = loc (?????????), [4] = flag isComment??? ??????

header_record = ""
if listOfLine[0][1] == "START":
    #?????? program ?????? ?????? ??? ??????..??????..
    header_record = "H" + listOfLine[0][0].ljust(6) + dectohex(starting_address).zfill(6) + dectohex(program_length).zfill(6)
    header_record = header_record.upper()
    # H + program name + starting address of object program (hexadecimal) + program length in bytes (hexadecimal)
    # 1 +      6       +                        6                         +                    6               
else:
    pass

error_undefined_symbol = False
error_opcode = False

# ??? ???????????? immediate file ??? ?????? ??????????????? object code ?????? ????????? ????????????
text_record_list = []

# for line in listOfLine[1:]:
#     # ?????? ????????? ??? ????????? ???????????? ???????????????
#     # ????????? ??? ???????????? object code??? ???????????????
#     temp_object_code = ""
#     temp_object_code_list = []

#     if not line[0].startswith("."):
#         # then this is a comment line
#         if optab[line[1]]:
#             #if line[1] in optab:
#             #if key in dic:
#             temp_object_code_list[0] = optab[line[1]]
#             if line[2]:
#                 if symtab[line[2]]:
#                     temp_object_code_list.append(symtab[line[2]])
#                 else:
#                     temp_object_code_list[1] = "0"
#             else:
#                 temp_object_code_list[1] = "0"
#             temp_object_code += temp_object_code_list[0]
#             temp_object_code += hex(int( ( "0" + bin(int(temp_object_code_list[1], 16)).zfill(15) ), 2)) #bin to hex ????????? ????????????  ??????,,
#             # ????????? "0" indicates indexed-addressing mode
#             text_record_list.append((temp_object_code, list[3])
# ????????? ?????? ??????????????? ??? ???????????? elif??? ????????? ???????????? ???????????????. ???????????? ???????????? ????????? ??????. invalid syntax ??????.
# ????????? ????????? ????????????.
# ?????????????????? indentation??? ???????????????????????? ????????? ????????????.
# # ????????? ????????? ?????? ???????????? ??? ????????????. ?????? ?????????.
# ??? ?????? ????????? ??? ?????? ?????? ??????????????????. ????????? ????????? ??? ????????? ????????? ?????? ???????????????
#         elif line[1] != "END":
#             error_opcode = True
#         elif line[1] == "BYTE" or line[1] == "WORD":
#             # convert constant to object code:
#             if line[2].startswith("C"):
#                 temp_object_code = map(ord, line[2][1:-1])
#             elif line[2].startswith("X"):
#                 temp_object_code = line[2][1:-1]
#             else:
#                 # ?????? ?????????..?
#                 # ????????? ???
#                 # ????????????
#                 temp_object_code = line[2].zfill(6)
#             text_record_list.append((temp_object_code, line[3]))
#         else:
#             break

for i in range(1, len(listOfLine)):
    temp_object_code = ""
    temp_object_code_list = ["", "", ""]
    # ???????????? ????????? ??????

    if not listOfLine[i][0].startswith("."):
        if listOfLine[i][1] in optab:
            temp_object_code_list[0] = optab[listOfLine[i][1]]
            if listOfLine[i][2]:
                if listOfLine[i][2] in symtab:
                    # debug###########################################################
                    # print("symtab[listOfLine[i][2]] = " + str(symtab[listOfLine[i][2]]))
                    temp_object_code_list[1] = symtab[listOfLine[i][2]]
                else:
                    # temp_object_code_list[1] = "0"
                    temp_object_code_list[1] = "0"
            else:
                temp_object_code_list[1] = "0"
            # debug###############################################
            print("temp_object_code_list[0] = " + temp_object_code_list[0])
            # print("temp_object_code_list[next] = " + bintohex("0" + hextobin(temp_object_code_list[1]).zfill(15)))
            # print("temp_object_code_list[next] = " + hextobin(temp_object_code_list[1]).zfill(15))
            print("temp_object_code_list[next] = " + str(temp_object_code_list[1]))

            temp_object_code = temp_object_code_list[0] + bintohex("0" + hextobin(temp_object_code_list[1]).zfill(15))
            # temp_object_code += hex(int(("0" + bin(int(temp_object_code_list[1], 16)).zfill(15)), 2))
            # 
            # ?????? ????????? ????????? ????????? ???????????? ?????? ??????!
            # ?????? hex to bin ????????? ???????????? ????????????!
            # 
            text_record_list.append((temp_object_code, listOfLine[i][3]))
        elif listOfLine[i][1] != "END":
            error_opcode = True
        elif listOfLine[i][1] == "BYTE" or listOfLine[i][1] == "WORD":
            if listOfLine[i][2].startswith("C"):
                temp_object_code = map(ord, listOfLine[i][2][2:-1])
            elif listOfLine[i][2].startswith("X"):
                temp_object_code = listOfLine[i][2][2:-1]
            else:
                temp_object_code = listOfLine[i][2].zfill(6)
            text_record_list.append((temp_object_code, line[3]))
        else:
            break


print("text_record_list")
print("")

for l in text_record_list:
    print(l)

print("")



# Text record
# T + starting address for object code in this record (hexadecimal) + 
# length of object code in this record in bytes (hexadecimal) + 
# object code, represented in hexadecimal (2 columns per byte of object code)
# 1 +                                6                              + 
#                               2                             + 
#                                 60 (column 10-69)

# End record
# E + address of first excutable instruction in object program (hexadecimal)
# 1 +                                  6                                    

fobject = open("object.txt", 'w')
fobject.write(header_record)
fobject.write("\n")
thei = 0
temp_temp = "T"
# Tuple, ("object code", "loc")
for linetuple in text_record_list:
    print ("thei = " + str(thei))
    if thei > 60:
        fobject.write(temp_temp.upper() + "\n")
        temp_temp = "T"
        thei = 0
    if thei == 0:
        temp_temp = "T"
        temp_temp += str(dectohex(linetuple[1])).zfill(6)
    thei += len(linetuple[0])
    temp_temp += linetuple[0]
fobject.write(temp_temp + "\n")
end_record = "E" + dectohex(address_of_first_excutable_instruction).zfill(6)
fobject.write(end_record)

# ????????? Pythonic ?????? ????????? ????????? ?????????

fobject.close


###################################
# T???????????? ????????? startingaddress??? 1000?????? 4096?????? ????????? ????????? ????????????

# int() can't convert non-string with explicit base
# ??? int(param, base)??? parameter??? str?????? ??????

# ????????? ????????? .upper() ??????

# ????????? ???????????? ?????? byte x'05'??? object code??? ?????????????????? ???????????????