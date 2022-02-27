#!/usr/bin/env python3
import tarfile
import os.path

def tar_archive(output_filename, source_dir, compression_type):
    with tarfile.open(output_filename, f'w:{compression_type}') as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


source_dir = input('please enter the path of folder to archive: ')
output_filename = input('please enter the output filename: ')
to_be_compressed = input('Do you want the archive to be compressed, reply Y/N: ')

while to_be_compressed not in ['Y', 'N' ,'y', 'n']:
    to_be_compressed = input('Please enter a valid reply, either Y/N: ')
if to_be_compressed == 'Y':
    compression_type = input("please enter the type of compression, list includes gz, bz2, xz: ")
    tar_archive(output_filename,source_dir,compression_type )
