# iHeartRadio-Assessment

This uses mongoDB, so to get this to work:

1. Have an instance of mongod running
2. Have copies of artists.tsv, users.tsv, listens.tsv in the same directory as the python scripts
3. Type this into the shell in that directory:

```
mongoimport --db iHeartAssessment --collection artists --type tsv --headerline --file artists.tsv
mongoimport --db iHeartAssessment --collection users --type tsv --headerline --file users.tsv
mongoimport --db iHeartAssessment --collection listens --type tsv --headerline --file listens.tsv
```


Question 3 uses pandas instead of mongoDB, so all that is needed to run it is to have the TSVs in the same directory. My code will plot either gender or age, but not both at the same time. To switch between the two, uncomment/comment the correct blocks of code in assessmentQ3-pandas.py.
