## Student Information
- **Name:** Brycen Anderson
- **Student ID:** 111017061
- **Class:** CSCI 3751-001
- **Homework #:** HW2
- **Due Date:** september 26, 2026

---

# Problem 1
    I believe strong fundamentals are the most 8important part of becoming a good computer scientist. Technology will continue to evolve, and understanding the basics gives us a foundation for learning new concepts. When someone plagiarizes code or presents another person's ideas as their own, they skip the practice that builds that foundation. They might finish an assignment, but they can struggle later when a harder problem requires understanding what they skipped. 

    online information and publicly available code can still be useful learning resources. I think the important distinction is whether I am using a resource to understand something or simply copying it to avoid doing the work. To maintain academic integrity, I should credit the sources I use, follow the assignment's rules, and make sure I can explain my own solution.

    Working through problems includes making mistakes and occasionally failing. Those experiences help me recognize problems and understand how to fix them. Protecting my integrity means being honest about my work while developing the skills that work is supposed to demonstrate. 

# Problem 2
    I think AI has useful applications, especially outside of school. It can help automate repetitive tasks and support people who already understand the work they are doing. I do not think they should be used to complete schoolwork because education is where people need to build their own understanding. 
    
    my main concern is that AI can do the thinking a student needs to practice. Learning something unfamiliar can be uncomfortable. It takes time to struggle with a problem, make mistakes, and figure out why an approach does not work. In my experience, that friction is an important part of learning. Receiving an answer immediately can remove the opportunity to develop those skills 
    
    some people argue that AI allows students to move on the harder problems. I understand that argument, but harder problems still depend on fundamental. if someone relies on AI for the basics, they may be unable to explain, evaluate, or fix the solution it produces. Moving ahead does not necessarily mean they are prepared for what come next. 

    someone who has worked through a problem repeatedly may recognize it quickly when it appears again. they have experience with both the solution and the mistakes that lead away from it. someone who consistently lets AI solve the problem may miss that experience , even if their finished work looks correct. 
    
    for me, the purpose of school is to develop the ability to think and solve problems independently. AI may be valuable in the workplace, but students first need the knowledge to judge its output. Building that foundation should come before relying on automation. 

# Problem 3
```bash
    [bryruto@Brycen-archlinux hw2]$  grep -oE '[a-zA-Z]+' Lincoln.txt | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -nr | head -n 5
     13 that
     11 the
     10 we
      8 to
      8 here
    [bryruto@Brycen-archlinux hw2]$  grep -oE '[a-zA-Z]+' Kennedy.txt | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -nr | head -n 3
     33 the
     24 of
     22 to
```

# Problem 4
```bash
[bryruto@Brycen-archlinux hw2]$ sort Kennedy.txt > Kennedy.txt
[bryruto@Brycen-archlinux hw2]$ cat Kennedy.txt
```

## No data in the Kennedy.txt anymore
    cat kennedy.txt had no data anymore 

```bash
[bryruto@Brycen-archlinux hw2]$ ls
kennedy  Kennedy.txt  King.txt  Lincoln.txt  problem1.md
[bryruto@Brycen-archlinux hw2]$ rm kennedy 
[bryruto@Brycen-archlinux hw2]$ ls
Kennedy.txt  King.txt  Lincoln.txt  problem1.md
[bryruto@Brycen-archlinux hw2]$ cat King.txt
[bryruto@Brycen-archlinux hw2]$ sort -o King.txt King.txt
[bryruto@Brycen-archlinux hw2]$ cat King.txt
data data data it was a lot
```
## results
    sort Kennedy.txt > Kennedy.txt made Kennedy empty
    
    fix-> sort -o King.txt King.txt this still had data in King after  



# Problem 5

```bash
#!/bin/bash
n=$1
shift
files=("$@")
echo "Number of Files: ${#files[@]}"
echo "Processing: ${files[*]}"
for file in "${files[@]}"; do
    echo "===($(wc -l -w -m "$file" | awk '{print $1, $2, $3, $4}'))==="
    grep -oE '[a-zA-Z]+' "$file" |tr '[:upper:]' '[:lower:]'|sort |uniq -c|sort -nr |head -n "$n"
done
echo "===done==="
```

## output
```bash
[bryruto@Brycen-archlinux hw2]$ bash wordCounter.sh 4 Kennedy.txt King.txt Lincoln.txt
Number of Files: 3
Processing: Kennedy.txt King.txt Lincoln.txt
===(19 561 3183 Kennedy.txt)===
     33 the
     24 of
     22 to
     19 we
===(58 1652 9061 King.txt)===
    102 the
     99 of
     60 to
     41 and
===(6 278 1477 Lincoln.txt)===
     13 that
     11 the
     10 we
      8 to
===done===
```


