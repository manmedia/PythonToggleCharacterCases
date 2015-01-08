#
# A module capable of changing alphabet letter cases.
#
# It uses very generic Python functionality to ensure
# backward compatibility.
#
#
# The programme processes a set of characters by default
# If no character is entered for processing, the programme
# simply exists. This can be turned off by setting 'a' to 1
# (for all vowels) or 2 (for all consonants).
# 
#
#

import os;
import sys;
import re;
import string;
from re import sub;


#
#! Get parsed arguments
#
def get_parsed_args():
        
    # Pre-allocate
    parser = "";
    args = "";
    if sys.version_info < (2,7):
        from optparse import OptionParser
        parser = OptionParser();
        parser.add_option("-i", "--input_path", type=str, help="Input file path with extension");
        parser.add_option("-o", "--output_path", type=str, help="Output file path with extension");
        parser.add_option("-a", "--all_chars", type=int, help="Switch a type of characters (all vowels or cons.), disable=0, vowel=1, cons=2", default=0);
        parser.add_option("-c", "--c", type=str, help="Characters to process (comma-separated list, no whitespace)", default="");

    else:
        from argparse import ArgumentParser
        parser = ArgumentParser();
        parser.add_argument("-i", "--input_path", type=str, help="Input file path with extension");
        parser.add_argument("-o", "--output_path", type=str, help="Output file path with extension");
        parser.add_argument("-a", "--all_chars", type=int, help="Switch a type of characters (all vowels or cons.), disable=0, vowel=1, cons=2", default=0);
        parser.add_argument("-c", "--c", type=str, help="Characters to process (comma-separated list, no whitespace)", default="");
    
    args = parser.parse_args();
    args = vars(args);

    ##print(option)
    ##print(args)
    ##print(type(option))
    ##print(option.c)
    ##print(option.all_chars)
    ##print(option.input_path)
    ##print(option.output_path)

    # Safety assertions
    assert (args['all_chars'] >= 0 and args['all_chars'] <= 2), \
           "Invalid value! programme exiting!\n type python switchLetterCase.py -h for information on arguments"

    # If nothing to process, programme will exit
    if (args['all_chars'] == 0) and \
       ((args['c'] == "") or \
        (args['c'] == " ") or \
        args['all_chars'] is None or \
        all([x is ',' for x in args['c']])):
        
        print(".....Nothing to process, programme exiting.\n\n");
        sys.exit(0);

    return args;


#
#! Main processor function
#

def process_files(args):

    
    try:
        # Get handlers
        f1 = open(args['input_path'], 'r')
        f2 = open(args['output_path'], 'w');

        # Initial setup
        line_to_write = ""       
        if (args['all_chars'] == 0):    # process characters in the list

            gg = "".join(args['c'])

            for line in f1:
                g = [y.upper() if y in gg else y.lower() if y.upper() in gg else y for y in line];
                line_to_write = "".join(g);
                f2.write(line_to_write);

        elif (args['all_chars'] == 1):    # process vowels only

            vowels = sub('[^aeiou]+','',string.ascii_lowercase)

            for line in f1:
                g = [y.upper() if y in vowels else y.lower() if y.upper() in vowels else y for y in line];
                line_to_write = "".join(g);
                f2.write(line_to_write);       

        elif (args['all_chars'] == 0):    # process consonants in the list

            consonants = sub('[aeiou]+','',string.ascii_lowercase)

            for line in f1:
                g = [y.upper() if y in gg else y.lower() if y.upper() in gg else y for y in line];
                line_to_write = "".join(g);
                f2.write(line_to_write);

        # Print some INFO    
        print("All characters toggled! Terminating programme......\n\n");

        f1.close();
        f2.close();
          
    except (Exception, BaseException, IOError, ValueError, WindowsError) as e:        
        print(e);

    finally:
        del f1, f2

