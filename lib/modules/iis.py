#!/usr/bin/python

class IIS:

    import re
    
    #Initial Configurations
    numberOfAttacks = 0
    bytes_sent = 0
    returned_2xx = 0
    returned_3xx = 0
    returned_4xx = 0
    returned_5xx = 0
    snaredate = ''
    snarehost = ''
    snarelog = ''
    random = ''
    host = ''
    l = ''
    u = ''
    time = ''
    rMethod = ''
    rURI = ''
    v = ''
    status = ''
    nbytes = ''
    
    
    logFormat = "%snaredate %snarehost %snarelog %random %h %l %u %t \"%r\" %>s %b"
    logFormat = logFormat.split(" ")
    #logKeys = logFormat
    logTable = {
                  '%snaredate' : '(?P<snaredate>\w{3}\s+\d{0,2}\s+\d{2}:\d{2}:\d{2})',
                  '%snarehost' : '(?P<snarehost>\w*)',
                  '%snarelog' : '(?P<snarelog>\w*)',
                  '%random' : '(?P<random>\d)',
                  '%h' : '(?P<host>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
                  '%l' : '(?P<l>[\D|\w])',
                  '%u' : '(?P<u>[\D|\w])',
                  '%t' : '(?P<time>\[\d{2}\/\w*\/\d{4}:\d{2}:\d{2}:\d{2}\s*-\d{4}\])',
                  '"%r"' : '(?P<request>"\w\s*.*")',
                  '%>s' : '(?P<status>\d{3})',
                  '%b' : '(?P<bytes>\d*)'
      }
    exploitTable = [
                    '(.)\1{10}',
                    "'",
                    '\s*or\s*(.)*=\1',
                    'xp_cmdshell',
                    'union\s+select',
                    'file:',
                    'load_file',
                    'out_file',
                    'dump_file',
                    'in_file',
                    '@@version',
                    'version\(\)',
                    '/*',
                    '*/',
                    '--'
                    
    ]
    for x in logFormat:
        logFormat[logFormat.index(x)] = logTable[x]
    
    logFormat = re.compile('\s+'.join(logFormat))
    
    for line in open('/var/log/remote'):
        matches = logFormat.match(line)
        parsedLine = {}
        if matches:
            parsedLine['snaredate']       = matches.group('snaredate')
            parsedLine['snarehost']       = matches.group('snarehost')
            parsedLine['snarelog']        = matches.group('snarelog')
            parsedLine['random']          = matches.group('random')
            parsedLine['host']            = matches.group('host')
            parsedLine['l']               = matches.group('l')
            parsedLine['u']               = matches.group('u')
            parsedLine['time']            = matches.group('time')
            parsedLine['rMethod'],parsedLine['rURI'],parsedLine['v']  = re.split('\s+',matches.group('request'))
            parsedLine['status']          = matches.group('status')
            parsedLine['nBytes']          = matches.group('bytes')
            
        if parsedLine.get('status', '') == '404': print line