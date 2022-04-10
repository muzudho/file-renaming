# file-renaming

ファイル名の一括変更

# Run

```shell
python main.py
```

# How to use

```plaintext
python main.py
Which directory?
Example: .
.
Current directory: C:\Users\むずでょ\Documents\GitHub\file-renaming

Files
-----
example-1-a.txt
LICENSE
main.py
README.md

Are you sure this is the right directory (y/n)?
y

Please enter a regular expression pattern.
Example: ^example-([\d\w]+)-([\d\w]+).txt$
^example-([\d\w]+)-([\d\w]+).txt$

Numbering
---------
(1) example-1-a.txt \1=[1] \2=[a]
( ) LICENSE
( ) main.py
( ) README.md

Was there a match (y/n)?
y

Enter the pattern after the conversion.
Example: example-\2-\1.txt
example-\2-\1.txt

Simulation
----------
(1) example-1-a.txt --> example-a-1.txt

Do you want to run it (y/n)?
y

Result
------
(0)Rename C:\Users\むずでょ\Documents\GitHub\file-renaming\example-1-a.txt --> C:\Users\むずでょ\Documents\GitHub\file-renaming\example-a-1.txt
```

# Case study

## Case 1

例えばファイル名を以下のように付けているとする。  

```plaintext
201612050853.png
201612050853b.png
```

これを以下のように変形したい。  

```plaintext
201612__math__05-0853.png
201612__math__05-0853-b.png
```

ならば正規表現は以下のようにする。  

```plaintext
# Before:
^(\d{6})(\d{2})(\d{4})([\d\w]*).png$

# After:
\1__math__\2-\3-\4.png
```

## Case 2


例えばファイル名を以下のように付けているとする。  

```plaintext
20170429.png
20170429a1.png
```

これを以下のように変形したい。  

```plaintext
201704__shogi__29-.png
201704__shogi__29-a1.png
```

ならば正規表現は以下のようにする。  

```plaintext
# Before:
^(\d{6})(\d{2})([\d\w]*).png$

# After:
\1__math__\2-\3.png
```

## Case 3

例えばファイル名を以下のように付けているとする。  

```plaintext
201612030331_1.png
201612030331_10b.png
```

これを以下のように変形したい。  

```plaintext
201612__etc__03-0331_1.png
201612__etc__03-0331_10b.png
```

ならば正規表現は以下のようにする。  

```plaintext
# Before:
^(\d{6})(\d{2})(\d{4})_([\d\w]*).png$

# After:
\1__math__\2-\3-\4.png
```

## Case 4

例えばファイル名を以下のように付けているとする。  

```plaintext
20171205a41a_do00.png
20171205a41b_dos00.png
```

これを以下のように変形したい。  

```plaintext
201712__music-01完全１度__05-a41a_do00.png
201712__music-01完全１度__05-a41b_dos00.png
```

ならば正規表現は以下のようにする。  

```plaintext
# Before:
^(\d{6})(\d{2})([^\.]*).png$

# After:
\1__music-01完全１度__\2-\3.png
```

## Case 5

例えばファイル名を以下のように付けているとする。  

```plaintext
img13.png
img13b13c1.png
```

これを以下のように変形したい。  

```plaintext
201712__shogi-wcsc27-pr1__13.png
201712__shogi-wcsc27-pr1__13b13c1.png
```

ならば正規表現は以下のようにする。  

```plaintext
# Before:
^img([^\.]*).png$

# After:
201712__shogi-wcsc27-pr1__\1.png
```
