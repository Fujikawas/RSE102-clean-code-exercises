# This code allows you to store information on people owing you money
# and then list all those people in a ordered and formatted way in the terminal.
# Try to improve the `payday` function by splitting the logic into smaller functions.

from dataclasses import dataclass
from typing import Iterable


@dataclass
class Debtor:
    """Stores the information on a person owing us money"""

    name: str
    debt: float


def payday(debtors: Iterable[Debtor]) -> None:
    ordered = _sort_debtors(debtors)
    _print_debtors(ordered)


# sort the debtors according to their debt amount,higher amount appear earlier
def _sort_debtors(debtors: Iterable[Debtor]) -> Iterable[Debtor]:
    ordered = reversed(sorted(debtors, key=lambda debtor: debtor.debt))
    return ordered


def _print_debtors(debtors: Iterable[Debtor]) -> None:
    for debtor in debtors:
        if debtor.debt > 100.0:
            _print_debtor_with_exclamation(debtor)
        else:
            _print_debtor(debtor)


def _print_debtor_with_exclamation(debtor: Debtor) -> None:
    print(f"{debtor.name}: !!!{debtor.debt}!!!")


def _print_debtor(debtor: Debtor) -> None:
    print(f"{debtor.name}: {debtor.debt}")


if __name__ == "__main__":
    payday(
        [
            Debtor("Person1", 100.0),
            Debtor("Person2", 200.0),
            Debtor("Person3", 10.0),
            Debtor("Person4", 50.0),
            Debtor("Person5", 1250.0),
        ]
    )
