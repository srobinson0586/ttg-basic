#!/bin/python
# Python Lists Tuples And Sets - Pytest Suite
import application
import base64

enc_list1 = [b'YQ==', b'Tg==', b'eg==', b'Qw==', b'aA==', b'Vw==', b'bw==', b'RA==', b'cQ==', b'Rw==']
enc_list2 = [b'Tg==', b'Qw==', b'Vw==', b'RA==', b'Rw==']

def lists_tuples_and_sets():
    # lists
    dec_list1 = [base64.b64decode(x) for x in enc_list1]
    dec_list2 = [base64.b64decode(x) for x in enc_list2]
    first = application.lists_splice_odds(dec_list1)
    assert first == dec_list2, "list_splice_odds(); Incorrect return value"
    assert type(first) == list, "lists_splice_odds(); Incorrect return type"
    print('[+] list_splice_odds Test PASSED')

    # sets
    dec_set1 = set(dec_list1)
    dec_set2 = set(dec_list2)
    second = application.sets_intersect_sets(dec_set1,  dec_set2)
    assert second == dec_set2, "sets_intersect_sets(); Incorrect return value"
    assert type(second) == set, "sets_intersect_sets(); Incorrect return type"
    print('[+] sets_intersect_sets Test PASSED')

    # tuples
    dec_tuple = tuple(dec_list2[:4])
    third = application.tuples_ret_all(dec_tuple[0], dec_tuple[1], dec_tuple[2], dec_tuple[3])
    assert third == dec_tuple, "tuples_ret_all(); Incorrect return value"
    assert type(third) == tuple, "tuples_ret_all(); Incorrect return value"
    print('[+] tuples_ret_all Test PASSED')

def test_lists_tuples_and_sets():
    try:
        lists_tuples_and_sets()
    except AssertionError as e:
        print(f"[-] Test FAILED: '{e}'")
        exit()

    print("[+] ALL TESTS PASSED!\n")

# for use without pytest
test_lists_tuples_and_sets()
