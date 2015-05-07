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
