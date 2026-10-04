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

## Entry 5
artifact:  askcode/search_words.py at commit
tool:      Claude Opus 5.5 on claude.ai
prompts:   Claude wrote search_words following the
           six scoring steps in the docstring; prompts/searchwords.md
review:    <what you read; e.g. whether you checked that ties keep corpus order
           via the (-score, index) sort key, and that zero-df words are ignored>
checks:    pytest tests/test_search_words.py: 100% pass
evidence:  HANDOUT Step 3, search_words.py docstring steps 1 to 6
risk:      no stemming or length normalization, so plural and paraphrased
           questions miss (q02 "redirects") and long functions such as
           resolve_redirects rank high on unrelated questions (q04, q05, q06);
           behaviour on the hidden tests is unverified

## Entry 6
artifact:  askcode/answer.py at commit 
tool:      Claude Opus 5.5 on claude.ai
prompts:   asked Claude to implement the assignment's code files from the handout;
           Claude wrote parse_reply from the five rules in the docstring;
           prompts/answer.md
review:    read parse_reply section by section against docstring rules 1 to 5;
           confirmed the fence must be whole first/last lines, duplicate keys are
           rejected via object_pairs_hook, BadReply is re-raised before the
           ValueError handler, and bool is excluded from line; 
checks:    pytest tests/test_answer.py: 15 passed n 0.01s
evidence:  HANDOUT Step 4 part B, answer.py docstring rules 1 to 5
risk:      a reply that passes is well formed, not true: parse_reply does not
           check that "file" was one of the files shown or that "line" falls
           inside a shown function, so a confident wrong citation passes;
           behaviour on the hidden tests is unverified

## Entry 7
artifact:  results/top3_words_five_part.csv, results/whole_five_part.csv,
           results/gold_five_part.csv and ai_replies/ at commit 5da3b62
tool:      askcode run_eval, openai gpt-6-luna
prompts:   
review:    read all 30 replies and marked the correct column in each file against
           expected_answer in questions.json; marked q10 yes only where the reply
           said not found; marked every valid_json = no row as no; assigned a fault
           to each top3 miss using the Step 5 rule and Table 3
checks:    python3.12 -m askcode.run_eval --context whole --prompt five_part --dry-run:
           estimated 545,375 input tokens, about $0.1091;
           python3.12 -m askcode.run_eval --search words --context top3 --prompt five_part:
           valid JSON 10 of 10, right place 4 of 10;
           Estimated Tokens: 24,188 in, 846 out, cost: $0.0053
           python3.12 -m askcode.run_eval --context gold --prompt five_part:
           valid JSON 10 of 10, right place 10 of 10;
           python3.12 -m askcode.summary: Tables 2 and 3 printed
evidence:  HANDOUT Step 5
risk:      one run per configuration, so a fresh run may answer differently;
           correct marks are my own judgement against expected_answer;
        

## Entry 8
artifact:  askcode/search_meaning.py at commit 
tool:      Claude Opus 5.5 on claude.ai
prompts:   asked Claude to implement the assignment's code files from the handout,
           which included search_meaning.py; later pasted the HANDOUT Step 7 text
           asking for cosine and MeaningIndex, and Claude confirmed the existing
           version, reran its tests, and explained it; prompts/claude-search-meaning.md
review:    
checks:    pytest tests/test_search_meaning.py: 6 passes in 0.01s
           python3.12 -m askcode.run_eval --search meaning --no-ai:
           
evidence:  HANDOUT Step 7, search_meaning.py docstring rules
risk:      

## Entry 9
artifact:  results/top3_words_five_part.csv, results/whole_five_part.csv,
           results/gold_five_part.csv and ai_replies/ at commit <your SHA>
tool:      askcode run_eval, openai gpt-6-luna, 
           Claude Opus 5.5 on claude.ai, to compare my correct marks
           with expected_answer and to check the dry run
prompts:   
review:    read all 30 replies and marked the correct column against expected_answer;
           first marked every top3 row yes, then re-marked q02, q04, q05, q06 and q08
           as no, because "not found in the code shown" (and the hedged q04 reply)
           did not match the expected answers; kept q07 yes because its core claim
           ("not only 200") is right; marked all whole and gold rows yes after reading
           each reply; 
checks:    python3.12 -m askcode.run_eval --context whole --prompt five_part --dry-run:
           estimated 545,375 input tokens, about $0.1091;
           python3.12 -m askcode.run_eval --search words --context top3 --prompt five_part:
           valid JSON 10 of 10, right place 4 of 10;
           python3.12 -m askcode.run_eval --context whole --prompt five_part:
           valid JSON 10 of 10, right place 10 of 10;
           python3.12 -m askcode.run_eval --context gold --prompt five_part:
           valid JSON 10 of 10, right place 10 of 10;
           python3.12 -m askcode.summary: Table 3 lists q02, q04, q05, q06, q08,
           all hit no and correct with gold context yes
evidence:  HANDOUT Step 5; REPORT.md sections 1 and 2
risk:      one run per configuration on 10 questions, so a fresh run may differ;
           correct marks are my own judgement against expected_answer;
           q02's expected value (30) is set at module level, outside every chunk,
           so no chunk-based context contains it
result:    correct: top3 5 of 10, whole 10 of 10, gold 10 of 10;
           input / output tokens: top3 24,188 / 846, whole 550,025 / 682,
           gold 8,041 / 411; cost at $0.20 / $0.50 per MTok: top3 $0.0053,
           whole $0.1103, gold $0.0018;
           faults for top3 misses: retrieval 5, generation 0, both 0;
           results/top3_words_five_part.csv, whole_five_part.csv, gold_five_part.csv
changed:   every top3 miss was a retrieval failure and gold was perfect, so the
           bottleneck is search, not the prompt; I kept the prompt unchanged and
           compared meaning search on the same questions in Step 7 (8 of 9 in the
           top 3 vs 3 of 9 for word search); I used whole vs top3 cost and accuracy
           for the decision rule in REPORT.md section 2