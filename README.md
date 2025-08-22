# 🚀 LLM Bug Buster Challenge

Welcome to the **Mini LLM Debugging Challenge** 🎯  
This challenge is part of **GirlScript Summer of Code (GSSoC)** micro-event.

---

## 📌 Problem Statement
You are tasked with fixing a buggy **mini language model simulation**.  
The program is supposed to predict the **next word** based on word frequency from a given text corpus.

---

## 🐞 Buggy Code
Check the `buggy_code.py` file.  
It contains multiple logical and syntax errors. Your task is to **fix them**.

---

## ✅ Expected Behavior
- Input: `"I"` → Output: `"love"`
- Input: `"love"` → Output: `"coding"` (or most frequent)
- Input: `"python"` → Output: `"is"`
- Input: `"open"` → Output: `"source"`

---

## 🎯 Task
1. Debug the code inside `buggy_code.py`.
2. Make sure your program produces the correct predictions.
3. Submit your fixed file as:
   - **Pull Request** (preferred), OR
   - Share your corrected code in a `.py` file.

---

## 📝 Instructions
- Only modify the logic, do not change the corpus.
- Use Python 3.x.
- Bonus Task: Modify the program to return **top 3 probable words**.

---

## 🏆 Example Run
```bash
$ python buggy_code.py
love
coding
is
source
```

---

## ⚡ Rules
- Do NOT change the input corpus.
- Do NOT hardcode outputs.
- Your fix must be generic enough to work on any text corpus.

---

Good luck & Happy Debugging 🚀  
