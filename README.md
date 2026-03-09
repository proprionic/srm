# SRM

SRM (Smarter rm) is born as an alternative to `rm` (the linux command used to remove files).. Its goal is to be a **SMARTER** and **SAFER** version of it.

# How?

SRM is built with cleanliness in mind. it uses a safe and intuitive approach to recover and protect your files.

```bash 
/home/USER/.trash/
├── files
│   ├── 7ea875ac-aba3-404e-8801-ec0255001e5c.txt
│   ├── 9845e262-ade4-4c3a-a7bc-24c77275bd87.py
│   ├── adb0ebf0-fb34-4fa5-8d43-923e5bdd8aff.md
│   ├── ec9d95e2-d2e9-490a-bf8e-e2fd9ae43461.cpp
│   └── fa6c6b94-5fa1-4c36-8978-e96ce3953cf3.js
└── metadata
    ├── 7ea875ac-aba3-404e-8801-ec0255001e5c.json
    ├── 9845e262-ade4-4c3a-a7bc-24c77275bd87.json
    ├── adb0ebf0-fb34-4fa5-8d43-923e5bdd8aff.json
    ├── b826819e-4e2c-46f1-b90f-430c143541c1.json
    ├── ec9d95e2-d2e9-490a-bf8e-e2fd9ae43461.json
    └── fa6c6b94-5fa1-4c36-8978-e96ce3953cf3.json
```

What it'll do is move the deleted file into the directory *~/.trash/files*, assign it a UUID  and create metadata about it in the *~/.trash/metadata* directory.

The metadata will have a bunch of useful information SRM will then use to recover your file. 
**UUID** ==> It's just the UUID.
**dest** ==> The destination of the file
**og_path** ==> The original path# SRM

SRM (Smarter rm) is born as an alternative to `rm` (the linux command used to remove files).. Its goal is to be a **SMARTER** and **SAFER** version of it.

# How?

SRM is built with cleanliness in mind. it uses a safe and intuitive approach to recover and protect your files.

```bash 
/home/USER/.trash/
├── files
│   ├── 7ea875ac-aba3-404e-8801-ec0255001e5c.txt
│   ├── 9845e262-ade4-4c3a-a7bc-24c77275bd87.py
│   ├── adb0ebf0-fb34-4fa5-8d43-923e5bdd8aff.md
│   ├── ec9d95e2-d2e9-490a-bf8e-e2fd9ae43461.cpp
│   └── fa6c6b94-5fa1-4c36-8978-e96ce3953cf3.js
└── metadata
    ├── 7ea875ac-aba3-404e-8801-ec0255001e5c.json
    ├── 9845e262-ade4-4c3a-a7bc-24c77275bd87.json
    ├── adb0ebf0-fb34-4fa5-8d43-923e5bdd8aff.json
    ├── b826819e-4e2c-46f1-b90f-430c143541c1.json
    ├── ec9d95e2-d2e9-490a-bf8e-e2fd9ae43461.json
    └── fa6c6b94-5fa1-4c36-8978-e96ce3953cf3.json
```

What it'll do is move the deleted file into the directory *~/.trash/files*, assign it a UUID  and create metadata about it in the *~/.trash/metadata* directory.

The metadata will have a bunch of useful information SRM will then use to recover your file.

**UUID** ==> It's just the UUID.
**dest** ==> The destination of the file
**og_path** ==> The original path
**del_time** ==> the time and date of the deletion of the file.

This is an **example** of the metadata. 

```json
{
"UUID": "7ea875ac-aba3-404e-8801-ec0255001e5c", 
"filename": "nutz.txt",
"dest": "/home/deez/.trash/files/7ea875ac-aba3-404e-8801-ec0255001e5c", 
"og_path": "/home/deez/projects/srm/nutz.txt", 
"del_time": "2026-03-04 22:42:47"
}
```

# About it

SRM is built in python *(ik, not the best for a tool like this, i might port it to c or cpp.)*, it was born as an app you run through the terminal (not a command, literally python3 srm.py ...) and then made into a CLI tool. 

I started building it out of pure boredom and to get a python refresher, i just noticed it could become an amazing project, so, here i am writing the docs for it. :)).

I started writing docs for it pretty late actually, i've been working on the first version of srm for something like 3/4 days, so, yeah... whoops..
# Devlog

#### ToDo
##### - Arguments
- **clean** ==> Delete *ALL* files in the *~/.trash/files* directory -- done 
	- clean **(n)** ==> delete files **older** than *'n'* days. -- not done
	- clean **xG** ==> delete files larger than *'x'* GB. -- not done
	- clean **xM** ==> delete files older than *'x'* MB. -- not done 

- **recover** ==> Recover a file from trash to it's original directory -- not done
	- recover *(file)* **directory** ==> Recover a file from the trash into a
	 specified directory. -- not done 

##### QoL 

## Sensible paths

I wanna introduce the recognition of sensible paths (e.g /, /home/user, /home/user/Documents, ...). 

