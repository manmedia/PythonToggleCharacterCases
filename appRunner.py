#
# Runner
#


import switchLetterCase

args = switchLetterCase.get_parsed_args();
print(type(args))
switchLetterCase.process_files(args);
