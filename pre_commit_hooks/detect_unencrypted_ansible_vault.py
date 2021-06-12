import argparse
from typing import Optional
from typing import Sequence


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    unencrypted_vault_files = []

    for filename in args.filenames:
        with open(filename, 'rb') as f:
            content = f.read()
            if not b'$ANSIBLE_VAULT;' in content:
                unencrypted_vault_files.append(filename)

    if unencrypted_vault_files:
        for unencrypted_vault_file in unencrypted_vault_files:
            print(f'Unencrypted vault found: {unencrypted_vault_file}')
        return 1
    else:
        return 0


if __name__ == '__main__':
    exit(main())
