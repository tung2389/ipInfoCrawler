```bash
grep '^A' scrawledHost.log
grep '*A*' scrawledHost.log
grep 'A' scrawledHost.log
grep 'AS' scrawledHost.log

grep 'AS[0-9]*' scrawledHost.log
grep -o 'AS[0-9]*' scrawledHost.log
grep -o 'AS[0-9]*' scrawledHost.log | uniq -cd
grep -o 'AS[0-9]*' scrawledHost.log

uniq
tldr uniq
tldr sort

grep -o 'AS[0-9]*' scrawledHost.log | sort -u
tldr tr
grep -o 'AS[0-9]*' newHost.log >> scrawledASN.log
cat scrawledASN.log | sort -u
```