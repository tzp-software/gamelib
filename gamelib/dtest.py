import os
if os.environ.get('DEBUG') or __debug__:
    print 'DEBUG MODE'
else:
    pass

