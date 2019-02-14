# AOC-2018 1.1 1.2
import logging
import time

# log configutation
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
ch = logging.StreamHandler()
log.addHandler(ch)

if __name__ == '__main__':
    '''
    '''
    starttime = time.time()
    frequency = 0
    loops = 0

    with open("input.txt") as content:
        log.info("Loading input, frequency currently {0}".format(frequency))
        for line in content:
            loops+=1
            # Current frequency  0, change of +1; resulting frequency  1.
            log.debug("Current frequency {0}, change of {1}; resulting frequency {2}".format(frequency, int(line), frequency + int(line)))
            frequency = frequency + int(line)

    endtime = time.time()
    log.info("Finished with final frequency {0}.".format(frequency))
    log.info("Time taken: {0}".format(endtime-starttime))
    log.info("Loops: {0}".format(loops))