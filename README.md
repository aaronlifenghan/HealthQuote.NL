Dutch Metaphor Extraction and Collection Project in the healthcare and cancer domain - resources to share


# Phase-1: Dutch Metaphor Extraction from Cancer Patients' Interviews and Forum Data using LLMs and Human in the Loop

# Summary
Metaphors and metaphorical language (MLs) play an important role in healthcare communication between clinicians, patients, and patients' family members. In this work, we focus on Dutch language data from cancer patients. We extract metaphors used by patients using two data sources: (1) cancer patient storytelling interview data and (2) online forum data, including patients' posts, comments, and questions to professionals. We investigate how current state-of-the-art large language models (LLMs) perform on this task by exploring different prompting strategies such as chain of thought reasoning, few-shot learning, and self-prompting. With a human-in-the-loop setup, we verify the extracted metaphors and compile the outputs into a corpus named HealthQuote.NL. We believe the extracted metaphors can support better patient care, for example shared decision making, improved communication between patients and clinicians, and enhanced patient health literacy. They can also inform the design of personalized care pathways. We share prompts and related resources at this Github URL

# Resources:
Initial Instruction Prompts.docx - the Initial Instruction Prompts (IPs) we used on LLMs.

RPrompt-1.docx - the Refined Prompts with LLM assistance and human refinement for LLMs with Chain of Thoughts, examples.

RPrompt-2.docx - the Refined Prompts with LLM assistance and human refinement for LLMs with Chain of Thoughts, and the full English MetaphorMenu as context within the prompt.

healthquoteNL_2511.06427v1.pdf - the preprint paper of this stage with methodology and extracted Dutch metaphor examples and their alignment to the original English MetaphorMenu.

HealthQuote.NL corpus - cleaning up to share (accessible on demand/request)


# Reference:

@misc{han2025dutchmetaphorextractioncancer,
      title={Dutch Metaphor Extraction from Cancer Patients' Interviews and Forum Data using LLMs and Human in the Loop}, 
      author={Lifeng Han and David Lindevelt and Sander Puts and Erik van Mulligen and Suzan Verberne},
      year={2025},
      eprint={2511.06427},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2511.06427}, 
}

# contact 
L(dot)Han@lumc.nl
