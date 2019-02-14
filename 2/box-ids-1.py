# AOC-2018 2.1
import logging

# log configutation
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
ch = logging.StreamHandler()
log.addHandler(ch)


def checks(id, count):

    # for each digit in string
    # dict digit:count++
    # when finished, should have key:value pairs for all letters in string, scan this
    # if any letter == 2 AND any letter == 3 return both
    # else if any letter == 2 return two
    # else if any letter == 3 return three
    # else retun neither
    return True


if __name__ == '__main__':
    '''
    '''
    checksum2s = 0
    checksum3s = 0
    twos_set = set()
    threes_set = set()

    with open("input.txt") as content:
        log.info("Loading input")
        for line in content:
            # Read box ID
            # If check2s:
            # Increment checksum2s
            # Add to twos_set
            # If check3s:
            # Increment checksum3s
            # Add to threes_set
            box_id = line
            log.debug("Checking box_id: {0}".format(box_id))

            if checks(box_id, 2) is True:
                log.debug("{0} valid for 2s".format(box_id))
                checksum2s += 1
                twos_set.update(box_id)

    log.info("# check2s {0}.".format(checksum2s))
