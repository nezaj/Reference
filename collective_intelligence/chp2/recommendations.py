#! /usr/bin/env python
from math import sqrt
from data import critics
from collections import defaultdict

def sim_distance(prefs, person1, person2):
    """
    Returns a similarity score based on euclidean distance between person1 and and person 2
    """
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
    """ Returns a similarity score based on the pearson correlation score """
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

def getRecommendations(prefs, person, similarity=sim_pearson):
    """
    Get recommendations for a person by using a weighted average
    of ever other user's rankings. Only ranks movies that haven't
    already been rated by the person
    """
    totals = defaultdict(lambda: 0)
    simSums = defaultdict(lambda: 0)

    def score_items(sim, other):
        """
        Updates total score and similarity sum for each item that was not reviews by the specified person.
        Weights total score by similarity score.
        """
        for item in prefs[other]:
            # only score movies I haven't seen yet
            if item not in prefs[person] or prefs[person][item] == 0:
                # Similarity * Score
                totals[item] += prefs[other][item] * sim
                # Sum of similarities
                simSums[item] += sim

    for other in prefs:
        # Don't compare me to myself
        if other == person: continue
        sim = similarity(prefs, person, other)

        # ignore scores of 0 or lower
        if sim <= 0: continue
        score_items(sim, other)

    # Create the normalized list
    rankings = [(total / simSums[item], item) for item, total in totals.items()]

    # Return the sorted list
    rankings.sort()
    rankings.reverse()
    return rankings

def topMatches(prefs, person, n=5, similarity=sim_pearson):
    """
    Returns the best matches for person from the prefs dictionary
    Number of results and similarity function are optional params.
    """
    scores=[(similarity(prefs, person, other),other) for other in prefs if other != person]

    # Sort the list so the highest scores appear at the top
    scores.sort(reverse=True)
    return scores[0:n]

if __name__ == "__main__":
    for person in critics:
        recommendations = getRecommendations(critics, person)
        print "Recommendations for {}: {}".format(person, recommendations)
