# AOC-2018 2.1
import logging

# log configutation
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
ch = logging.StreamHandler()
log.addHandler(ch)


def checks(string, count):

    char_dict = {}
    # for each char in string, add to set / increment 1
    # when finished, should have key:value pairs for all letters in string, scan this
    for char in string[:len(string) - 1]:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
        log.debug("char_dict: {0}".format(char_dict))

    # check list, if any value == count
    for char in char_dict:
        if char_dict[char] == count:
            return True

    # else return false
    return False


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
                log.info("{0} valid for 2s".format(box_id))
                checksum2s += 1
                twos_set.update(box_id)

            if checks(box_id, 3) is True:
                log.info("{0} valid for 3s".format(box_id))
                checksum3s += 1
                twos_set.update(box_id)

    log.info("# check2s {0}.".format(checksum2s))
    log.info("# check3s {0}.".format(checksum3s))

    checksum = checksum2s*checksum3s
    log.info("Checksum: {0}".format(checksum))