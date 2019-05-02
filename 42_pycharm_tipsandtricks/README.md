# 42 PyCharm Tips & Tricks

- this repo: https://github.com/pauleveritt/42-workshop
- replay this presentation: https://www.jetbrains.com/pycharm/guide/playlists/42/


## Presentation with verbal notes

I tried to get most of the verbal only info here.

Presentation lacked a lot of cues to make it easy to understand. 


1. Find Action: SHIFT+CMD+a
  - "speed typing": basically tokenized real-time word search
2. 
3. Tabs
  - tabs are a drain on your brain, turn them off
  - "I'm going to tell you where you can put your tabs..."
4. Navigation Bar
  - Turn that off...
5. Recent Files & Tools (terminal etc.): CMD+E 
  - misnamed, it's recent files and tools
  - actually named "Recent Files"
  - Number one way to move around
6. Navigate to Symbol: CMD+OPT+O
  - Find all window, 
7. Navigate by file: CMD+SHIFT+O
  - indexing also indexes dependencies so you can search them
8. Navigate cursor forward and backward: CMD+{ and CMD+}
9. Activate Navigation Bar: OPT+UP
10. Navigate files with navigation bar: left, up, down  
  - Can access the entire project directory structure
  - "speed search": can use it here - press `down`
  - make a new file, too left, up, CMD+n
11. probably in 10
12. probably in 10
13. probably in 10
14. Navbar activate, SHIFT-CMD-F
15. Add a line before and after: `SHIFT-Return` 
  - note: vim mode: use `o` or `shift-o` in ed mode...
16. Make and Extend a selection using keyboard: `OPT+up`
  - note: another easy vim thing: visual mode
  - repeat to select more and more, not sure their rules for increased select area, something like word, line, code block, page... or something
17. Reformat code: something like CTL+OPT+L
  - follows preferences in your settings
18. Optimize Imports: CTL+ALT+O
19. Record in requirements: ALT+ENTER
20. Let IDE add construtor arguments: `ALT+ENTER`
  - mostly for `self` in `__init__`?
21. _
22. _
23. Right click an import, `refactor->rename`
  - undo will undo the whole transaction including all references to that import
  - can do with most any reference to a symbol, does not work on strings
24. _
25. Quick Documentation:  _
26. View Parameter Info: CMD+P when highlighting the parentheses of an argument list
  - 
27. Run from keyboard
28. Conditional Breakpoints: right click the breakpoint to set the condition
  - Stop on a breakpoint only when the customer is larry... 
29. Evaluate Expression During Debugging
30. Split screen without tabs - find action`->'sp ver' or `split vertic' (or whatever "speed typing" search)
  - ALT+TAB to go to next pane
31. Run Single Test: right click in a test or in the gutter to only run one test
  - turn on `AUTOTEST` which will repeat tests every N seconds... also set your AUTOTEST DELAY to change interval
32. See visual code coverage in IDE
  - after running you will get a window showing code coverage details
  - if you add a `.coveragerc` you can exclude your virtualenv or other vendor files
33. *LOCAL HISTORY*: Find Action: show history
  - "Wake up for this one!"
  - tracks every editor and ide transaction and keep per-transaction revision per file
  - sort of random access to history rather than linear like undo/redo
34. _
35. _
36. Put a new project under version control
  - Only enabled when in a project not under version control
37. Reword commit message: `CMD+9` to get to version control, right click commit, choose `reword`
38. Undo Commit: in `version control area`, right click, undo commit
  - make a change list or put in default change list (sounds like a git stash)
39. Only commit some changes
  - ehh figure it out from `version control area` if you don't want to use git CLI
40. Run npm scripts from `package.json`: right click on the line left bar and run
41. Wrap selection with tag: alt-up to mark selection, right click, surround with, then write tag...
  - surround with ??? - `div.columns` - shorthand notation for generating large chunks of html
42. Drag a sqlite database onto the database tab to create a connection
  - then you can autocomplete on sql and your configured table and column names
  - if you rename a column in the sql tab, pycharm will refactor your python code to match

