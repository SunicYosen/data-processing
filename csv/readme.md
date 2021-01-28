# Programming Sample Instructions

Calculate signals and returns for a simple intra-day momentum strategy.  For example, using two moving averages, signal to go long (1) when the faster average is larger than the slower, or signal to go short (-1) when the faster average is less than the slower.

## Usage

```
usage: main.py [-h] [--data DATA] [--outfile OUTFILE] [--mysql_host MYSQL_HOST] [--mysql_user MYSQL_USER] [--mysql_passwd MYSQL_PASSWD] [--mysql_database MYSQL_DATABASE] [--mysql_table MYSQL_TABLE]
```

Using libraries:

- pandas
- datetime