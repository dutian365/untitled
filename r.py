#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

import execjs
"""
FUNCTIONS
    compile(pattern, flags=0)
        Compile a regular expression pattern, returning a pattern object.

    escape(pattern)
        Escape all the characters in pattern except ASCII letters, numbers and '_'.

    findall(pattern, string, flags=0)
        Return a list of all non-overlapping matches in the string.

        If one or more capturing groups are present in the pattern, return
        a list of groups; this will be a list of tuples if the pattern
        has more than one group.

        Empty matches are included in the result.

    finditer(pattern, string, flags=0)
        Return an iterator over all non-overlapping matches in the
        string.  For each match, the iterator returns a match object.

        Empty matches are included in the result.

    fullmatch(pattern, string, flags=0)
        Try to apply the pattern to all of the string, returning
        a match object, or None if no match was found.

    match(pattern, string, flags=0)
        Try to apply the pattern at the start of the string, returning
        a match object, or None if no match was found.

    purge()
        Clear the regular expression caches

    search(pattern, string, flags=0)
        Scan through string looking for a match to the pattern, returning
        a match object, or None if no match was found.

    split(pattern, string, maxsplit=0, flags=0)
        Split the source string by the occurrences of the pattern,
        returning a list containing the resulting substrings.  If
        capturing parentheses are used in pattern, then the text of all
        groups in the pattern are also returned as part of the resulting
        list.  If maxsplit is nonzero, at most maxsplit splits occur,
        and the remainder of the string is returned as the final element
        of the list.

    sub(pattern, repl, string, count=0, flags=0)
        Return the string obtained by replacing the leftmost
        non-overlapping occurrences of the pattern in string by the
        replacement repl.  repl can be either a string or a callable;
        if a string, backslash escapes in it are processed.  If it is
        a callable, it's passed the match object and must return
        a replacement string to be used.

    subn(pattern, repl, string, count=0, flags=0)
        Return a 2-tuple containing (new_string, number).
        new_string is the string obtained by replacing the leftmost
        non-overlapping occurrences of the pattern in the source
        string by the replacement repl.  number is the number of
        substitutions that were made. repl can be either a string or a
        callable; if a string, backslash escapes in it are processed.
        If it is a callable, it's passed the match object and must

        return a replacement string to be used.

    template(pattern, flags=0)
        Compile a template pattern, returning a pattern object
        """
s = re.compile(r'\d')
print(s.match('111  ddsss  111'))
