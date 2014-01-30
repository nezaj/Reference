#! /usr/bin/env python
from math import sqrt

# Returns a distance-based simiarity score for person1 and person2
def sim_distance(prefs, person1, person2):
    # Get the list of shared_items
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    # if they have no ratings in common, return 0
    if len(si) == 0: return 0

    # Add up the squares of all the differences
    p1_prefs = prefs[person1]
    p2_prefs = prefs[person2]
    sum_of_squares = sum([pow(p1_prefs[item] - p2_prefs[item],2) for item in si])

    return (1 / (1 + sqrt(sum_of_squares)))

def sim_pearson(prefs, p1, p2):
    # Get the list of shared_items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    # Find the number of elements
    n = len(si)

    # if they have no ratings in common, return 0
    if n == 0: return 0

    # Add up all preferences
    sum1 = sum([prefs[p1][i] for i in si])
    sum2 = sum([prefs[p2][i] for i in si])

    # Sum up the squares
    sum1Sq = sum([pow(prefs[p1][i],2) for i in si])
    sum2Sq = sum([pow(prefs[p2][i],2) for i in si])

    # Sum up the products
    pSum = sum([prefs[p1][i] * prefs[p2][i] for i in si])

    # Calculate Pearson score
    num = pSum - ((sum1 * sum2) / n)
    den = sqrt((sum1Sq - (pow(sum1,2)) / n) * (sum2Sq - (pow(sum2,2)) / n))

    if den == 0: return 0
    r = num/den

    return r

# A dictionary of movie critics and their ratings of a small set of movies
critics = {
    'Lisa Rose': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.5,
        'Just My  Luck': 3.0,
        'Superman Returns': 3.5,
        'You, Me and Dupree': 2.5,
        'The Night Listener': 3.0
    },
    'Gene Seymour': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 3.5,
        'Just My  Luck': 1.5,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.5,
        'The Night Listener': 3.0
    },
    'Michael Phillips': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.0,
        'Superman Returns': 4.0,
        'The Night Listener': 3.0
    },
    'Mick Lasalle': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Just My  Luck': 2.0,
        'Superman Returns': 3.0,
        'You, Me and Dupree': 2.0,
        'The Night Listener': 3.0
    },
    'Jack Matthews': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.5,
        'The Night Listener': 3.0
    },
    'Toby': {
        'Snakes on a Plane': 4.5,
        'Superman Returns': 4.0,
        'You, Me and Dupree': 1.0
    },
}
