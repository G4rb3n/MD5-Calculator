#coding:utf-8

import os
import argparse
import pefile
import hashlib

# 计算PE文件的MD5信息
def get_sec_md5(file_path, sec_name) :

    print(" " + os.path.basename(file_path))
    print("\t|")
    if (sec_name == 'file') or (sec_name == 'all') :
        print("\t|-- [ file ] --> [" + hashlib.md5(open(file_path, 'rb').read()).hexdigest() + "]")

    try :
        pe = pefile.PE(file_path)
        for section in pe.sections:
            if sec_name != '' :
                if (sec_name.encode() in section.Name) or (sec_name == 'all') :
                    print("\t|-- [ " + section.Name.decode()[:-2] + "] -> [" + section.get_hash_md5() + "]")
        pe.close()
    except :
        return 0


if __name__ == "__main__" :

    # 接收用户参数
    parser = argparse.ArgumentParser(description="MD5_Generator")
    parser.add_argument('path')
    parser.add_argument('sec_name')
    args = parser.parse_args()

    print("\n\n\t\t\tMD5 Generator")
    print("=================================================================\n")

    # 遍历文件夹
    if os.path.isdir(args.path):
    	files = os.listdir(args.path)
    	for file in files:
            file_path = args.path + file
            get_sec_md5(file_path, args.sec_name)
    
    # 若是文件，则直接计算MD5信息
    else :
        get_sec_md5(args.path, args.sec_name)

