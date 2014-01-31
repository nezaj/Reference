# Chapter Two: Making Recommendations

**Collaborative filtering**
> A collaborative filtering algortihm usually works by searching a large group of people and finding a smaller set with tastes similar to yours. It looks at other things they like and combines them to create a ranked list of suggestions. There are several different ways of deciding which people are similar and combining their choices to make a list.

### Collecting Preferences
No matter how preferences are expressed, you need a way to map them onto numerical values. For a site where people vote on news stories, values of -1, 0, and 1 could be used to represent "disliked," "didn't vote", and "liked."

Using a dictionary is convenient for experimenting with the algorithims and for illustrative purposes. For veyr large datasets you'll probably want to store preferences in a databse.

### Finding Similar Users
After collecting data about the things people like, you need a way to determine how similar people are in their tastes. You do this by comparing each personw ith every other person and calculating a *similarity score*.

#### Approach 1: Euclidean Distance Score
Calculate distance between user prefences. Similar people will have smaller distances. However, we want these people to have higher rankings. So we will add 1 to the function (to prevent divide by zero) and invert it. For example the distance between user x and y can be calculated like follows
```
1 / (1 + sqrt(pow(x1-y1) + pow(x2-y2) + pow(x3-y3) ... ))
```

#### Approach 2: Pearson Correlation Score
A slightly more sophisticated way to determine the similarity between people's interests is to use a Pearson correlation coefficient. The correlation coefficient is a measure of how well two sets of data fit on a straight line. It tends to give better results in situations where the data isn't well normalized -- for example, if critics' movie rankings are routinely more harsh than average.

One interesting asspect of using the Pearson score is that it corrects for grade inflation. In the case of movie critics, if one critics is inclined to give higher scores than the other, there can still be perfect correlation if the difference between their scores is consistent. The Euclidean distance score described above will say that two critics are dissimilar because one is consistently harsher than the other, even if their tastes are very similar. Depending on your particular application, this behavior may or may not be what you want.

Unlike the euclidean distance metrics, this formula is not very intuitive, but it does tell you how much the variables change together divided by the product of how much they vary individually. Values range between -1 and 1. Scores of .5 and above indicate high positive correlation. A score 0 means that the variables change independently of each other. A score of 1 means that two people have exactly the same ratings for every item.

#### Which to Use?
Which metrics to use depends on your application. There are other metrics as well such as the Jaccard Coefficent and/or Manhattan Distance which can be used as a similarity function as long as they return a float where a higher value means more similar.

#### Ranking Users
Now that you have functions for comparing two people, you can create a function that scores everyone against a given person and finds the closest matches. The closest match would be the user with the highest similarity score with the given person.

### Recommending Items
Score items by producing a weighted score that takes into account the rankings of the critics. Take the votes of all the other critics and multiply how similiar they are to me by the score they gave each movie. Normalize the the total weighted score by dividing it by the total similarity score. This adjusts for movies which have too many or too little reviews.


