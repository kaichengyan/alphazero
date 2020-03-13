import logging
import os
import sys


def setup_logger(log_dir, filename):
    FORMAT = '%(asctime)s - %(name)-15s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO,
                        format=FORMAT,
                        datefmt='%Y/%m/%d %H:%M:%S',
                        handlers=[logging.FileHandler(os.path.join(log_dir, filename), 'w+'),
                                  logging.StreamHandler(sys.stderr)]
                        )
    logging.getLogger('ignite.engine.engine.Engine').setLevel(logging.WARNING)
