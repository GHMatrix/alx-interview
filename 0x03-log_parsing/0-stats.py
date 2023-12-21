#!/usr/bin/env python3
"""
Log parsing interview challenge
"""

import sys

def parse_logs():
    """
    Reads logs from standard input and generates reports
    Reports:
        * Prints log size after reading every 10 lines & at KeyboardInterrupt
    Raises:
        KeyboardInterrupt (Exception): handles this exception and raises it
    """
    lineNumber = 0
    fileSize = 0
    statusCodes = {}
    codes = ('200', '301', '400', '401', '403', '404', '405', '500')
    
    try:
        for line in sys.stdin:
            lineNumber += 1
            parts = line.split()

            try:
                fileSize += int(parts[-1])
                if parts[-2] in codes:
                    statusCodes[parts[-2]] = statusCodes.get(parts[-2], 0) + 1
            except (IndexError, ValueError):
                pass
            
            if lineNumber == 10:
                report(fileSize, statusCodes)
                lineNumber = 0

        report(fileSize, statusCodes)
        
    except KeyboardInterrupt:
        report(fileSize, statusCodes)
        raise

def report(fileSize, statusCodes):
    """
    Prints generated report to standard output
    Args:
        fileSize (int): total log size after every 10 successfully read lines
        statusCodes (dict): dictionary of status codes and counts
    """
    print("File size: {}".format(fileSize))
    for key, value in sorted(statusCodes.items()):
        print("{}: {}".format(key, value))

if __name__ == '__main__':
    parse_logs()
