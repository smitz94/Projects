# TWITTER BOT- RUSTY

This program analyzes the mentions to this bot and retweet back according to the **greetings** and **sentiments** of the mentions. 
It responds back in every 15 seconds to the mentions.

_Language used_ : **PYTHON** 

_Libraries used_ : [**tweepy**](http://docs.tweepy.org/en/latest/#), [**textblob**](https://textblob.readthedocs.io/en/dev/) 
and [**time**](https://docs.python.org/3/library/time.html)

> Get a developer twitter account before beginning to code for this Bot.

## PRE-REQUISITE

```bash
Install tweepy and textblob using terminal or command prompt

pip install tweepy

pip install textblob

if that doesnt work try to install nltk first

pip install nltk

pip install -U git+https://github.com/tweepy/tweepy.git@2efe385fc69385b57733f747ee62e6be12a1338b

```
## HOW TO CODE

[RUSTY_BOT.PY](https://github.com/smitz94/Projects/blob/master/Twitter%20Bot-Rusty/rusty_bot.py)

This file consists of program that is the script of the bot and going to initiate the bot to analyse and reply to the mentions.

* Create api object to interact- read and write on twitter.
* Use type() function on several parameters in twitter data we find there are classes and objects present in the data.
* Convert class object to dictionary and then analyse the data.
* **_Sentiment Analysis_** is part of [NLP](https://www.datacamp.com/community/tutorials/simplifying-sentiment-analysis-python), where sentiments
**_polarity_** determines whether it is negative, positive or neutral.

[KEYS.PY](https://github.com/smitz94/Projects/blob/master/Twitter%20Bot-Rusty/keys.py)

Add your generated **_Consumer Keys_** and **_Access Keys_** here.

## RESULTS

* **INITIATION

![](https://github.com/smitz94/Projects/blob/master/Twitter%20Bot-Rusty/img1.png)

* **GREETINGS

![](https://github.com/smitz94/Projects/blob/master/Twitter%20Bot-Rusty/img4.png)

* **NEGATIVE MENTION

![](https://github.com/smitz94/Projects/blob/master/Twitter%20Bot-Rusty/img3.png)

* **POSITIVE MENTION

![](https://github.com/smitz94/Projects/blob/master/Twitter%20Bot-Rusty/img2.png)
