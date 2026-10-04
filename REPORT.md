# Assignment 2 Report: Ask the Code

Name:
Provider and model:
Prices used (per million tokens, input and output), and the page you found them on:

## Table 1. Finding the right function

Paste Table 1 from `python -m askcode.summary` here, exactly as printed.


| Run | Right function in top 3 |
| --- | --- |
| retrieval_words | 3 of 9 |
| retrieval_meaning | 8 of 9 |

## Table 2. Answers


| Run | Valid JSON | Right place | Correct (your marks) | Input tokens | Output tokens | Cost (USD) |
| --- | --- | --- | --- | --- | --- | --- |
| top3_words_five_part | 10 of 10 | 4 of 10 | 10 of 10 | 24,188 | 846 | 0.0053 |
| whole_five_part | 10 of 10 | 10 of 10 | 10 of 10 | 550,025 | 682 | 0.1103 |
| gold_five_part | 10 of 10 | 10 of 10 | 10 of 10 | 8,041 | 411 | 0.0018 |
| top3_words_minimal | 0 of 10 | 0 of 10 | 0 of 10 | 19,428 | 3,824 | 0.0058 |

## 1. Whose fault is it? (Step 5)

One row for every question marked `no` in top3_words_five_part. Take the first three
columns from Table 3 of `python -m askcode.summary`. Fault is retrieval, generation or
both, following the rule in Step 5. Evidence is one sentence about what you saw in the
reply or the retrieved functions.

| Question | Hit in top 3 | Correct with gold context | Fault | Evidence |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## 2. Paste everything or search? (Step 5)

In the particular instance cost was negilible between top3_words_five_part vs gold_five_part. Although, cost was negligible in this instance it really depends on the size of the code and in some cases may not be  advisable to upload entire code as it may skew the results or may not improve the results at all and it is better to do specific search when code bases are big

## 3. Minimal prompt against five-part prompt (Step 6)

Five part did better than minimal. Right place was 4 out of 10 and correct 10 out of 10 compared to minimal where both were 0 out of 10. 
q01, the POST-and-301 question. Both prompts gave essentially the same answer: the follow-up request uses GET. The difference was the format of line. Five-part replied with "file": "sessions.py", "line": 350, an integer inside rebuild_method, so it passed the check and landed in the right place. Minimal replied with "line": "348–353", a text range. That fails parse_reply rule 4 ("line must be an integer"), so the reply was marked invalid JSON, wrong place and incorrect, even though its content was right.

THe only change was the prompt between both runs leading to a belief prompt was the reason

## 4. Word search against meaning search (Step 7)

q06. Word search ranked merge_setting outside the top 3, and meaning search ranked it 1st. The question never uses the function's own words ("merge", "setting"), and its words that do match ("headers", "session", "request", "None") appear in many functions, so they carry little weight. The embedding matches the meaning of "combining the request's settings with the session's and dropping None values" directly.

q03. Word search ranked get_encoding_from_headers 1st, and meaning search ranked it 2nd. The question contains rare, distinctive words ("charset", "encoding", "Content-Type") that appear in only a few functions and so get heavy weights. To the embedding, it's one of several encoding-related functions with similar meaning, and a near neighbour edged ahead. To make that last clause specific, open results/retrieval_meaning.csv and name the function meaning search ranked 1st for q03.

The overall picture is worth a sentence too. Word search had 3 of 9 in the top 3, and meaning search had 8 of 9. They fail in opposite directions, as the week 4 material says word search wins on rare exact tokens, and meaning search wins on paraphrase.

## 5. Your decision rule (Step 8)

One rule for this codebase: when would you paste everything, and when would you search?
Cite the measured cost and the measured correct count of both designs.

Run|	Input tokens (10 questions)	|Output tokens	|Cost	|Per question	|Correct
Paste everything (whole)	550,025	682	$0.1103	about $0.011	10 of 10
Search (top3 words)	24,188	846	$0.0053	about $0.0005	10 of 10

For this codebase, I would paste everything when I need a correct answer to a small number of questions, and search when I am answering many questions or the codebase grows. Pasting the whole of requests (about 55,000 input tokens per question) answered 10 of 10 correctly for $0.1103, while top-3 word search answered <N> of 10 for $0.0053: about 21 times cheaper, but it failed whenever retrieval missed the right function. At about one cent per question, the whole codebase fits in the model's context and the accuracy is worth the price for one-off questions.
At thousands of questions a day, or for a codebase too large for the context window, the 21× cost difference dominates, so I would search, preferably with meaning search, which found 8 of 9 answerable questions in the top 3 versus 3 of 9 for word search.