# Chapter Two: Making Recommendations

**Collaborative filtering**
> A collaborative filtering algortihm usually works by searching a large group of people and finding a smaller set with tastes similar to yours. It looks at other things they like and combines them to create a ranked list of suggestions. There are several different ways of deciding which people are similar and combining their choices to make a list.

### Collecting Preferences
No matter how prefeences are expressed, you need a way to map them onto numerical values. For a site where people vote on news stories, values of -1, 0, and 1 could be used to represent "disliked," "didn't vote", and "liked."

Using a dictionary is convenient for experimenting with the algorithims and for illustrative purposes. For veyr large datasets you'll probably want to store preferences in a databse.

### Finding Similar Users
After collecting data about the things people like, you need a way to determine how similar people are in their tastes. You do this by comparing each personw ith every other person and calculating a *similarity score*.

#### Approach 1: Euclidean Distance Score
Calculate distance between user prefences. Similar people will have smaller distances. However, we want these people to have higher rankings. So we will add 1 to the function (to prevent divide by zero) and invert it. For example the distance between user x and y can be calculated like follows
```
1 / (1 + sqrt(pow(x1-y1) + pow(x2-y2) + pow(x3-y3) ... ))
```

