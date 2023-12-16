# FileIO [CS50 - Week 6]

- Let's play Mobile Legend ...... data!

### Task 1
- Ask user input for hero name and role.
- Write the data into text file (.txt).
- Everytime we run the program and add user input , we would like to add data as new line to that txt file.

### Task 2
- By using these dictionary values, you need to create csv file.

```python
data1 = {'hero_name': 'Terizla', 'role' : 'fighter', 'release_year' : 2019}

data2 = {'hero_name': 'Martis', 'role' : 'fighter', 'release_year' : 2018}

data3 = {'hero_name': 'Grock', 'role' : 'tank', 'release_year' : 2017}

data4 = {'hero_name': 'Carmilla', 'role' : 'support', 'release_year' : 2020}

data5 = {'hero_name': 'Irithel', 'role' : 'marksman', 'release_year' : 2017}
```

### Task 3
- By using mlbb_hero.csv [file](./data/mlbb_hero.csv), find the the highest damage hero.
- And also find the hero with maximum win rate.
- If you found multiple hero with same value , you can take the first hero (or) select hero that you like.
- Hint : More easy if read as dictionary. Select column value and compare row by row.