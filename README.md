# ida2md
IDA format to the markdown table conversion using python

# Example

Input:

```
Address	Ordinal-Name	Library
0000000180078F18		AccessCheck	api-ms-win-security-base-l1-1-0
0000000180078A28		ActivateActCtx	api-ms-win-core-sidebyside-l1-1-0
0000000180077750		AddConsoleAliasA	api-ms-win-core-console-l3-2-0
...
```

Output (Markdown table style):

```
|Address|Ordinal-Name|Library|
|----|----|----|
|180078F18|AccessCheck|api-ms-win-security-base-l1-1-0|
|180078A28|ActivateActCtx|api-ms-win-core-sidebyside-l1-1-0|
|180077750|AddConsoleAliasA|api-ms-win-core-console-l3-2-0|
...
```
