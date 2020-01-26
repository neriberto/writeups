# Motivational Message

## Description

My friend sent me this motivational message because the CTF organizers made this competition too hard, but there's nothing in the message but a complete mess. I think the CTF organizers tampered with it to make it seem like my friend doesn't believe in me anymore, but it's working like reverse psychology on me!!!!

### Hint

The hint is a link to : https://github.com/JEF1056/riceteacatpanda/tree/master/Motivational Message (200)

## Solution

Get the file from github

```bash
$ wget https://github.com/JEF1056/riceteacatpanda/blob/master/Motivational%20Message%20(200)/motivation!!!!!.txt?raw=true
```

Let's see the output of the `file` command

```bash
$ file motivation!!!!!.txt
motivation!!!!!.txt: data
```

At this moment the obvious execution of `strings` with `grep` command didn't brings the flag, then let's try identify the file using `hexdump`

```bash
hexdump -C -n 100 motivation!!!!!.txt
00000000  82 60 42 ae 44 4e 45 49  00 00 00 00 df db f8 e5  |.`B.DNEI........|
00000010  19 76 cb 05 03 ff ef fe  92 3f f8 11 ec 04 01 00  |.v.......?......|
00000020  40 10 04 01 00 40 10 04  01 00 40 10 04 51 d3 6e  |@....@....@..Q.n|
00000030  99 df ff a4 9f ff 49 69  f4 05 e0 23 38 08 02 00  |......Ii...#8...|
00000040  80 20 08 02 00 80 20 08  02 00 80 21 b6 87 57 36  |. .... ....!..W6|
00000050  e8 08 05 9b 01 00 40 10  04 01 00 40 10 04 01 00  |......@....@....|
00000060  40 10 04 51                                       |@..Q|
00000064
```

Ok, pause to read the description and after the phrase (but it's working like `reverse` psychology on me!!!!) caught my eye, lets see the output of `hexdump` again, but now let's see all.

```bash
hexdump -C motivation!!!!!.txt
```

too much lines before

```bash
00040d30  4c 99 92 66 66 4c cc cc  99 33 26 64 92 64 c9 24  |L..ffL...3&d.d.$|
00040d40  c9 24 92 49 24 92 5f a3  8e 38 e3 df 38 e3 8e 38  |.$.I$._..8..8..8|
00040d50  fb fb ff ff e3 fd dd 44  0f dd ec 5e 78 54 41 44  |.......D...^xTAD|
00040d60  49 00 20 00 00 3b 4f 36  12 00 00 00 06 08 ad 03  |I. ..;O6........|
00040d70  00 00 e8 03 00 00 52 44  48 49 0d 00 00 00 0a 1a  |......RDHI......|
00040d80  0a 0d 47 4e 50 89                                 |..GNP.|
00040d86
```

Can you see the GNP ? this remenber PNG in reverse, then let's `reverse` the file

```
$ cat reverse.py
with open('motivation!!!!!.txt', 'rb') as fp_in:
    reversed_data = fp_in.read()[::-1]
    with open('motivation.png', 'wb') as fp_out:
        fp_out.write(reversed_data)

$ python reverse.py
$ file motivation.png
motivation.png: PNG image data, 1000 x 941, 8-bit/color RGBA, non-interlaced
```

We found the image:

![Motivation PNG](https://raw.githubusercontent.com/neriberto/writeups/master/riceteacatpanda/motivation/motivation.png)

And the last step, to get the flag:

```bash
zsteg motivation.png  | grep rtcp
b1,rgb,lsb,xy       .. text: "rtcp{^ww3_1_b3l31v3_1n_y0u!}"
```

Note: if didn't has `zsteg` installed, try it (for debian flavors):

```bash
$ sudo gem install zsteg
```
