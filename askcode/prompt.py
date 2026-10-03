"""Step 4, part A: the five-part prompt from the Week 3 slides.

YOUR CODE. Read HANDOUT.md, Step 4, first.
Check your work with:  pytest tests/test_prompt.py
"""

from __future__ import annotations

from askcode.core import NO_CODE, Chunk, Prompt, format_chunk  # noqa: F401


SYSTEM_PROMPT = """Goal:
You answer a developer's question about the Python `requests` library, using only the
code that is shown to you, and you point to the file and line that supports the answer.

Inputs and outputs:
Input: a "Code:" section with one or more functions. Each function starts with a header
line "### <file>, <function name>, lines <start> to <end>", and every code line after it
begins with its line number. After the code comes a "Question:" line and the question.
Output: one JSON object that answers the question and cites one file and one line.

Rules:
1. Answer only from the code shown. Do not use what you remember about requests or
   any other library, and do not guess.
2. Keep the answer short: one to three sentences that a new teammate can act on.
3. "file" is the file name exactly as written in the header of the function you used,
   for example "sessions.py".
4. "line" is the single line number, as printed before the code, that best supports
   your answer. It must be a line inside the function you cite.
5. If the code shown does not answer the question, reply with the answer
   "not found in the code shown" and null for both "file" and "line". Do this also
   when no code is shown.
6. Reply with the JSON object only: no greeting, no explanation, no Markdown.

Example:
Question: What timeout does Session.close set before closing its adapters?
Code shows only `Session.close` in sessions.py, lines 794 to 797, which loops over
self.adapters and calls close() on each, with no timeout anywhere.
Correct reply:
{"answer": "not found in the code shown", "file": null, "line": null}
Question: How does Session.close close the session?
Correct reply:
{"answer": "It calls close() on every transport adapter in self.adapters.", "file": "sessions.py", "line": 797}

Reply format:
Exactly one JSON object with exactly these keys, and nothing before or after it:
"answer": a string,
"file": a string, or null,
"line": an integer, or null.
"file" and "line" are both null or both set."""


def build_prompt_five_part(question: str, chunks: list[Chunk]) -> Prompt:
    """Build the prompt your pipeline sends to the AI.

    Requirements. The tests check each one.

    1. prompt.system holds the five parts from slide 6. Each part starts on its own
       line with its label, in this order:
           Goal:
           Inputs and outputs:
           Rules:
           Example:
           Reply format:
    2. Rules tell the model to answer only from the code shown, and, when that code
       does not answer the question, to reply with the answer
       "not found in the code shown" and null for both file and line.
    3. Example holds one sample question and its correct reply written as a JSON
       object with the keys "answer", "file" and "line". Do not use one of your own
       ten questions.
    4. Reply format asks for exactly one JSON object with the keys "answer" (a string),
       "file" (a string or null) and "line" (an integer or null), with nothing before
       or after it.
    5. prompt.system is the same text for every question and every set of chunks.
       It is the stable part of the prompt, so it goes first (slide 26).
    6. prompt.user is a line "Code:", then every chunk shown with format_chunk(chunk)
       in the order given, separated by blank lines, then a line "Question:", then
       the question. The question comes last. If chunks is empty, put NO_CODE under
       "Code:" instead.
    """
    if chunks:
        code = "\n\n".join(format_chunk(chunk) for chunk in chunks)
    else:
        code = NO_CODE
    user = f"Code:\n{code}\n\nQuestion:\n{question}"
    return Prompt(system=SYSTEM_PROMPT, user=user)