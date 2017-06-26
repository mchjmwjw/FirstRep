1. ```min(arg1, arg2[, arg3, ...][, key])```
    * 返回最小值
    * key : 指定规则key=func,如key=len

2. ```map(function, iterable, ...)```
    * Apply function to every item of iterable and return a list of the results. 
    * ```map(len, ['abc', 'asdfg', 'bn')```

3. ```ord(c)```
    * 字符转为ASCII码
    * c: 长度为1的字符串

4. ```str.isalpha()```
    * 判断字符串中是否都是字母

5. ```zip([iterable, ...])```
    * This function returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
    * ```
        >>> x = [1, 2, 3]
        >>> y = [4, 5, 6]
        >>> zipped = zip(x, y)
        >>> zipped
            [(1, 4), (2, 5), (3, 6)]
        >>> x2, y2 = zip(*zipped)
        >>> x == list(x2) and y == list(y2)
            True

6. ```string.ascii_lowercase```
    * 26个小写字母的字符串
    * 需要导入 string 模块

7. ```class type(object)```
    * With one argument, return the type of an object. The return value is a type object. 
    * The ```isinstance()``` built-in function is recommended for testing the type of an object.
    
8. ```str.lower()```
9. ```str.translate(table[, deletechars])```
    * ```
        >>> 'read this short text'.translate(None, 'aeiou')
            'rd ths shrt txt'

10. pylint 命名规范
``` 
variable-rgx:
[a-z_][a-z0-9_]{2,30}$

const-rgx:
(([A-Z_][A-Z0-9_]*)|(__.*__))$