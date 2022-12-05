"""Top-level package for dsdz."""

from collections import Counter

__author__ = """Fábio P. Fortkamp"""
__email__ = 'fabio@fabiofortkamp.com'
__version__ = '0.1.0'


def number_of_friends(user: dict) -> int:
    """Return how many friends `user` has"""
    return len(user["friends"])


def not_the_same(user: dict, other_user: dict) -> bool:
    """Return whether the IDs of the given users are different"""
    return user["id"] != other_user["id"]


def not_friends(user: dict, other_user: dict) -> bool:
    """Return whether there is no connection betwen given users"""
    return all(
        not_the_same(friend, other_user)
        for friend in user["friends"]
    )


def friends_of_friend_ids(user: dict) -> Counter:
    """Return a counter of how many friens in commom `user` has with its friends"""
    return Counter(
        foaf["id"]
        for friend in user["friends"]
        for foaf in friend["friends"]
        if not_the_same(user, foaf)
        and not_friends(user, foaf)
    )
