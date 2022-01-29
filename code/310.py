from typing import Union

def func(num: Union[int, float]) -> bool:
    if num + 10 > 100:
        return True

    return False

def func(num: int | float) -> bool:
    if num + 10 > 100:
        return True

    return False

# https://benhoyt.com/writings/python-pattern-matching/
parser = argparse.ArgumentParser()
parser.add_argument('command', choices=['push', 'pull', 'commit'])
args = parser.parse_args()

match args.command:
    case 'push':
        print('pushing')
    case 'pull':
        print('pulling')
    case _:
        parser.error(f'{args.command!r} not yet implemented')