It'll work like this:

```txt 
deez@nuts: srm /home/user
Are you sure you wanna delete /home/user? It's a sensible path. y/N
```

```txt
deez@nuts: y
Okay, your choice.
```

```txt
deez@nuts: n
Probably the best choice.
```


### Risk levels example

## Low risk
`~/Downloads/tmp.txt`

## Medium risk
`~/Documents/`

## High risk
`/`
`~/`
`/home`


**del_time** ==> the time and date of the deletion of the file.

This is an **example** of the metadata. 

```json
{
"UUID": "7ea875ac-aba3-404e-8801-ec0255001e5c", 
"filename": "nutz.txt",
"dest": "/home/deez/.trash/files/7ea875ac-aba3-404e-8801-ec0255001e5c", 
"og_path": "/home/deez/projects/srm/nutz.txt", 
"del_time": "2026-03-04 22:42:47"
}
```

# About it

SRM is built in python *(ik, not the best for a tool like this, i might port it to c or cpp.)*, it was born as an app you run through the terminal (not a command, literally python3 srm.py ...) and then made into a CLI tool. 

I started building it out of pure boredom and to get a python refresher, i just noticed it could become an amazing project, so, here i am writing the docs for it. :)).

I started writing docs for it pretty late actually, i've been working on the first version of srm for something like 3/4 days, whoops..
# Devlog

#### ToDo
##### - Arguments
- **clean** ==> Delete *ALL* files in the *~/.trash/files* directory -- done 
	- clean **(n)** ==> delete files **older** than *'n'* days. -- not done
	- clean **xG** ==> delete files larger than *'x'* GB. -- not done
	- clean **xM** ==> delete files older than *'x'* MB. -- not done 

- **recover** ==> Recover a file from trash to it's original directory -- not done
	- recover *(file)* **directory** ==> Recover a file from the trash into a
	 specified directory. -- not done 

##### QoL 

## Sensible paths

I wanna introduce the recognition of sensible paths (e.g /, /home/user, /home/user/Documents, ...). 

It'll work like this:

```txt 
deez@nuts: srm /home/user
Are you sure you wanna delete /home/user? It's a sensible path. y/N
```

```txt
deez@nuts: y
Okay, your choice.
```

```txt
deez@nuts: n
Probably the best choice.
```


### Risk levels example

## Low risk
`~/Downloads/tmp.txt`

## Medium risk
`~/Documents/`

## High risk
`/`
`~/`
`/home`

## Problems 

- When moving a file to the trash directory, it's data is erased. -- fixed (08/03/26 [02:35 am])
- Directories aren't handled right. -- fixed (08/03/26 [02:35 am])


### Actual devlog

###### 8th March 2026 - 01:13 am
Today, i'll **rewrite** srm from scratch.. i wanna do it because, even tho i didn't write THAT much code, adding functionalities and stuff is becoming pretty stressing. I adapted a "new" file structure.

now:

```abc
srm_rewrite/
└── src
    ├── clean.py
    ├── list.py
    ├── recover.py
    └── srm.py
```

before:

```abc
srm/
└── src
    └── srm.py
t
```
(i know, pretty shitty.) 

and adding a function everytime was SO UGLY.

as you can already imagine, srm.py will be the *main* file, containing the parser (that thing that allows you to run srm with arguments.), while *clean.py - list.py - recover.py* will be the files that will contain the code to clean the trash folder, list the files (and metadata) in the trash folder and to recover the files. 

I guess recover.py will be the hardest one to build, since i'll have to deal with original paths and stuff.. BUT, what i'm dealing with right now is: moving files to trash without losing their contents.. I don't know how to do that tbh.... (well, i do know, but im stubborn and wanna keep the idea of changing the file's name into a uuid, instead of just moving the file.)
*(I think i'll do this in two hours (i feel like i'll do most of it now and continue when i wake up tomorrow but u got the idea.).. Still no cpp porting, i don't think it'll be that useful, i'll do it when i'm bored of python i guess. )* --- in the end, i got into the doomscrolling abyss and went to sleep at 4am, doing almost nothing..... 

**BUT NOW** i'm working on the configuration file! 
```python 
# config.py

import os
from pathlib import Path


def init():
    
    home = os.path.expanduser("~")
    trash_dir = Path.home() / ".trash"
    trash_dir_files = trash_dir / "files"
    trash_dir_metadata = trash_dir / "metadata"
    
    trash_dir.mkdir(exist_ok=True)
    trash_dir_files.mkdir(exist_ok=True)
    trash_dir_metadata.mkdir(exist_ok=True)

    return home, trash_dir, trash_dir_files, trash_dir_metadata
```


###### 9th March 2026 -- 00:02 am

I added the list feature, i admit i used a little bit of AI to help me out with it, i wouldn't have done it normally, but i know i couldn't have done it myself. What i did with AI is just printing nicely the files with all the heading and stuff, the logic is all mine. 