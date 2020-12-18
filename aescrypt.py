#! /usr/bin/env python3

import os, sys, subprocess

if os.getcwd() != "/usr/bin":
  os.system('sudo cp aescrypt.py aescrypt && sudo mv aescrypt /usr/bin')

if os.geteuid() != 0:
  print("Please run with sudo...")
  exit()

reqs = subprocess.check_output([sys.executable, '-m' 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
if 'pyAesCrypt' not in installed_packages:
  print("Package 'pyAesCrypt' not installed, installing now...")
  subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyAesCrypt'])

import pyAesCrypt

def wait():
  wait = input("PRESS ENTER TO CONTINUE")

if len(sys.argv) < 8 or '--help' in sys.argv or '-h' in sys.argv:
  print('AESCrypt v1.0\nSourced on Github and created by Cisc0-gif, Ecorp7@protonmain.com\n')
  print('        -h, --help      Displays this help menu')
  print('        -e, --encrypt   Encrypts file')
  print('        -d, --decrypt   Decrypts file')
  print('        -p, --pass      *REQ*Encrypts/Decrypts File with Password')
  print('        -b, --buff      *REQ*File Encrypt/Decrypt Buffer Size (64 = 64Kb)')
  print('        -f, --file      *REQ*Filepath of File to Encrypt/Decrypt')
  print('Ex:     aescrypt -e -p PASSWORD -b 64 -f /home/kali/test.txt')
  print('Ex:     aescrypt --decrypt --pass PASSWORD --buff 64 --file /home/kali/test.txt')

short = ['-h', '-p', '-b', '-f', '-e', '-d']
long = ['--help', '--pass', '-buff', '--file', '--encrypt', '--decrypt']

if len(sys.argv) < 8:
  print("[!] You're missing an argument!")
  exit()

crypt = sys.argv[1]
encryptPass = sys.argv[3]
buff = sys.argv[5]
bufferSize = int(buff) * 1024
file = sys.argv[7]

if crypt == '-e' or crypt == '--encrypt':
  try:
    print('Encrypting ' + str(file) + '...')
    pyAesCrypt.encryptFile(str(file), (str(file) + '.aes'), str(encryptPass), bufferSize)
    print(str(file) + " encrypted!")
    erase = input("Do you want to erase original?(can't be undone)[y/N]: ")
    if erase.lower() == 'y':
      os.system('sudo shred -f ' + str(file) + ' && sudo rm ' + str(file))
  except:
    print(str(file) + " failed to encrypt!")

if crypt == '-d' or crypt == '--decrypt':
  try:
    print('Decrypting ' + str(file) + '...')
    pyAesCrypt.decryptFile(str(file), "dataout.txt", str(encryptPass), bufferSize)
    print(str(file) + " decrypted!")
    erase = input("Do you want to erase encrypted file?(can't be undone)[y/N]: ")
    if erase.lower() == 'y':
      os.system('sudo shred -f ' + str(file) + ' && sudo rm ' + str(file))
  except:
    print(str(file) + " failed to decrypt!")
