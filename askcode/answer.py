"""Step 4, part B: check the AI's reply before your program trusts it.

YOUR CODE. Read HANDOUT.md, Step 4, first.
Check your work with:  pytest tests/test_answer.py
"""

from __future__ import annotations

import json  # noqa: F401  (you will need it)

from askcode.core import BadReply  # noqa: F401  (raise this for every bad reply)


def parse_reply(text: str) -> dict:
    """Check the model's reply and return {"answer": ..., "file": ..., "line": ...}.

    Accept the reply only if every rule holds. Otherwise raise BadReply with a short
    message that says which rule failed. Never let a different exception escape.

    1. After stripping whitespace, the reply is one JSON object. The only thing
       allowed around it is a single Markdown code fence: a first line of ``` or
       ```json, and a last line of ```. Any other text before or after the object
       makes the reply bad.
    2. The object has exactly the keys "answer", "file" and "line": none missing,
       none extra.
    3. "answer" is a string that is not empty or only whitespace.
    4. "file" is a non-empty string or null. "line" is an integer or null; true and
       false do not count as integers, and an integer line must be at least 1.
    5. "file" and "line" are both null, or both set.

    Return a new dict with exactly the three keys and the values from the reply.
    """
    if not isinstance(text, str):
        raise BadReply("reply is not text")

    body = text.strip()
    if body.startswith("```"):
        lines = body.split("\n")
        if len(lines) < 3 or lines[0].strip() not in ("```", "```json") or lines[-1].strip() != "```":
            raise BadReply("rule 1: code fence must be a ``` or ```json line and a closing ``` line")
        body = "\n".join(lines[1:-1]).strip()

    if not body.startswith("{"):
        raise BadReply("rule 1: reply is not a single JSON object")
    def no_duplicate_keys(pairs: list) -> dict:
        keys = [key for key, _ in pairs]
        if len(keys) != len(set(keys)):
            raise BadReply("rule 2: a key appears more than once")
        return dict(pairs)

    try:
        data = json.loads(body, object_pairs_hook=no_duplicate_keys)
    except BadReply:
        raise
    except (json.JSONDecodeError, ValueError, RecursionError) as error:
        raise BadReply(f"rule 1: not valid JSON, or text around the object ({error})") from None
    if not isinstance(data, dict):
        raise BadReply("rule 1: reply is not a JSON object")

    if set(data) != {"answer", "file", "line"}:
        raise BadReply(f"rule 2: keys must be exactly answer, file, line; got {sorted(data)}")

    answer, file, line = data["answer"], data["file"], data["line"]

    if not isinstance(answer, str) or not answer.strip():
        raise BadReply("rule 3: answer must be a non-empty string")

    if file is not None and (not isinstance(file, str) or not file.strip()):
        raise BadReply("rule 4: file must be a non-empty string or null")
    if line is not None:
        if isinstance(line, bool) or not isinstance(line, int):
            raise BadReply("rule 4: line must be an integer or null")
        if line < 1:
            raise BadReply("rule 4: line must be at least 1")

    if (file is None) != (line is None):
        raise BadReply("rule 5: file and line must both be null or both be set")

    return {"answer": answer, "file": file, "line": line}