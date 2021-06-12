import pytest

from pre_commit_hooks.detect_unencrypted_ansible_vault import main

# Input, expected return value
TESTS = (
    (b'$ANSIBLE_VAULT;', 0),
    (b'$ANSIBLE_VAULT;1.2;AES256;dev', 0),
    (b'', 1),
)


@pytest.mark.parametrize(('input_s', 'expected_retval'), TESTS)
def test_main(input_s, expected_retval, tmpdir):
    path = tmpdir.join('file.txt')
    path.write_binary(input_s)
    assert main([str(path)]) == expected_retval
