import re

def get_vars(conf_file):
    line_sub = re.compile('\s+|"|\[|\]')
    temp = [None]*2
    vars_hash = {}
    
    try:
        f = open(conf_file)
    except IOError as e:
        print "There was an error opening the file: " + e
    
    for line in f:
        if re.match('^[#|;]',line):
            pass
        elif re.match('^$',line):
            pass
        else:
            temp[0],temp[1] = line.rstrip('\r\n').split('=')
            for t in temp:
                t = re.sub(line_sub, "", t)
            vars_hash[temp[0]] = temp[1]
    return vars_hash

print get_vars('/home/dev/projects/rubywatch/rubywatch/lib/config/rubywatch.conf')