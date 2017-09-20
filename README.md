# Mail-Service-Testing-Tool

## Basic Overview

[![Build Status](https://travis-ci.org/saurabhmarpadge/Mail-Service-Testing-Tool.svg?branch=master)](https://travis-ci.org/saurabhmarpadge/Mail-Service-Testing-Tool)
Testing tool to send mails simultaneously from different Mailing Services such as Outlook, Gmail and Yahoo. Time interval and number of times the mails should be sent can be configured. 

## Install

  In order to use Mail Service Testing Tool, you need Python installed. In order to do so, you should install Python >= 2.7 from ![here](https://www.python.org/downloads/).

```
git clone https://github.com/saurabhmarpadge/Mail-Service-Testing-Tool.git
```

Consider using a virtualenv:

```
$ pip3 install virtualenv
$ virtualenv venv        # On Linux
$ venv\scripts\activate  # On Windows
```

Now install dependencies 

```
(venv)$ pip install -r requirements.txt
```

## Working

![Demo](https://github.com/saurabhmarpadge/Mail-Service-Testing-Tool/blob/master/Pic/demo.gif)

## Contribute

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:

- Fork the repo
- Create a new branch (`git checkout -b improve-feature`)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (`git commit -am 'Improve feature'`)
- Push to the branch (`git push origin improve-feature`)
- Create a Pull Request 
