# Regular Expression

### Online Regular Expression Engine
1. [https://regexr.com/](https://regexr.com/)
2. [https://regex101.com/](https://regex101.com/)
3. [https://www.regexpal.com/](https://www.regexpal.com/)

### Metacharacter
* Wildcard Metacharacter
* Escaping Metacharacter
  * dot (\\.)
  * forward slash (\\/)
* Special Characters
  * Spaces
  * Tabs (\t)
  * Line Return (\r, \n, \r\n)

### Character Sets 
* `\d` = [0-9]
* `\w` = [a-zA-Z0-9]
* `\D` = [^0-9]
* `\W` = [^a-zA-Z0-9]
* `\s` = [\r\n\t\f]

### Repetition Metacharacters
1. `*` Zero or more times
2. `+` One or more times
3. `?` Zero or one time

### Quantified Repetition
1. `\d{0,}` is same as `\d*`
2. `\d{1,}` is same as `\d+`
3. `\d{3}-\d{3}-\d{4}` matches most US phone numbers
4. `/^(\+88)?01[76598]\d{8}$/g` matches most Bangladeshi mobile phone numbers

### Greedy expression vs Lazy expression

* [https://javascript.info/regexp-greedy-and-lazy](https://javascript.info/regexp-greedy-and-lazy)
* [https://medium.com/@318097/greedy-lazy-match-in-regular-expression-35ce8eca4060](https://medium.com/@318097/greedy-lazy-match-in-regular-expression-35ce8eca4060)