# everything I did
```bash
[bryruto@Brycen-archlinux hw2]$ nvim problem1.txt
[bryruto@Brycen-archlinux hw2]$ nvim problem1.md
[bryruto@Brycen-archlinux hw2]$ ls
Kennedy.txt  King.txt  Lincoln.txt  problem1.md
[bryruto@Brycen-archlinux hw2]$ last
reboot   system boot  7.2.6-arch2-1    Sat Sep 26 10:20   still running
reboot   system boot  7.2.6-arch2-1    Fri Sep 25 11:51 - 17:15  (05:23)
reboot   system boot  7.2.6-arch2-1    Fri Sep 25 10:41 - 11:51  (01:10)
reboot   system boot  7.2.6-arch2-1    Thu Sep 24 10:57 - 14:56  (03:59)
reboot   system boot  7.2.6-arch2-1    Wed Sep 23 13:21 - 09:02  (19:40)
reboot   system boot  7.2.6-arch2-1    Wed Sep 23 13:16 - 13:21  (00:04)
reboot   system boot  7.2.6-arch2-1    Tue Sep 22 17:12 - crash  (20:04)
reboot   system boot  7.2.6-arch2-1    Tue Sep 22 12:24 - 14:49  (02:24)
reboot   system boot  7.2.6-arch2-1    Tue Sep 22 11:05 - 11:41  (00:36)
reboot   system boot  7.2.6-arch2-1    Mon Sep 21 17:16 - 23:23  (06:07)
reboot   system boot  7.1.8-arch1-3    Sun Sep 20 10:46 - 22:37  (11:50)
reboot   system boot  7.1.8-arch1-3    Sat Sep 19 12:19 - 22:59  (10:40)
reboot   system boot  7.1.8-arch1-3    Fri Sep 18 12:10 - 17:20  (05:09)
reboot   system boot  7.1.8-arch1-3    Thu Sep 17 12:18 - 17:22  (05:03)
reboot   system boot  7.1.8-arch1-3    Thu Sep 17 11:41 - 12:16  (00:35)
reboot   system boot  7.1.8-arch1-3    Tue Sep 15 11:08 - 15:07  (03:58)
reboot   system boot  7.1.8-arch1-3    Mon Sep 14 12:38 - 15:06  (02:27)
reboot   system boot  7.1.8-arch1-3    Sun Sep 13 13:59 - 23:51  (09:52)
reboot   system boot  7.1.8-arch1-3    Sun Sep 13 13:26 - 13:58  (00:31)
reboot   system boot  7.1.8-arch1-3    Sat Sep 12 11:35 - 21:46  (10:10)
reboot   system boot  7.1.8-arch1-3    Fri Sep 11 12:20 - 17:22  (05:01)
reboot   system boot  7.1.8-arch1-3    Thu Sep 10 13:38 - 14:52  (01:13)
reboot   system boot  7.1.8-arch1-3    Thu Sep 10 11:10 - 13:37  (02:26)
reboot   system boot  7.1.8-arch1-3    Wed Sep  9 13:59 - 23:18  (09:18)
reboot   system boot  7.1.8-arch1-3    Wed Sep  9 11:47 - 13:59  (02:12)
reboot   system boot  7.1.8-arch1-3    Tue Sep  8 16:56 - 00:59  (08:03)
reboot   system boot  7.1.8-arch1-3    Tue Sep  8 15:08 - 15:09  (00:00)
reboot   system boot  7.1.8-arch1-3    Tue Sep  8 11:06 - 15:07  (04:01)
reboot   system boot  7.1.8-arch1-3    Mon Sep  7 12:03 - 01:23  (13:20)
reboot   system boot  7.1.8-arch1-3    Sun Sep  6 15:05 - 04:12  (13:06)
reboot   system boot  7.1.8-arch1-3    Sun Sep  6 14:22 - 15:05  (00:42)
reboot   system boot  7.1.8-arch1-3    Sat Sep  5 12:30 - 17:17  (04:47)
reboot   system boot  7.1.8-arch1-3    Fri Sep  4 19:12 - 20:26  (01:13)
reboot   system boot  7.1.8-arch1-3    Fri Sep  4 13:26 - 15:23  (01:56)
reboot   system boot  7.1.8-arch1-3    Fri Sep  4 12:18 - 13:26  (01:07)
reboot   system boot  7.1.8-arch1-3    Thu Sep  3 11:50 - 14:46  (02:56)
reboot   system boot  7.1.8-arch1-3    Wed Sep  2 15:00 - 00:15  (09:15)
reboot   system boot  7.1.8-arch1-3    Tue Sep  1 16:51 - 23:05  (06:13)
reboot   system boot  7.1.8-arch1-3    Tue Sep  1 14:49 - 15:01  (00:12)
reboot   system boot  7.1.8-arch1-3    Mon Aug 31 17:16 - 22:47  (05:31)
reboot   system boot  7.1.8-arch1-3    Mon Aug 31 11:55 - 15:06  (03:10)
reboot   system boot  7.1.8-arch1-3    Sun Aug 30 14:50 - 01:15  (10:24)
reboot   system boot  7.1.8-arch1-3    Sat Aug 29 12:11 - 16:19  (04:08)
reboot   system boot  7.1.8-arch1-3    Fri Aug 28 13:23 - 16:20  (02:56)
reboot   system boot  7.1.8-arch1-3    Wed Aug 26 12:04 - 19:21  (07:16)
reboot   system boot  7.1.8-arch1-3    Tue Aug 25 17:31 - 02:16  (08:45)
reboot   system boot  7.1.8-arch1-3    Tue Aug 25 11:23 - 15:06  (03:43)
reboot   system boot  7.1.8-arch1-3    Tue Aug 25 08:13 - 09:03  (00:49)
reboot   system boot  7.1.8-arch1-3    Mon Aug 24 17:46 - 23:43  (05:57)
reboot   system boot  7.1.8-arch1-3    Sun Aug 23 14:51 - 22:33  (07:41)
reboot   system boot  7.1.8-arch1-3    Fri Aug 21 15:38 - 16:21 (1+00:43)
reboot   system boot  7.1.8-arch1-3    Fri Aug 21 12:13 - 15:37  (03:24)
reboot   system boot  7.1.8-arch1-3    Thu Aug 20 17:07 - 17:22  (00:14)
reboot   system boot  7.1.8-arch1-3    Wed Aug 19 19:19 - 14:36  (19:17)
reboot   system boot  7.1.8-arch1-3    Wed Aug 19 15:24 - 19:15  (03:51)
reboot   system boot  7.1.8-arch1-3    Wed Aug 19 12:48 - 15:06  (02:18)
reboot   system boot  7.1.5-arch1-2    Tue Aug 18 17:26 - 00:54  (07:27)
reboot   system boot  7.1.5-arch1-2    Tue Aug 18 10:53 - 12:18  (01:25)
reboot   system boot  7.1.5-arch1-2    Tue Aug 18 08:43 - 09:43  (00:59)
reboot   system boot  7.1.5-arch1-2    Mon Aug 17 19:45 - 21:28  (01:42)
reboot   system boot  7.1.5-arch1-2    Sun Aug 16 12:46 - 16:04  (03:17)
reboot   system boot  7.1.5-arch1-2    Sat Aug 15 14:42 - 16:32  (01:50)
reboot   system boot  7.1.5-arch1-2    Fri Aug 14 12:27 - 15:42  (03:15)
reboot   system boot  7.1.5-arch1-2    Wed Aug 12 13:44 - 01:56  (12:12)
reboot   system boot  7.1.5-arch1-2    Wed Aug 12 01:22 - 02:28  (01:05)
reboot   system boot  7.1.5-arch1-2    Tue Aug 11 14:47 - 00:01  (09:14)
reboot   system boot  7.1.5-arch1-2    Tue Aug 11 12:31 - 14:46  (02:15)
reboot   system boot  7.1.5-arch1-2    Mon Aug 10 20:28 - 01:34  (05:05)
reboot   system boot  7.1.5-arch1-2    Mon Aug 10 18:23 - 20:27  (02:04)
reboot   system boot  7.1.5-arch1-2    Sun Aug  9 13:16 - 16:43  (03:26)
reboot   system boot  7.1.5-arch1-2    Sun Aug  9 12:32 - 13:15  (00:43)
reboot   system boot  7.1.5-arch1-2    Sat Aug  8 12:34 - 16:39  (04:05)
reboot   system boot  7.1.5-arch1-2    Thu Aug  6 12:21 - 15:44  (03:23)
reboot   system boot  7.0.12-arch1-1   Wed Aug  5 12:27 - 00:57  (12:29)
reboot   system boot  7.0.12-arch1-1   Tue Aug  4 22:20 - 00:41  (02:20)
reboot   system boot  7.0.12-arch1-1   Tue Aug  4 16:09 - 22:20  (06:10)
reboot   system boot  7.0.12-arch1-1   Mon Aug  3 12:57 - 02:35  (13:38)
reboot   system boot  7.0.12-arch1-1   Sun Aug  2 21:27 - 01:39  (04:12)
reboot   system boot  7.0.12-arch1-1   Sun Aug  2 17:32 - 21:26  (03:53)
reboot   system boot  7.0.12-arch1-1   Sat Aug  1 12:01 - 16:50  (04:49)
reboot   system boot  7.0.12-arch1-1   Thu Jul 30 13:02 - 16:12  (03:10)
reboot   system boot  7.0.12-arch1-1   Wed Jul 29 15:44 - 23:31  (07:47)
reboot   system boot  7.0.12-arch1-1   Wed Jul 29 08:39 - 11:31  (02:51)
reboot   system boot  7.0.12-arch1-1   Wed Jul 29 08:38 - 08:38  (00:00)
reboot   system boot  7.0.12-arch1-1   Tue Jul 28 23:16 - 00:52  (01:36)
reboot   system boot  7.0.12-arch1-1   Tue Jul 28 13:59 - 22:27  (08:28)
reboot   system boot  7.0.12-arch1-1   Tue Jul 28 10:47 - 11:35  (00:47)
reboot   system boot  7.0.12-arch1-1   Mon Jul 27 15:45 - 01:12  (09:26)
reboot   system boot  7.0.12-arch1-1   Mon Jul 27 15:00 - 15:44  (00:44)
reboot   system boot  7.0.12-arch1-1   Sun Jul 26 14:49 - 16:39  (01:50)
reboot   system boot  7.0.12-arch1-1   Sun Jul 26 14:07 - 14:48  (00:41)
reboot   system boot  7.0.12-arch1-1   Sat Jul 25 12:18 - 16:57  (04:39)
reboot   system boot  7.0.12-arch1-1   Sat Jul 25 12:06 - 12:17  (00:10)
reboot   system boot  7.0.12-arch1-1   Fri Jul 24 12:11 - 17:04  (04:52)
reboot   system boot  7.0.12-arch1-1   Thu Jul 23 12:30 - 16:27  (03:57)
reboot   system boot  7.0.12-arch1-1   Wed Jul 22 15:23 - 01:44  (10:20)
reboot   system boot  7.0.12-arch1-1   Tue Jul 21 09:35 - 01:47  (16:11)
reboot   system boot  7.0.12-arch1-1   Tue Jul 21 01:16 - 04:27  (03:11)
reboot   system boot  7.0.12-arch1-1   Mon Jul 20 17:50 - 01:15  (07:25)
reboot   system boot  7.0.12-arch1-1   Mon Jul 20 17:08 - 17:49  (00:41)
reboot   system boot  7.0.12-arch1-1   Sun Jul 19 11:43 - 17:42  (05:58)
reboot   system boot  7.0.12-arch1-1   Sat Jul 18 12:06 - 17:15  (05:09)
reboot   system boot  7.0.12-arch1-1   Fri Jul 17 11:35 - 17:26  (05:50)
reboot   system boot  7.0.12-arch1-1   Thu Jul 16 13:42 - 17:19  (03:37)
reboot   system boot  7.0.12-arch1-1   Wed Jul 15 15:42 - 04:00  (12:17)
reboot   system boot  7.0.12-arch1-1   Wed Jul 15 14:57 - 15:41  (00:44)
reboot   system boot  7.0.12-arch1-1   Tue Jul 14 18:10 - 03:05  (08:55)
reboot   system boot  7.0.12-arch1-1   Tue Jul 14 17:28 - 17:56  (00:27)
reboot   system boot  7.0.12-arch1-1   Mon Jul 13 16:30 - 05:44  (13:14)
reboot   system boot  7.0.12-arch1-1   Sun Jul 12 12:00 - 16:09  (04:09)
reboot   system boot  7.0.12-arch1-1   Sun Jul 12 11:35 - 11:59  (00:24)
reboot   system boot  7.0.12-arch1-1   Fri Jul 10 16:09 - 16:45  (00:35)
reboot   system boot  7.0.12-arch1-1   Fri Jul 10 12:18 - 16:08  (03:49)
reboot   system boot  7.0.12-arch1-1   Wed Jul  8 16:16 - 23:08  (06:52)
reboot   system boot  7.0.12-arch1-1   Wed Jul  8 14:59 - 16:15  (01:15)
reboot   system boot  7.0.12-arch1-1   Tue Jul  7 23:41 - 04:17  (04:36)
reboot   system boot  7.0.12-arch1-1   Tue Jul  7 17:56 - 23:40  (05:44)
reboot   system boot  7.0.12-arch1-1   Tue Jul  7 04:17 - 05:32  (01:14)
reboot   system boot  7.0.12-arch1-1   Tue Jul  7 01:57 - 04:16  (02:19)
reboot   system boot  7.0.12-arch1-1   Mon Jul  6 02:35 - 03:03  (00:27)
reboot   system boot  7.0.12-arch1-1   Sun Jul  5 13:23 - 14:39  (01:15)
reboot   system boot  7.0.12-arch1-1   Sun Jul  5 12:09 - 13:23  (01:13)
reboot   system boot  7.0.12-arch1-1   Sun Jul  5 11:34 - 12:08  (00:34)
reboot   system boot  7.0.12-arch1-1   Sun Jul  5 10:38 - 11:33  (00:55)
reboot   system boot  7.0.12-arch1-1   Sun Jul  5 04:53 - 04:57  (00:03)
reboot   system boot  7.0.12-arch1-1   Sat Jul  4 19:54 - 22:47  (02:52)
reboot   system boot  7.0.12-arch1-1   Sat Jul  4 19:20 - 19:53  (00:32)
reboot   system boot  7.0.12-arch1-1   Sat Jul  4 17:18 - 19:20  (02:01)
reboot   system boot  7.0.12-arch1-1   Thu Jul  2 10:20 - 12:27  (02:07)
reboot   system boot  7.0.12-arch1-1   Thu Jul  2 08:02 - 10:19  (02:17)
reboot   system boot  7.0.12-arch1-1   Thu Jul  2 04:07 - 04:08  (00:00)
reboot   system boot  7.0.12-arch1-1   Wed Jul  1 09:04 - 11:17  (02:12)
reboot   system boot  7.0.12-arch1-1   Tue Jun 30 19:10 - 03:24  (08:14)
reboot   system boot  7.0.12-arch1-1   Tue Jun 30 09:00 - 11:39  (02:39)
reboot   system boot  7.0.12-arch1-1   Tue Jun 30 06:10 - 08:59  (02:49)
reboot   system boot  7.0.12-arch1-1   Tue Jun 30 04:22 - 06:09  (01:47)
reboot   system boot  7.0.12-arch1-1   Mon Jun 29 15:02 - 21:39  (06:36)
reboot   system boot  7.0.12-arch1-1   Mon Jun 29 00:19 - 11:38  (11:18)
reboot   system boot  7.0.12-arch1-1   Sun Jun 28 11:26 - 11:32  (00:06)
reboot   system boot  7.0.12-arch1-1   Sun Jun 28 09:51 - 11:25  (01:34)
reboot   system boot  7.0.12-arch1-1   Sat Jun 27 12:39 - 15:52  (03:12)
reboot   system boot  7.0.12-arch1-1   Thu Jun 25 12:07 - 15:45  (03:38)
[bryruto@Brycen-archlinux hw2]$ ls
Kennedy.txt  King.txt  Lincoln.txt  problem1.md
[bryruto@Brycen-archlinux hw2]$ cat lincoln.txt
cat: lincoln.txt: No such file or directory
[bryruto@Brycen-archlinux hw2]$ cat linconln.txt | uniq -c | sort -nr | head -n 5  
cat: linconln.txt: No such file or directory
[bryruto@Brycen-archlinux hw2]$ cat Linconln.txt | uniq -c | sort -nr | head -n 5  
cat: Linconln.txt: No such file or directory
[bryruto@Brycen-archlinux hw2]$ cat Lincoln.txt | uniq -c | sort -nr | head -n 5  
      1 Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.
[bryruto@Brycen-archlinux hw2]$ grep -oE '[a-zA-Z]+' Lincoln.txt | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -nr | head -n 5
     13 that
     11 the
     10 we
      8 to
      8 here
[bryruto@Brycen-archlinux hw2]$ grep -oE '[a-zA-Z]+' Lincoln.txt | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -nr | head -n 3
     13 that
     11 the
     10 we
[bryruto@Brycen-archlinux hw2]$ grep -oE '[a-zA-Z]+' Kennedy.txt | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -nr | head -n 3
     33 the
     24 of
     22 to
[bryruto@Brycen-archlinux hw2]$ sort kennedy.txt > file.txt
sort: cannot read: kennedy.txt: No such file or directory
[bryruto@Brycen-archlinux hw2]$ sort Kennedy.txt > file.txt
[bryruto@Brycen-archlinux hw2]$ sort -o Kennedy.txt Kennedy.txt
[bryruto@Brycen-archlinux hw2]$ cat Kennedy.txt

Let every nation know, whether it wishes us well or ill, that we shall pay any price, bear any burden, meet any hardship, support any friend, oppose any foe to assure the survival and the success of liberty.
The world is very different now. For man holds in his mortal hands the power to abolish all forms of human poverty and all forms of human life. And yet the same revolutionary beliefs for which our forebears fought are still at issue around the globe--the belief that the rights of man come not from the generosity of the state but from the hand of God.
This much we pledge--and more.
To our sister republics south of our border, we offer a special pledge--to convert our good words into good deeds--in a new alliance for progress--to assist free men and free governments in casting off the chains of poverty. But this peaceful revolution of hope cannot become the prey of hostile powers. Let all our neighbors know that we shall join with them to oppose aggression or subversion anywhere in the Americas. And let every other power know that this Hemisphere intends to remain the master of its own house.
To those new states whom we welcome to the ranks of the free, we pledge our word that one form of colonial control shall not have passed away merely to be replaced by a far more iron tyranny. We shall not always expect to find them supporting our view. But we shall always hope to find them strongly supporting their own freedom--and to remember that, in the past, those who foolishly sought power by riding the back of the tiger ended up inside.
[bryruto@Brycen-archlinux hw2]$ ls
Kennedy.txt  King.txt  Lincoln.txt  problem1.md
[bryruto@Brycen-archlinux hw2]$ nvim problem1.md
[bryruto@Brycen-archlinux hw2]$ ls
Kennedy.txt  King.txt  Lincoln.txt  problem1.md
[bryruto@Brycen-archlinux hw2]$  grep -oE '[a-zA-Z]+' Lincoln.txt | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -nr | head -n 5
     13 that
     11 the
     10 we
      8 to
      8 here
[bryruto@Brycen-archlinux hw2]$  grep -oE '[a-zA-Z]+' Kennedy.txt | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -nr | head -n 3
     33 the
     24 of
     22 to
[bryruto@Brycen-archlinux hw2]$ ^C
[bryruto@Brycen-archlinux hw2]$ nvim problem1.md
[bryruto@Brycen-archlinux hw2]$ nvim problem1.md
[bryruto@Brycen-archlinux hw2]$ cat Kennedy.txt
Vice President Johnson, Mr. Speaker, Mr. Chief Justice, President Eisenhower, Vice President Nixon, President Truman, Reverend Clergy, fellow citizens:

We observe today not a victory of party but a celebration of freedom--symbolizing an end as well as a beginning--signifying renewal as well as change. For I have sworn before you and Almighty God the same solemn oath our forbears prescribed nearly a century and three-quarters ago.

The world is very different now. For man holds in his mortal hands the power to abolish all forms of human poverty and all forms of human life. And yet the same revolutionary beliefs for which our forebears fought are still at issue around the globe--the belief that the rights of man come not from the generosity of the state but from the hand of God.

We dare not forget today that we are the heirs of that first revolution. Let the word go forth from this time and place, to friend and foe alike, that the torch has been passed to a new generation of Americans--born in this century, tempered by war, disciplined by a hard and bitter peace, proud of our ancient heritage--and unwilling to witness or permit the slow undoing of those human rights to which this nation has always been committed, and to which we are committed today at home and around the world.

Let every nation know, whether it wishes us well or ill, that we shall pay any price, bear any burden, meet any hardship, support any friend, oppose any foe to assure the survival and the success of liberty.

This much we pledge--and more.

To those old allies whose cultural and spiritual origins we share, we pledge the loyalty of faithful friends. United there is little we cannot do in a host of cooperative ventures. Divided there is little we can do--for we dare not meet a powerful challenge at odds and split asunder.

To those new states whom we welcome to the ranks of the free, we pledge our word that one form of colonial control shall not have passed away merely to be replaced by a far more iron tyranny. We shall not always expect to find them supporting our view. But we shall always hope to find them strongly supporting their own freedom--and to remember that, in the past, those who foolishly sought power by riding the back of the tiger ended up inside.

To those people in the huts and villages of half the globe struggling to break the bonds of mass misery, we pledge our best efforts to help them help themselves, for whatever period is required--not because the communists may be doing it, not because we seek their votes, but because it is right. If a free society cannot help the many who are poor, it cannot save the few who are rich.

To our sister republics south of our border, we offer a special pledge--to convert our good words into good deeds--in a new alliance for progress--to assist free men and free governments in casting off the chains of poverty. But this peaceful revolution of hope cannot become the prey of hostile powers. Let all our neighbors know that we shall join with them to oppose aggression or subversion anywhere in the Americas. And let every other power know that this Hemisphere intends to remain the master of its own house.
[bryruto@Brycen-archlinux hw2]$ sort kennedy > kennedy 
[bryruto@Brycen-archlinux hw2]$ cat kennedy
[bryruto@Brycen-archlinux hw2]$ sort Kennedy.txt > Kennedy.txt
[bryruto@Brycen-archlinux hw2]$ cat Kennedy.txt
[bryruto@Brycen-archlinux hw2]$ ls
kennedy  Kennedy.txt  King.txt  Lincoln.txt  problem1.md
[bryruto@Brycen-archlinux hw2]$ rm kennedy 
[bryruto@Brycen-archlinux hw2]$ ls
Kennedy.txt  King.txt  Lincoln.txt  problem1.md
[bryruto@Brycen-archlinux hw2]$ cat King.txt
I am happy to join with you today in what will go down in history as the greatest demonstration for freedom in the history of our nation.

Five score years ago, a great American, in whose symbolic shadow we stand today, signed the Emancipation Proclamation. This momentous decree came as a great beacon light of hope to millions of Negro slaves who had been seared in the flames of withering injustice. It came as a joyous daybreak to end the long night of their captivity.

But one hundred years later, the Negro still is not free. One hundred years later, the life of the Negro is still sadly crippled by the manacles of segregation and the chains of discrimination. One hundred years later, the Negro lives on a lonely island of poverty in the midst of a vast ocean of material prosperity. One hundred years later, the Negro is still languishing in the corners of American society and finds himself an exile in his own land. So we have come here today to dramatize a shameful condition.

In a sense we have come to our nation's capital to cash a check. When the architects of our republic wrote the magnificent words of the Constitution and the Declaration of Independence, they were signing a promissory note to which every American was to fall heir. This note was a promise that all men, yes, black men as well as white men, would be guaranteed the unalienable rights of life, liberty, and the pursuit of happiness.

It is obvious today that America has defaulted on this promissory note insofar as her citizens of color are concerned. Instead of honoring this sacred obligation, America has given the Negro people a bad check, a check which has come back marked "insufficient funds." But we refuse to believe that the bank of justice is bankrupt. We refuse to believe that there are insufficient funds in the great vaults of opportunity of this nation. So we have come to cash this check — a check that will give us upon demand the riches of freedom and the security of justice. We have also come to this hallowed spot to remind America of the fierce urgency of now. This is no time to engage in the luxury of cooling off or to take the tranquilizing drug of gradualism. Now is the time to make real the promises of democracy. Now is the time to rise from the dark and desolate valley of segregation to the sunlit path of racial justice. Now is the time to lift our nation from the quick sands of racial injustice to the solid rock of brotherhood. Now is the time to make justice a reality for all of God's children.

It would be fatal for the nation to overlook the urgency of the moment. This sweltering summer of the Negro's legitimate discontent will not pass until there is an invigorating autumn of freedom and equality. Nineteen sixty-three is not an end, but a beginning. Those who hope that the Negro needed to blow off steam and will now be content will have a rude awakening if the nation returns to business as usual. There will be neither rest nor tranquility in America until the Negro is granted his citizenship rights. The whirlwinds of revolt will continue to shake the foundations of our nation until the bright day of justice emerges.

But there is something that I must say to my people who stand on the warm threshold which leads into the palace of justice. In the process of gaining our rightful place we must not be guilty of wrongful deeds. Let us not seek to satisfy our thirst for freedom by drinking from the cup of bitterness and hatred.

We must forever conduct our struggle on the high plane of dignity and discipline. We must not allow our creative protest to degenerate into physical violence. Again and again we must rise to the majestic heights of meeting physical force with soul force. The marvelous new militancy which has engulfed the Negro community must not lead us to a distrust of all white people, for many of our white brothers, as evidenced by their presence here today, have come to realize that their destiny is tied up with our destiny. They have come to realize that their freedom is inextricably bound to our freedom. We cannot walk alone.

As we walk, we must make the pledge that we shall always march ahead. We cannot turn back. There are those who are asking the devotees of civil rights, "When will you be satisfied?" We can never be satisfied as long as the Negro is the victim of the unspeakable horrors of police brutality. We can never be satisfied, as long as our bodies, heavy with the fatigue of travel, cannot gain lodging in the motels of the highways and the hotels of the cities. We cannot be satisfied as long as the Negro's basic mobility is from a smaller ghetto to a larger one. We can never be satisfied as long as our children are stripped of their selfhood and robbed of their dignity by signs stating "For Whites Only". We cannot be satisfied as long as a Negro in Mississippi cannot vote and a Negro in New York believes he has nothing for which to vote. No, no, we are not satisfied, and we will not be satisfied until justice rolls down like waters and righteousness like a mighty stream.

I am not unmindful that some of you have come here out of great trials and tribulations. Some of you have come fresh from narrow jail cells. Some of you have come from areas where your quest for freedom left you battered by the storms of persecution and staggered by the winds of police brutality. You have been the veterans of creative suffering. Continue to work with the faith that unearned suffering is redemptive.

Go back to Mississippi, go back to Alabama, go back to South Carolina, go back to Georgia, go back to Louisiana, go back to the slums and ghettos of our northern cities, knowing that somehow this situation can and will be changed. Let us not wallow in the valley of despair.

I say to you today, my friends, so even though we face the difficulties of today and tomorrow, I still have a dream. It is a dream deeply rooted in the American dream.

I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident: that all men are created equal."

I have a dream that one day on the red hills of Georgia the sons of former slaves and the sons of former slave owners will be able to sit down together at the table of brotherhood.

I have a dream that one day even the state of Mississippi, a state sweltering with the heat of injustice, sweltering with the heat of oppression, will be transformed into an oasis of freedom and justice.

I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character.

I have a dream today.

I have a dream that one day, down in Alabama, with its vicious racists, with its governor having his lips dripping with the words of interposition and nullification; one day right there in Alabama, little black boys and black girls will be able to join hands with little white boys and white girls as sisters and brothers.

I have a dream today.

I have a dream that one day every valley shall be exalted, every hill and mountain shall be made low, the rough places will be made plain, and the crooked places will be made straight, and the glory of the Lord shall be revealed, and all flesh shall see it together.

This is our hope. This is the faith that I go back to the South with. With this faith we will be able to hew out of the mountain of despair a stone of hope. With this faith we will be able to transform the jangling discords of our nation into a beautiful symphony of brotherhood. With this faith we will be able to work together, to pray together, to struggle together, to go to jail together, to stand up for freedom together, knowing that we will be free one day.

This will be the day when all of God's children will be able to sing with a new meaning, "My country, 'tis of thee, sweet land of liberty, of thee I sing. Land where my fathers died, land of the pilgrim's pride, from every mountainside, let freedom ring."

And if America is to be a great nation this must become true. So let freedom ring from the prodigious hilltops of New Hampshire. Let freedom ring from the mighty mountains of New York. Let freedom ring from the heightening Alleghenies of Pennsylvania!

Let freedom ring from the snowcapped Rockies of Colorado!

Let freedom ring from the curvaceous slopes of California!

But not only that; let freedom ring from Stone Mountain of Georgia!

Let freedom ring from Lookout Mountain of Tennessee!

Let freedom ring from every hill and molehill of Mississippi. From every mountainside, let freedom ring.

And when this happens, when we allow freedom to ring, when we let it ring from every village and every hamlet, from every state and every city, we will be able to speed up that day when all of God's children, black men and white men, Jews and Gentiles, Protestants and Catholics, will be able to join hands and sing in the words of the old Negro spiritual, "Free at last! free at last! thank God Almighty, we are free at last!"

[bryruto@Brycen-archlinux hw2]$ sort -o King.txt King.txt
[bryruto@Brycen-archlinux hw2]$ cat King.txt

And if America is to be a great nation this must become true. So let freedom ring from the prodigious hilltops of New Hampshire. Let freedom ring from the mighty mountains of New York. Let freedom ring from the heightening Alleghenies of Pennsylvania!
And when this happens, when we allow freedom to ring, when we let it ring from every village and every hamlet, from every state and every city, we will be able to speed up that day when all of God's children, black men and white men, Jews and Gentiles, Protestants and Catholics, will be able to join hands and sing in the words of the old Negro spiritual, "Free at last! free at last! thank God Almighty, we are free at last!"
As we walk, we must make the pledge that we shall always march ahead. We cannot turn back. There are those who are asking the devotees of civil rights, "When will you be satisfied?" We can never be satisfied as long as the Negro is the victim of the unspeakable horrors of police brutality. We can never be satisfied, as long as our bodies, heavy with the fatigue of travel, cannot gain lodging in the motels of the highways and the hotels of the cities. We cannot be satisfied as long as the Negro's basic mobility is from a smaller ghetto to a larger one. We can never be satisfied as long as our children are stripped of their selfhood and robbed of their dignity by signs stating "For Whites Only". We cannot be satisfied as long as a Negro in Mississippi cannot vote and a Negro in New York believes he has nothing for which to vote. No, no, we are not satisfied, and we will not be satisfied until justice rolls down like waters and righteousness like a mighty stream.
But not only that; let freedom ring from Stone Mountain of Georgia!
But one hundred years later, the Negro still is not free. One hundred years later, the life of the Negro is still sadly crippled by the manacles of segregation and the chains of discrimination. One hundred years later, the Negro lives on a lonely island of poverty in the midst of a vast ocean of material prosperity. One hundred years later, the Negro is still languishing in the corners of American society and finds himself an exile in his own land. So we have come here today to dramatize a shameful condition.
But there is something that I must say to my people who stand on the warm threshold which leads into the palace of justice. In the process of gaining our rightful place we must not be guilty of wrongful deeds. Let us not seek to satisfy our thirst for freedom by drinking from the cup of bitterness and hatred.
Five score years ago, a great American, in whose symbolic shadow we stand today, signed the Emancipation Proclamation. This momentous decree came as a great beacon light of hope to millions of Negro slaves who had been seared in the flames of withering injustice. It came as a joyous daybreak to end the long night of their captivity.
Go back to Mississippi, go back to Alabama, go back to South Carolina, go back to Georgia, go back to Louisiana, go back to the slums and ghettos of our northern cities, knowing that somehow this situation can and will be changed. Let us not wallow in the valley of despair.
I am happy to join with you today in what will go down in history as the greatest demonstration for freedom in the history of our nation.
I am not unmindful that some of you have come here out of great trials and tribulations. Some of you have come fresh from narrow jail cells. Some of you have come from areas where your quest for freedom left you battered by the storms of persecution and staggered by the winds of police brutality. You have been the veterans of creative suffering. Continue to work with the faith that unearned suffering is redemptive.
I have a dream that my four little children will one day live in a nation where they will not be judged by the color of their skin but by the content of their character.
I have a dream that one day, down in Alabama, with its vicious racists, with its governor having his lips dripping with the words of interposition and nullification; one day right there in Alabama, little black boys and black girls will be able to join hands with little white boys and white girls as sisters and brothers.
I have a dream that one day even the state of Mississippi, a state sweltering with the heat of injustice, sweltering with the heat of oppression, will be transformed into an oasis of freedom and justice.
I have a dream that one day every valley shall be exalted, every hill and mountain shall be made low, the rough places will be made plain, and the crooked places will be made straight, and the glory of the Lord shall be revealed, and all flesh shall see it together.
I have a dream that one day on the red hills of Georgia the sons of former slaves and the sons of former slave owners will be able to sit down together at the table of brotherhood.
I have a dream that one day this nation will rise up and live out the true meaning of its creed: "We hold these truths to be self-evident: that all men are created equal."
[bryruto@Brycen-archlinux hw2]$ ls
Kennedy.txt  King.txt  Lincoln.txt  problem1.md  wordCounter.sh
[bryruto@Brycen-archlinux hw2]$ bash wordCounter.sh 4 Kennedy.txt Lincoln.txt
==== Kennedy.txt (# of lines, # of words, # of characters) ====
  19  561 3183 Kennedy.txt
     33 the
     24 of
     22 to
     19 we

==== Lincoln.txt (# of lines, # of words, # of characters) ====
   6  278 1477 Lincoln.txt
     13 that
     11 the
     10 we
      8 to

[bryruto@Brycen-archlinux hw2]$ ls
Kennedy.txt  King.txt  Lincoln.txt  problem1.md  wordCounter.sh
[bryruto@Brycen-archlinux hw2]$ nvim wordCounter.sh
[bryruto@Brycen-archlinux hw2]$ bash wordCounter.sh
Number of Files: 0
Processing: 
[bryruto@Brycen-archlinux hw2]$ bash wordCounter.sh 4 Kennedy.txt King.txt Lincoln.txt
Number of Files: 0
Processing: 
[bryruto@Brycen-archlinux hw2]$ nvim wordCounter.sh
[bryruto@Brycen-archlinux hw2]$ bash wordCounter.sh 4 Kennedy.txt King.txt Lincoln.txt
Number of Files: 3
Processing: Kennedy.txt King.txt Lincoln.txt

===(  19  561 3183 Kennedy.txt)====
     33 the
     24 of
     22 to
     19 we

===(  58 1652 9061 King.txt)====
    102 the
     99 of
     60 to
     41 and

===(   6  278 1477 Lincoln.txt)====
     13 that
     11 the
     10 we
      8 to

==done====
[bryruto@Brycen-archlinux hw2]$ nvim wordCounter.sh
[bryruto@Brycen-archlinux hw2]$ bash wordCounter.sh 4 Kennedy.txt King.txt Lincoln.txt
Number of Files: 3
Processing: Kennedy.txt King.txt Lincoln.txt
===(  19  561 3183 Kennedy.txt)====
     33 the
     24 of
     22 to
     19 we
===(  58 1652 9061 King.txt)====
    102 the
     99 of
     60 to
     41 and
===(   6  278 1477 Lincoln.txt)====
     13 that
     11 the
     10 we
      8 to

==done====
[bryruto@Brycen-archlinux hw2]$ nvim wordCounter.sh
[bryruto@Brycen-archlinux hw2]$ bash wordCounter.sh 4 Kennedy.txt King.txt Lincoln.txt
Number of Files: 3
Processing: Kennedy.txt King.txt Lincoln.txt
===(  19  561 3183 Kennedy.txt)===
     33 the
     24 of
     22 to
     19 we
===(  58 1652 9061 King.txt)===
    102 the
     99 of
     60 to
     41 and
===(   6  278 1477 Lincoln.txt)===
     13 that
     11 the
     10 we
      8 to

==done====
[bryruto@Brycen-archlinux hw2]$ nvim wordCounter.sh
[bryruto@Brycen-archlinux hw2]$ bash wordCounter.sh 4 Kennedy.txt King.txt Lincoln.txt
Number of Files: 3
Processing: Kennedy.txt King.txt Lincoln.txt
===(Kennedy.txt)===
     33 the
     24 of
     22 to
     19 we
===(King.txt)===
    102 the
     99 of
     60 to
     41 and
===(Lincoln.txt)===
     13 that
     11 the
     10 we
      8 to
===done===
[bryruto@Brycen-archlinux hw2]$ nvim wordCounter.sh
[bryruto@Brycen-archlinux hw2]$ bash wordCounter.sh 4 Kennedy.txt King.txt Lincoln.txt
Number of Files: 3
Processing: Kennedy.txt King.txt Lincoln.txt
wc: file: No such file or directory
===()===
     33 the
     24 of
     22 to
     19 we
wc: file: No such file or directory
===()===
    102 the
     99 of
     60 to
     41 and
wc: file: No such file or directory
===()===
     13 that
     11 the
     10 we
      8 to
===done===
[bryruto@Brycen-archlinux hw2]$ nvim wordCounter.sh
[bryruto@Brycen-archlinux hw2]$ bash wordCounter.sh 4 Kennedy.txt King.txt Lincoln.txt
Number of Files: 3
Processing: Kennedy.txt King.txt Lincoln.txt
===(  19  561 3183 Kennedy.txt)===
     33 the
     24 of
     22 to
     19 we
===(  58 1652 9061 King.txt)===
    102 the
     99 of
     60 to
     41 and
===(   6  278 1477 Lincoln.txt)===
     13 that
     11 the
     10 we
      8 to
===done===
[bryruto@Brycen-archlinux hw2]$ nvim wordCounter.sh
[bryruto@Brycen-archlinux hw2]$ bash wordCounter.sh 4 Kennedy.txt King.txt Lincoln.txt
Number of Files: 3
Processing: Kennedy.txt King.txt Lincoln.txt
===(19 561 3183 Kennedy.txt)===
     33 the
     24 of
     22 to
     19 we
===(58 1652 9061 King.txt)===
    102 the
     99 of
     60 to
     41 and
===(6 278 1477 Lincoln.txt)===
     13 that
     11 the
     10 we
      8 to
===done===
[bryruto@Brycen-archlinux hw2]$ ls
Kennedy.txt  King.txt  Lincoln.txt  problem1.md  wordCounter.sh
[bryruto@Brycen-archlinux hw2]$ nvim problem1.md
[bryruto@Brycen-archlinux hw2]$ nvim problem1.md
[bryruto@Brycen-archlinux hw2]$ ls
Kennedy.txt  King.txt  Lincoln.txt  problem1.md  wordCounter.sh
[bryruto@Brycen-archlinux hw2]$ wordCounter.sh
bash: wordCounter.sh: command not found
[bryruto@Brycen-archlinux hw2]$ nvim wordCounter.sh
[bryruto@Brycen-archlinux hw2]$ nvim problem1.md
[bryruto@Brycen-archlinux hw2]$ 
```
