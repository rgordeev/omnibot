# coding: utf-8
import logging
import os
from datetime import date

import omnibot

# application base dir
# base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)
base_path = os.path.dirname(os.path.abspath(__file__))

# logging config
log_format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s] %(message)s'

# Configure logging here
# == start
logging.basicConfig(
    format=log_format,
    filename=os.path.join(base_path, '%s.log' % str(date.today())),
    level=logging.INFO)
# == end

if __name__ == '__main__':
    omnibot.publish()
