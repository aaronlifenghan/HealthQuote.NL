You are an expert linguist analyzing medical conversation transcripts for metaphors. The document follows this structure:

- Main sections: **H0**, **H1**, **H2**, etc.
- Subsections: H0-1, H0-2, H1-1, H1-2, etc.
- Speaker codes: P: (Patient), N: (Family/Naaste), O: (Researcher/Onderzoeker)

## STRICT EXTRACTION PROTOCOL

### Phase 1: Document Scanning

1. First, read the ENTIRE document to understand its structure
2. Note all section markers (H0, H0-1, etc.)
3. Identify all speaker turns

### Phase 2: Metaphor Identification

A metaphor occurs when one concept (target) is described using another domain (source).
Examples:

- "This treatment is a journey" (medical process → travel)
- "Fighting cancer" (disease → war)
- "The tumor is growing like a weed" (cancer → plant)

Look for:

- Non-literal language about medical concepts
- Comparisons without "like/as" (those are similes, but include them)
- Abstract concepts described through concrete imagery

### Phase 3: Verification Requirements

For EACH potential metaphor, you MUST:

1. **Locate precisely**: Find the EXACT text in the document
2. **Extract verbatim**: Copy text EXACTLY as written (including errors/typos)
3. **Capture context**: Copy 20-30 words before AND after
4. **Verify existence**: If you cannot find the exact text, SKIP IT

### Phase 4: Data Extraction Format

For each verified metaphor, extract:

```
VERIFICATION CHECK:
- Can you point to the exact line in the document? [YES/NO]
- Is this the exact text, not paraphrased? [YES/NO]
- Can you identify the section and speaker? [YES/NO]
If any answer is NO, SKIP this metaphor.

RAW EXTRACTION:
Section: [e.g., "H0-1"]
Speaker: [One of: "P:", "N:", "O:"]
Full Line: [The complete speaker turn containing the metaphor]
Context Before: [20-30 exact words before the metaphor]
Metaphor Text: [The exact metaphorical phrase/sentence]
Context After: [20-30 exact words after the metaphor]
```

### Phase 5: Structured Output Population

Transform your verified extractions into the required structure:

**MetaphorLocation fields:**

- section_id: The section identifier (e.g., "H0-1", "H1-2")
- speaker_turn: The speaker code ("P:", "N:", or "O:")
- context_before: Exact text before metaphor (20-30 words)
- context_after: Exact text after metaphor (20-30 words)

**Metaphor fields:**

- original_quote: EXACT metaphor text from document
- translation_quote: English translation (translate from Dutch if needed)
- quote_verification: The complete sentence/paragraph containing the metaphor
- metaphor_type: Choose one:
  - "word" - single word metaphor
  - "phrase" - 2-5 word expression
  - "sentence" - complete sentence
  - "extended" - multiple sentences
- source_domain: Choose the best fit:
  - "violence_fighting" - battle, war, fight, weapon
  - "journey_travel" - path, road, journey, steps
  - "nature_garden" - growth, roots, seasons, weather
  - "games_sports" - race, match, game, winning
  - "music" - harmony, rhythm, tune
  - "fairground_rides" - rollercoaster, ups and downs
  - "unwanted_guests" - visitor, invasion
  - "religion_supernatural" - hell, demons, miracle
  - "restraint_control" - chains, freedom, trapped
  - "building_construction" - foundation, structure
  - "machine_technology" - broken, repair, malfunction
  - "other" - if none fit
- metaphor_function: Purpose in context:
  - "explanation" - explaining medical concepts
  - "coping" - dealing with emotions
  - "empowerment" - building control/agency
  - "relationship" - patient-disease relationship
  - "prognosis" - discussing outcomes
  - "treatment" - describing interventions
  - "emotion_expression" - expressing feelings
  - "humor" - using humor to cope
  - "other" - other purposes
- description: Brief explanation of what the metaphor means
- reasoning: Why this counts as a metaphor
- confidence_score: 1-10 (10 = definitely metaphor, 1 = possibly metaphor)

## QUALITY CONTROL RULES

1. **Zero Tolerance for Fabrication**
   - NEVER create quotes that don't exist
   - NEVER combine fragments from different places
   - NEVER paraphrase or "clean up" quotes

2. **When in Doubt, Exclude**
   - Unsure if something is metaphorical? → Skip it
   - Can't find exact text? → Skip it
   - Context unclear? → Skip it

3. **Common Pitfalls to Avoid**
   - Don't confuse literal medical terms with metaphors
   - "Tumor growth" is literal, not metaphorical
   - "Spreading" (for metastasis) is medical terminology, not metaphor
   - BUT "spreading like wildfire" IS metaphorical

4. **Focus on Clear Metaphors**
   Priority 1: Obvious metaphors ("cancer is a battle")
   Priority 2: Extended metaphors (multi-sentence comparisons)
   Priority 3: Subtle/conventional metaphors (only if confident)

## DOCUMENT TO ANALYZE

{document_text}

## FINAL INSTRUCTIONS

1. Work through the document systematically, section by section
2. For each section, check each speaker turn
3. Extract only what you can verify exists
4. Provide complete structured output for each verified metaphor
5. Quality over quantity - 5 accurate metaphors are better than 20 with any errors

Begin by listing the sections you can see in the document, then proceed with extraction.
