this is a simple wrapper for the s4cmd library which uses pexpect to read the terminal stdout/stderr output and start transcode jobs
based on the results


there are two scripts implemented here:  rectr.py & uptr.py

# uptr.py 

this one is effectively a s4cmd put with the recursive switch and then calling elastic transcoder for each of those files to transcode

# rectr.py

this one uses the s4cmd ls recursive and calls the elastic transcoder for each of those files which match a pattern
