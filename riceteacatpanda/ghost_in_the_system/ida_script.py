import idautils

sc = idautils.Strings()
# the buffer is at offset 0x00000000000021E8 offset
buffer = str([s for s in sc if hex(s.ea) == '0x21e8L'][0])
flag = ''
get_next = False


for function_ea in idautils.Functions():
    for ins in idautils.FuncItems(function_ea):
        if idaapi.isCode(idaapi.getFlags(ins)):
            cmd = idc.GetDisasm(ins)
            if get_next and idc.GetMnem(ins) == 'mov':
                value = idc.GetOpnd(ins, 1)
                if value.endswith('h'):
                    value = "0x" + value.replace('h', '')
                    value = int(value, 16)
                    flag += buffer[value]
                get_next = False
            if cmd == 'lea     rax, [rbp+otxt]':
                get_next = True

print(flag)