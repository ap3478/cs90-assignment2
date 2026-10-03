# Provenance Ledger

Write one entry per reviewable change or experiment, when the work is done. Use exactly
the schema in HANDOUT.md. Put the prompts you typed into AI tools in `prompts/` and name
the file in the entry's `prompts` field.

## Worked example (not graded; leave it here and add your entries under "My entries")

This shows the level of detail expected. The commit SHAs, dates and numbers are made up.

```
## Entry 2
artifact:  askcode/split.py at commit 3f2a9c1
tool:      GitHub Copilot Chat in VS Code, model Claude Haiku 4.5, 2026-09-22
prompts:   asked for an ast loop that returns methods with class-qualified names;
           prompts/split-01.md
review:    read every line; rejected its use of ast.walk, which also returned nested
           functions and broke rule 1; rewrote the loop over tree.body and class bodies
           myself; kept its decorator handling after checking it against rule 3
checks:    pytest tests/test_split.py: 8 passed
evidence:  HANDOUT Step 2, split.py docstring rules 1 to 6
risk:      I did not test a file with Windows line endings

## Entry 5
artifact:  results/top3_words_five_part.csv at commit 8d41e07
tool:      askcode run_eval, anthropic claude-haiku-4-5-20251001, 2026-09-23
prompts:   the five-part prompt in askcode/prompt.py at commit 8d41e07;
           prompts/five-part-v1.md
review:    read all ten replies and marked the correct column against questions.json
checks:    python -m askcode.run_eval --search words --context top3 --prompt five_part:
           valid JSON 10 of 10, right place 6 of 10
evidence:  HANDOUT Step 5
risk:      one run only; a fresh run may answer differently
dataset:   questions/questions.json at commit 51c0e2a; corpus requests v2.32.3
result:    correct 6 of 10, 24,113 input tokens; results/top3_words_five_part.csv
changed:   two misses were retrieval failures, so I looked at why word search missed
           them before touching the prompt
```

## My entries

## Entry 1
artifact:Pythonversion
tool:claude Opus 5.5
prompts:Installed Python3.12 using brew install @python3.12 but python --version still shows python 3.9.6
review: Response was use python3.12 --version command instead of python3 --version
checks:Ran command python3.12 --version in terminal
evidence:confirmed 3.12 version and also no errors detected when pip install -r requirements.txt was ran
risk:

## Entry 2
artifact:Pricing model for the .env file
tool:https://openai.com/business/pricing/#api
prompts:Input and output pricing 
review:
checks:Validated against GPT-6 models
evidence:$.10 for Input and $.50 for output
risk:GPT-6 has 2 models 6 and 5.6. May produce results for 5.6 which are higher and do not appear on the homepage of the API pricing models

## Entry 3
artifact:prompts/chunkandast.md
tool:google gemini
prompts:what is a chunck in python and how does it integrate with ast module
review: Read all replies to understand to under Chunk and how ast module plays a crucial role in splitting the data and providing a meaningful boundary when splitting the data
checks:Validated against GPT-6 models
evidence:Python's built-in ast (Abstract Syntax Tree) module parses source code into a hierarchical tree of syntactic nodes. Instead of naively splitting a file every N lines or tokens—which often breaks functions in half and ruins code context—an AST-driven chunker uses the ast module to find precise semantic boundaries
risk:

## Entry 4
artifact:  askcode/split.py
tool:      Claude Opus 5.5 on claude.ai
prompts:   pasted my failing pytest output and asked why it failed; Claude
           diagnosed that askcode/split.py was still the starter code
review:    read the traceback with Claude's explanation: all 8 failures ended at
           askcode/split.py:43 raising NotImplementedError, the template's
           placeholder. I never saved the file after writing the code and pytest was still running the tests against the example code
checks:    Verify the files are saved after each edit and there is no original code or placeholder codes in place
evidence:  HANDOUT Step 2, Done when: pytest tests/test_split.py passes
risk:      none for the splitter logic itself; verify accuracy and ensure the new codes are saved
