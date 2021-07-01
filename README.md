# MyDict

> Created on 2021/07/01

## Introduction

This is a lightweight personal dictionary app. User can CRUD the vocabularies when reading second-language book, etc. 

## Usage

Sorry there is only source code here. The usage is simple. `cd` to *src*, then

```bash
$ python3 dict.py
```

Then you are all set.

## Commands

### 1. put

#### Put a word

```bash
>> put {word} {definition to the word}
```

> separate by at least one space

##### Example

```bash
>> put apple 苹果
```

#### Put a phrase

Simply type *"put"*, then press enter.

```bash
>> put
```

Then follow the instruction:

```
>> Enter phrase: apple juice
>> Enter definition: 苹果汁
```

> Actually  you add a **word** in this way...

### 2. get

#### Conventional get

```bash
>> get apple
苹果
```

Or simply

```bash
>> apple
苹果
```

> Of course, "apple" has be in the dictionary

### 3. delete

```bash
>> del apple
success.
```

### 4. list

```bash
>> list
27 words total.

preceding    先前的
crisis    危机, 紧要关头; (crises 复数)
orthodoxy    正统
slump    衰弱;跌落;低潮状态
stimulus    刺激物
progenitor    先驱;创始人
...
```

### 5. save

Mannually save changes.

```bash
>> save
success.
```

### 6. exit

```bash
>> exit

Auto saving...
Bye!
```

You can also do ctrl + C to exit. These two ways are safe exiting, otherwise, your change would lost.