import os
from dotenv import load_dotenv
from guardrails import Guard
from guardrails.hub import DetectJailbreak, RegexMatch, LlmRagEvaluator, HallucinationPrompt

# Load environment variables from .env file
load_dotenv()

best_client_input = Guard(
    name='best-client-input',
    description='Checks that a string is in Title Case format.'
).use(
    DetectJailbreak
)

best_client_output = Guard(
    name='best-client-output',
    description='Checks that the LLM output does not contain any hallucinations.',
).use(
    LlmRagEvaluator(
        eval_llm_prompt_generator=HallucinationPrompt(prompt_name='hallucination_judge_llm'),
        llm_evaluator_fail_response='hallucinated',
        llm_evaluator_pass_response="factual",
        llm_callable="gpt-4o-mini",
        on_fail="exception",
        on="prompt"
    )
)